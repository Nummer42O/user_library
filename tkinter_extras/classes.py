import tkinter as tk
from tkinter.constants import *
from tkinter import font as tkfont
from functools import wraps
from time import perf_counter
import sys

from .constants import *
from .utility import *
from ..decorators import m_event, f_event, Debugger, wrapsAndExpand

#@wraps(tk.Spinbox)
class Spinbox(tk.Spinbox):
    @wraps(tk.Spinbox.__init__)
    def __init__(self, master = None, cnf = {}, **kw):
        cnf = tk._cnfmerge((cnf, kw));

        self._scroll = bool(cnf.pop("scroll", False));
        
        tk.Spinbox.__init__(self, master, cnf);

        if self._scroll:
            if sys.platform.startswith("linux"):
                self._up_id   = self.bind("<Button-4>", self._scrollup,   ADD);
                self._down_id = self.bind("<Button-5>", self._scrolldown, ADD);
            else:
                self._bind_id = self.bind("<MouseWheel>", self._scrollcmd, ADD);

    if sys.platform.startswith("linux"):
        @m_event
        def _scrollup(self):
            self.invoke("buttonup");

        @m_event
        def _scrolldown(self):
            self.invoke("buttondown");
    else:
        def _scrollcmd(self, event: tk.Event) -> None:
            if self._scroll:
                if event.delta > 0:
                    for _ in range( event.delta // 120):
                        self.invoke("buttonup");
                elif event.delta < 0:
                    for _ in range(-event.delta // 120):
                        self.invoke("buttondown");
    
    @wraps(tk.Spinbox.config)
    def configure(self, cnf=None, **kw):
        cnf = tk._cnfmerge((cnf, kw));

        if not cnf:
            return dict(tk.Spinbox.config(), scroll=False);

        scroll = bool(cnf.pop("scroll", self._scroll));
        if scroll != self._scroll:
            self._scroll = scroll;

            if scroll:
                if sys.platform.startswith("linux"):
                    self._up_id   = self.bind("<Button-4>", self._scrollup,   ADD);
                    self._down_id = self.bind("<Button-5>", self._scrolldown, ADD);
                else:
                    self._bind_id = self.bind("<MouseWheel>", self._scrollcmd, ADD);
            else:
                if sys.platform.startswith("linux"):
                    self.unbind("", self._up_id);
                    self.unbind("", self._down_id);
                else:
                    self.unbind("", self._bind_id);

        tk.Spinbox.config(self, cnf);
    config = configure;

    @wraps(tk.Spinbox.cget)
    def cget(self, key):
        if key == "scroll":
            return self._scroll;
        else:
            return tk.Spinbox.cget(self, key);
    __getitem__ = cget;

    @wraps(tk.Spinbox.keys)
    def keys(self):
        return tk.Spinbox.keyS() + ["scroll"];

#@wraps(tk.Text)
class moddedText(tk.Text): #standard keyboard shortcuts for text manipulation + "default text"
    _EXTRA = ("text", "text_fg", "text_bg", "text_font");
    _text: str;
    _text_fg: str;
    _text_bg: str;
    _text_font: typing.Union[str, tkfont.Font];

    @wraps(tk.Text.__init__)
    def __init__(self, master = None, cnf = {}, **kw):
        cnf, extra = filtercnf(cnf, kw, text="", text_fg="#555555", text_bg=None, text_font=None);

        tk.Text.__init__(self, master, cnf);
        self.__dict__.update({'_' + key: value for key, value in extra.items()});

        self._std_fg   = tk.Text.cget(self, "fg");
        self._std_bg   = tk.Text.cget(self, "bg");
        self._std_font = tk.Text.cget(self, "font");

        self._was_empty = None;

        if self._text:
            self._enter_id = self.bind("<FocusIn>",  self._enter, ADD);
            self._leave_id = self.bind("<FocusOut>", self._leave, ADD);

            self._leave();

        if self._text_bg is None:   self._text_bg   = self._std_bg;
        if self._text_font is None: self._text_font = self._std_font;


        self.bind("<Control-a>", self._select_all, ADD);
        self.bind("<Control-BackSpace>",
                  lambda event: self.delete(self.index(INSERT + ' -1 char wordstart +1 char'), INSERT),
                  ADD);
        self.bind("<Control-Delete>",
                  lambda event: self.delete(INSERT, self.index(INSERT + '  + 1 char wordend -1 char')),
                  ADD);
        self.bind("<Control-Shift-BackSpace>",
                  lambda event: self.delete(self.index(INSERT + ' linestart'), INSERT),
                  ADD);
        self.bind("<Control-Shift-Delete>",
                  lambda event: self.delete(INSERT, self.index(self.index(INSERT) + ' lineend')),
                  ADD);

        self.bind('<Control-g>', lambda x: print(self.index(SEL_FIRST), self.index(SEL_LAST)));

    @m_event
    def _select_all(self):
        self.tag_add(SEL, 0.0, self.index(END));
        self.mark_set(INSERT, END);
        self.see(INSERT);
        
        return "break";
    
    @m_event
    def _enter(self) -> None:
        if self._was_empty:
            self.delete(0.0, END);
            tk.Text.config(self, fg=self._std_fg, bg=self._std_bg, font=self._std_font);

            self._was_empty = None; #to check if currently in use

    @m_event
    def _leave(self) -> None:
        self._was_empty = (self.get(0.0, END) == '\n');

        if self._was_empty:
            self.insert(0.0, self._text);
            tk.Text.config(self, fg=self._text_fg, bg=self._text_bg, font=self._text_font);

    @wraps(tk.Text.configure)
    def configure(self, cnf = None, **kw):
        cnf, extra = filtercnf(cnf, kw, *self._EXTRA);

        if not cnf:
            return dict(tk.Text.config(self, cnf),
                        text=("text", None, None, "", self._text),
                        text_fg=("text_fg", None, None, "#555555", self._text_fg),
                        text_bg=("text_bg", None, None, None, self._text_bg),
                        text_font=("text_font", None, None, None, self._text_font));

        tk.Text.config(self, cnf);

        self._std_fg   = tk.Text.cget(self, "fg");
        self._std_bg   = tk.Text.cget(self, "bg");
        self._std_font = tk.Text.cget(self, "font");

        if "text" in extra and extra["text"] != self._text:
            if extra["text"]:
                self._enter_id = self.bind("<Enter>", self._enter, ADD);
                self._leave_id = self.bind("<Leave>", self._leave, ADD);
            else:
                self.unbind("", self._enter_id);
                self.unbind("", self._leave_id);
        
                if self._was_empty:
                    self.delete(0.0, END);
                    tk.Text.config(self, fg=self._std_fg, bg=self._std_bg, font=self._std_font);

        
        self.__dict__.update({'_' + key: value for key, value in extra.items()});

        if self._text_bg is None:   self._text_bg   = self._std_bg;
        if self._text_font is None: self._text_font = self._std_font;
    config = configure;

    @wraps(tk.Text.cget)
    def cget(self, key):
        if key in self._EXTRA:
            return getattr(self, '_' + key);
        else:
            return tk.Text.cget(self, key);
    __getitem__ = cget;

    @wraps(tk.Text.keys)
    def keys(self):
        return tk.Text.keys() + self._EXTRA;

#@wraps(tk.Entry)
class moddeddEntry(tk.Entry):
    _EXTRA = ("text", "text_fg", "text_bg", "text_font");
    _text: str;
    _text_fg: str;
    _text_bg: str;
    _text_font: typing.Union[str, tkfont.Font];

    @wraps(tk.Entry.__init__)
    def __init__(self, master = None, cnf = {}, **kw):
        cnf, extra = filtercnf(cnf, kw, text="", text_fg="#555555", text_bg=None, text_font=None);

        tk.Entry.__init__(self, master, cnf);
        self.__dict__.update({'_' + key: value for key, value in extra.items()});

        self._std_fg   = tk.Entry.cget(self, "fg");
        self._std_bg   = tk.Entry.cget(self, "bg");
        self._std_font = tk.Entry.cget(self, "font");
        self._std_show = tk.Entry.cget(self, "show");

        self._was_empty = None;

        if self._text:
            self._enter_id = self.bind("<FocusIn>", self._enter, ADD);
            self._leave_id = self.bind("<FocusOut>", self._leave, ADD);

            self._leave();

        if self._text_bg is None:   self._text_bg   = self._std_bg;
        if self._text_font is None: self._text_font = self._std_font;

        self.bind("<Control-a>", self._highlight_all, ADD);
        self.bind("<Control-BackSpace>", self._delete_text, ADD);
        self.bind("<Control-Delete>", self._delete_text, ADD);
        self.bind("<Control-Shift-BackSpace>",
                  lambda event: self.delete(0, INSERT),
                  ADD);
        self.bind("<Control-Shift-Delete>",
                  lambda event: self.delete(INSERT, END),
                  ADD);

    @m_event
    def _highlight_all(self):
        self.selection_range(0, END);
        self.icursor(END);
        self.xview_moveto(1);

        return "break";

    def _delete_text(self, event: tk.Event):
        pos = initial_pos = self.index(INSERT);
        text = tk.Entry.get(self);

        if not text: return;

        if event.keysym == "BackSpace": #<--
            if pos == self.index(END): pos -= 1; #Can not work with end index since it would raise IndexError in text string

            while pos > -1 and not (text[pos] == ' ' or text[pos] == '\n'):
                pos -= 1;
            
            tk.Entry.delete(self, pos + 1, initial_pos);
        elif event.keysym == "Delete": #Entf/Del
            end_pos = self.index(END);

            while pos < end_pos and not (text[pos] == ' ' or text[pos] == '\n'):
                pos += 1;
            
            tk.Entry.delete(self, initial_pos, pos);
    
    @m_event
    def _enter(self) -> None:
        if self._was_empty:
            tk.Entry.delete(self, 0, END);
            tk.Entry.config(self, fg=self._std_fg, bg=self._std_bg, font=self._std_font, show=self._std_show);

            self._was_empty = None; #to check if currently in use

    @m_event
    def _leave(self) -> None:
        self._was_empty = (tk.Entry.get(self) == '');

        if self._was_empty:
            tk.Entry.insert(self, 0, self._text);
            tk.Entry.config(self, fg=self._text_fg, bg=self._text_bg, font=self._text_font, show='');

    @wraps(tk.Entry.get)
    def get(self):
        if self._was_empty:
            return '';
        else:
            return tk.Entry.get(self);

    @wraps(tk.Entry.insert)
    def insert(self, index, string):
        if not self._was_empty:
            tk.Entry.insert(self, index, string);

    @wraps(tk.Entry.delete)
    def delete(self, first, last):
        if not self._was_empty:
            tk.Entry.delete(self, first, last);

    @wraps(tk.Entry.configure)
    def configure(self, cnf = None, **kw):
        cnf, extra = filtercnf(cnf, kw, *self._EXTRA);

        if not cnf:
            return dict(tk.Entry.config(self, cnf),
                        text=("text", None, None, "", self._text),
                        text_fg=("text_fg", None, None, "#555555", self._text_fg),
                        text_bg=("text_bg", None, None, None, self._text_bg),
                        text_font=("text_font", None, None, None, self._text_font));

        tk.Entry.config(self, cnf);

        self._std_fg   = tk.Entry.cget(self, "fg");
        self._std_bg   = tk.Entry.cget(self, "bg");
        self._std_font = tk.Entry.cget(self, "font");
        self._std_show = tk.Entry.chet(self, "show");

        if "text" in extra and extra["text"] != self._text:
            if extra["text"]:
                self._enter_id = self.bind("<Enter>", self._enter, ADD);
                self._leave_id = self.bind("<Leave>", self._leave, ADD);
            else:
                self.unbind("", self._enter_id);
                self.unbind("", self._leave_id);
        
                if self._was_empty:
                    tk.Entry.delete(self, 0, END);
                    tk.Entry.config(self, fg=self._std_fg, bg=self._std_bg, font=self._std_font, show=self._std_show);

        
        self.__dict__.update({'_' + key: value for key, value in extra.items()});

        if self._text_bg is None:   self._text_bg   = self._std_bg;
        if self._text_font is None: self._text_font = self._std_font;
    config = configure;

    @wraps(tk.Entry.cget)
    def cget(self, key):
        if key in self._EXTRA:
            return getattr(self, '_' + key);
        else:
            return tk.Entry.cget(self, key);
    __getitem__ = cget;

    @wraps(tk.Entry.keys)
    def keys(self):
        return tk.Entry.keys() + self._EXTRA;

class InfoBox(tk.Toplevel):
    """
    Infobox widget to display information when hovering over a widget.
    """

    #_KEEP   = ();
    _EXTRA  = ("bd", "borderwidth", "relief", "bg", "background", "height", "width", "bitmap", "compound", "fg", "font", "foreground", "image", "justify", "text",
               "textvariable", "underline", "wraplength", "delay", "outside");
    _REMOVE = ("class", "menu", "screen", "use", "colormap", "container", "highlightbackground", "highlightcolor", "highlightthickness", "cursor", "takefocus", "visual",
               "padx", "pady");

    def __init__(self, master = None, cnf = {}, **kw):
        cnf, extra = filtercnf(cnf, kw, *self._EXTRA, delay=750, outside=False);
        checkcnf(cnf, self._REMOVE);

        self._delay = extra.pop("delay");
        self._outside = bool(extra.pop("outside"));

        self._shown   = True;
        self._entered = False;

        if self._outside:
            self._getWindowPosFromXY = self._getWindowPosFromXY_outside;
        else:
            self._getWindowPosFromXY = self._getWindowPosFromXY_moved;

        tk.Toplevel.__init__(self, master, cnf, takefocus=False);
        self.overrideredirect(True);
        self._label = tk.Label(self, extra);
        self._label.pack(fill=BOTH, expand=True);
        self.update();

        self._enter_id  = self.master.bind("<Enter>",  self._enter,  ADD);
        self._leave_id  = self.master.bind("<Leave>",  self._leave,  ADD);
        self._motion_id = self.master.bind("<Motion>", self._motion, ADD);

        self.hide();
    
    @m_event
    def _enter(self):
        self._entered = True;

    @m_event
    def _leave(self):
        self._entered = False;

        if self._shown:
            self.hide();

    @m_event
    def _motion(self):
        if self._entered:
            if not self._shown:
                self.after(self._delay, self._show, self.winfo_pointerxy());
            else:
                self.hide();

    def _show(self, xy: typing.Tuple[int, int]):
        if xy == self.winfo_pointerxy() and self._entered:
            self.show();

    def _getWindowPosFromXY_outside(self, x: int, y: int) -> typing.Tuple[int, int]:
        width, height = self.master.winfo_width(), self.master.winfo_height();

        if width < height:
            x = self.master.winfo_rootx();

            if x + width + self._width > self.winfo_screenwidth():
                x -= self._width;
            else:
                x += width;
        else:
            y = self.master.winfo_rooty();

            if y + height + self._height > self.winfo_screenheight():
                y -= self._height;
            else:
                y += height;
        
        return (x, y);
    def _getWindowPosFromXY_moved(self, x: int, y: int) -> typing.Tuple[int, int]:
        if x + 10 + self._width > self.winfo_screenwidth():
            x -= (self._width + 10);
        else:
            x += 10;
        
        if y + 10 + self._height > self.winfo_screenheight():
            y -= (self._height + 10);
        else:
            y += 10;
        
        return (x, y);

    def show(self, xy: typing.Tuple[int, int] = None):
        """
        Display Infobox on (current pointer) position.
        """
        
        if not self._shown and self._entered:
            self.state("normal")

            x, y = xy or self.winfo_pointerxy(); #xy if xy not None else winfo_pointerxy

            x, y = self._getWindowPosFromXY(x, y);

            self.geometry(f"+{x}+{y}");
            self.tkraise(self.master);
            self.update();

            self._shown = True;

    def hide(self):
        """
        Withdraw Infobox.
        """
        
        if self._shown:
            self.update();
            self._width, self._height = self.winfo_width(), self.winfo_height();

            self.state("withdrawn");

            self._shown = False;

    @wraps(tk.Toplevel.destroy)
    def destroy(self):
        self.master.unbind("", self._enter_id);
        self.master.unbind("", self._leave_id);
        self.master.unbind("", self._motion_id);

        tk.Toplevel.destroy(self);

    @wraps(tk.Toplevel.configure)
    def configure(self, cnf=None, **kw):
        cnf, extra = filtercnf(cnf, kw, *self._EXTRA, delay=750);

        if not cnf:
            config = {key: value for key, value in self._label.config().items() if key in self._EXTRA};
            config["delay"] = ("delay", None, None, 750, self._delay);

            return config;

        checkcnf(cnf, self._REMOVE);

        self._delay = extra.pop("delay", self._delay);

        tk.Toplevel.config(cnf);
        self._label.config(extra);
    config = configure;
    
    @wraps(tk.Toplevel.cget)
    def cget(self, key):
        if key == "delay": return self._delay;
        else: return self._label.cget(key);
    __getitem__ = cget;

    @wraps(tk.Toplevel.keys)
    def keys(self):
        return self._EXTRA;

#@wraps(tk.Entry)
class warnEntry(tk.Entry):
    _EXTRA = ("text", "text_fg", "text_bg", "text_font", "warn_color", "bell", "checkcommand", "checkdelay");
    _text: str;
    _text_fg: str;
    _text_bg: str;
    _text_font: typing.Union[str, tkfont.Font];
    _warn_color: str;
    _bell: bool;
    _checkcommand: typing.Callable;
    _checkdelay: int;

    @wraps(tk.Entry.__init__)
    def __init__(self, master = None, cnf = {}, **kw):
        cnf, extra = filtercnf(cnf, kw, text="", text_fg="#555555", text_bg=None, text_font=None, checkcommand=None, checkdelay=500, warn_color="red", bell=False);

        tk.Entry.__init__(self, master, cnf);
        self.__dict__.update({'_' + key: value for key, value in extra.items()});


        self.bind("<KeyRelease>", self._callback, ADD);

        self._last_keystroke = 0.0;


        self._std_fg   = tk.Entry.cget(self, "fg");
        self._std_bg   = tk.Entry.cget(self, "bg");
        self._std_font = tk.Entry.cget(self, "font");
        self._std_show = tk.Entry.cget(self, "show");

        self._was_empty = None;

        if self._text:
            self._enter_id = self.bind("<FocusIn>", self._enter, ADD);
            self._leave_id = self.bind("<FocusOut>", self._leave, ADD);

            self._leave();

        if self._text_bg is None:   self._text_bg   = self._std_bg;
        if self._text_font is None: self._text_font = self._std_font;


        self.bind("<Control-a>", self._highlight_all, ADD);
        self.bind("<Control-BackSpace>", self._delete_text, ADD);
        self.bind("<Control-Delete>", self._delete_text, ADD);
        self.bind("<Control-Shift-BackSpace>",
                  lambda event: self.delete(0, INSERT),
                  ADD);
        self.bind("<Control-Shift-Delete>",
                  lambda event: self.delete(INSERT, END),
                  ADD);
    
    @m_event
    def _highlight_all(self):
        self.selection_range(0, END);
        self.icursor(END);
        self.xview_moveto(1);

        return "break";

    def _delete_text(self, event: tk.Event):
        pos = initial_pos = self.index(INSERT);
        text = tk.Entry.get(self);

        if not text: return;

        if event.keysym == "Backspace": #<--
            if pos == self.index(END): pos -= 1; #Can not work with end index since it would raise IndexError in text string

            while pos > -1 and not (text[pos] == ' ' or text[pos] == '\n'):
                pos -= 1;
            
            tk.Entry.delete(self, pos + 1, initial_pos);
        elif event.keysym == "Delete": #Entf/Del
            end_pos = self.index(END);

            while pos < end_pos and not (text[pos] == ' ' or text[pos] == '\n'):
                pos += 1;
            
            tk.Entry.delete(self, initial_pos, pos);
    
    @m_event
    def _enter(self) -> None:
        if self._was_empty:
            tk.Entry.delete(self, 0, END);
            tk.Entry.config(self, fg=self._std_fg, bg=self._std_bg, font=self._std_font, show=self._std_show);

            self._was_empty = None; #to check if currently in use

    @m_event
    def _leave(self) -> None:
        text = tk.Entry.get(self);
        self._was_empty = (text == '');

        if self._was_empty:
            tk.Entry.insert(0, self._text);
            tk.Entry.config(self, fg=self._text_fg, bg=self._text_bg, font=self._text_font, sohw='');
        elif not self._checkcommand(text):
            self._warn();

    def _callback(self, event: tk.Event):
        self._last_keystroke = perf_counter();
        self.after(self._checkdelay, self._check, self._last_keystroke);

    def _check(self, time: float):
        print(time, self._last_keystroke, self._was_empty, not self._was_empty);

        if time == self._last_keystroke and not self._was_empty:
            if not self._checkcommand(tk.Entry.get(self)):
                self._warn();
    
    def _warn(self):
        normal_cnf = {"bg": tk.Entry.cget(self, "bg")};
        warn_cnf   = {"bg": self._warn_color};

        if self._bell: self.bell();

        tk.Entry.config(self, warn_cnf)
        self.after(100, tk.Entry.config, self, normal_cnf);
        self.after(200, tk.Entry.config, self, warn_cnf);
        self.after(300, tk.Entry.config, self, normal_cnf);
        self.after(400, tk.Entry.config, self, warn_cnf);
        self.after(500, tk.Entry.config, self, normal_cnf);

    @wraps(tk.Entry.get)
    def get(self):
        if self._was_empty:
            return '';
        else:
            return tk.Entry.get(self);

    @wraps(tk.Entry.insert)
    def insert(self, index, string):
        if not self._was_empty:
            tk.Entry.insert(self, index, string);

    @wraps(tk.Entry.delete)
    def delete(self, first, last):
        if not self._was_empty:
            tk.Entry.delete(self, first, last);

    @wraps(tk.Entry.configure)
    def configure(self, cnf = None, **kw):
        cnf, extra = filtercnf(cnf, kw, *self._EXTRA);

        if not cnf:
            return dict(tk.Entry.config(self, cnf),
                        text=("text", None, None, "", self._text),
                        text_fg=("text_fg", None, None, "#555555", self._text_fg),
                        text_bg=("text_bg", None, None, None, self._text_bg),
                        text_font=("text_font", None, None, None, self._text_font),
                        checkcommand=("checkcommand", None, None, None, self._checkcommand),
                        checkdelay=("checkdelay", None, None, 100, self._checkdelay),
                        warn_color=("warn_color", None, None, "red", self._warn_color),
                        bell=("bell", None, None, False, self._bell));

        tk.Entry.config(self, cnf);

        self._std_fg   = tk.Entry.cget(self, "fg");
        self._std_bg   = tk.Entry.cget(self, "bg");
        self._std_font = tk.Entry.cget(self, "font");
        self._std_show = tk.Entry.cget(self, "show");

        if "text" in extra and extra["text"] != self._text:
            if extra["text"]:
                self._enter_id = self.bind("<Enter>", self._enter, ADD);
                self._leave_id = self.bind("<Leave>", self._leave, ADD);
            else:
                self.unbind("", self._enter_id);
                self.unbind("", self._leave_id);
        
                if self._was_empty:
                    tk.Entry.delete(self, 0, END);
                    tk.Entry.config(self, fg=self._std_fg, bg=self._std_bg, font=self._std_font, show=self._std_show);

        
        self.__dict__.update({'_' + key: value for key, value in extra.items()});

        if self._text_bg is None:   self._text_bg   = self._std_bg;
        if self._text_font is None: self._text_font = self._std_font;
    config = configure;

    @wraps(tk.Entry.cget)
    def cget(self, key):
        if key in self._EXTRA:
            return getattr(self, '_' + key);
        else:
            return tk.Entry.cget(self, key);
    __getitem__ = cget;

    @wraps(tk.Entry.keys)
    def keys(self):
        return tk.Entry.keys() + self._EXTRA;

class SizeFrame(tk.Frame):
    PACK = 1;
    GRID = 2;
    PLACE = 3;

    def __init__(self, master: tk.Widget, height: int = 0, width: int = 0, geom: int = PACK,
                 geom_cnf: typing.Dict[str, typing.Any] = {}, **geom_kw: typing.Dict[str, typing.Any]):
        tk.Frame.__init__(self, master, height=height, width=width);

        if geom == self.PACK:
            self.pack_propagate(False);
            self.pack(geom_cnf, **geom_kw);
        elif geom == self.GRID:
            self.grid_propagate(False);
            self.grid(geom_cnf, **geom_kw);
        elif geom == self.PLACE:
            self.place(geom_cnf, **geom_kw);
        else:
            raise ValueError(f"Invalid geometry type '{geom}'. Must be SizeFrame.PACK, SizeFrame.GRID or SizeFrame.PLACE");

def _remap_wrapper(method: typing.Callable):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        return method(self._outer_frame, *args, **kwargs);
    
    return wrapper;

class Scrollframe(tk.Frame):
    """
    Scrollframe widget which may contain other widgets, can have a 3D border and allows to scroll through its content.
    """

    _OUTER = ("borderwidth", "bd", "container", "height", "width", "highlightthickness", "highlightcolor", "highlightbackground", "padx", "pady", "relief", "takefocus");
    _BOTH  = ("colormap", "visual", "background", "bg", "class", "cursor");
    _EXTRA = ("yscrollcommand", "xscrollcommand", "fill", "focus", "minwidth", "minheight", "reqwidth", "reqheight", "unit", "page", "segment");
    _REMAP_METHODS = ('destroy', 'focus_set', 'focus', 'focus_force', 'grab_status', 'lower', 'tkraise', 'lift', 'winfo_containing', 'winfo_depth', 'winfo_exists',
                      'winfo_fpixels', 'winfo_geometry', 'winfo_height', 'winfo_ismapped', 'winfo_manager', 'winfo_parent', 'winfo_pathname', 'winfo_pixels',
                      'winfo_reqheight', 'winfo_reqwidth', 'winfo_rootx', 'winfo_rooty', 'winfo_vrootheight', 'winfo_vrootwidth', 'winfo_vrootx', 'winfo_vrooty',
                      'winfo_width', 'winfo_x', 'winfo_y', 'update', 'update_idletasks', 'bindtags', 'bind', 'unbind', 'bind_all', 'unbind_all', 'bind_class',
                      'unbind_class', 'mainloop', 'quit', 'pack_configure', 'pack', 'pack_forget', 'forget', 'pack_info', 'info', 'place_configure', 'place',
                      'place_forget', 'place_info', 'grid_configure', 'grid', 'grid_forget', 'grid_remove', 'grid_info');

    locals().update({method_name: _remap_wrapper(getattr(tk.Frame, method_name)) for method_name in _REMAP_METHODS});

    _yscrollcommand: typing.Callable;
    _xscrollcommand: typing.Callable;
    _fill: str;
    _focus: str;
    _minwidth: int; #absolute -> if width < minwidth it gets reset no matter what fill says
    _minheight: int;
    _reqwidth: int; #negotiable -> if width != reqwidth it gets reset if this is consistent with fill
    _reqheight: int;
    _unit: typing.Union[int, float];
    _page: typing.Union[int, float];
    _segment: typing.Union[int, float];

    @wrapsAndExpand(tk.Frame.__init__, """
    
    Options added with scrolling feature

        yscrollcommand, xscrollcommand, fill,
        focus, minwidth, minheight, reqwidth,
        reqheight, unit, pade, segment
    """)
    def __init__(self, master = None, cnf= {}, **kw):
        cnf,   extra = filtercnf(cnf, kw, yscrollcommand=None, xscrollcommand=None, fill=X, focus=NW, minwidth=0, minheight=0,
                                 reqwidth=0, reqheight=0, unit=30, page=400, segment=0.5);
        cnf,   both  = filtercnf(cnf, None, *self._BOTH);
        inner, outer = filtercnf(cnf, None, *self._OUTER);

        inner.update(both);
        outer.update(both);

        req_width  = extra.pop("reqwidth");  #both definetly included so no error should ever be raised here
        if req_width  >= extra["minwidth"]:  inner["width"]  = req_width;
        else: raise ValueError("reqwidth can not be lower then minwidth!");
        req_height = extra.pop("reqheight");
        if req_height >= extra["minheight"]: inner["height"] = req_height;
        else: raise ValueError("reqheight can not be lower then minheight!");

        self._outer_frame = tk.Frame(master, outer);
        tk.Frame.__init__(self, self._outer_frame, inner);

        for key, value in extra: setattr(self, '_' + key, value);

        self._adopting = False;

        tk.Frame.bind(self, "<Configure>", self._update_outer, ADD);
        self._outer_frame.bind("<Configure>", self._update_outer, ADD);

        self._update_outer();

    def _update_inner(self):
        if not self._adopting:
            self._adopting = True

            tk.Frame.update(self);
            tk.Frame.update_idletasks(self);
            
            placeinfo = tk.Frame.place_info(self);
            inner_width, inner_height = tk.Frame.winfo_width(self), tk.Frame.winfo_height(self); #actual current width/height
            req_width,   req_height   = tk.Frame.winfo_reqwidth(self), tk.Frame.winfo_reqheight(self); #width/height as required by it's children or width/height parameters
            outer_width, outer_height = tk.Frame.winfo_width(self._outer_frame), tk.Frame.winfo_height(self._outer_frame);

            has_minwidth, has_minheight = (self._minwidth > 0), (self._minheight > 0);

            if self._fill == X or self._fill == BOTH:
                if has_minwidth and outer_width < self._minwidth: tk.Frame.place_configure(self, relwidth='', width=self._minwidth); #width=minwidth
                else: tk.Frame.place_configure(self, relwidth=1, width=''); #relwidth=1
            elif has_minwidth and req_width < self._minwidth:
                #if req_width >= self._minwidth: tk.Frame.place_configure(self, relwidth='', width='') #reset
                tk.Frame.place_configure(self, relwidth='', width=self._minwidth) #width=minwidth
            else:
                tk.Frame.place_configure(self, relwidth='', width='') #reset all

            if self._fill == Y or self._fill == BOTH:
                if has_minheight and outer_height < self._minheight: tk.Frame.place_configure(self, relheight='', height=self._minheight); #height=minheight
                else: tk.Frame.place_configure(self, relheight=1, height=''); #relheight=1
            elif has_minheight and req_height < self._minheight:
                #if req_height >= self._minheight: tk.Frame.place_configure(self, relheight='', height='') #reset
                tk.Frame.place_configure(self, relheight='', height=self._minheight) #height=minheight
            else:
                tk.Frame.place_configure(self, relheight='', height='') #reset all

            tk.Frame.update(self);
            tk.Frame.update_idletasks(self);

            self._adopting = False
    
    def _update_outer(self, event: tk.Event = None):
        if not self._adopting:
            self._adopting = True
            
            
            
            self._adopting = False

    def xview(self, mode = None, value = None, submode = None):
        pass

    def yview(self, mode = None, value = None, submode = None):
        pass

del _remap_wrapper; #not needed anymore at all since it was especially for Scrollframe but could not be a method