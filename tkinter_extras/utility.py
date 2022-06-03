import tkinter as tk
import typing

_add_as_methods = {}
def _add_as_method(name: str) -> typing.Callable:
    def decorator(func: typing.Callable):
        global _add_as_methods;

        if name in _add_as_methods:
            raise NameError(f"Name '{name}' already exists as custom method.");

        _add_as_methods[name] = func;

        return func;
    
    return decorator;

@_add_as_method("pointer_over")
def pointerOver(widget: tk.Widget, dx: int = 0, dy: int = 0, padx: typing.Union[int, typing.Tuple[int, int]] = 0, pady: typing.Union[int, typing.Tuple[int, int]] = 0) -> bool:
    """
    Wether or not pointer is over widget.
    
    @param widget: Element in question
    @param dx: horizontal pointer offset
    @param dy: vertical pointer offset
    @param padding: padding around the edges of the widget to be added
    """

    if isinstance(padx, int):
        left = right = padx;
    elif isinstance(padx, (tuple, list)) and len(padx) == 2:
        left, right = padx;
    else:
        raise TypeError(f"padx must be int or tuple of ints. Not '{type(padx)}'.");

    if isinstance(pady, int):
        top = bottom = pady;
    elif isinstance(pady, (tuple, list)) and len(pady) == 2:
        top, bottom = pady;
    else:
        raise TypeError(f"pady must be int or tuple of ints. Not '{type(pady)}'.");

    x, y = widget.winfo_rootx(), widget.winfo_rooty(); #widget coordinates

    return (x - left) <= (widget.winfo_pointerx() + dx) <= (x + widget.winfo_width()  + right) and \
           (y - top)  <= (widget.winfo_pointery() + dy) <= (y + widget.winfo_height() + bottom);

def parseGeom(geometry: str, as_bbox: bool = False) -> typing.Tuple[int, int, int, int]:
    """
    Parses tkinters geometry output into tuple.

    @param geometry: Geometry as returned by tk.Widget.geometry ("wxh+x+y")
    @param as_boox: Wether or not output should be shaped like a bbox (top left -> bottom right)
    """

    size, x, y = geometry.split("+");
    x, y = int(x), int(y);
    width, height = size.split("x");

    if as_bbox:
        return x - 1, y - 1, x + int(width) + 1, y + int(height) + 1;
    else:
        return int(width), int(height), x, y;

@_add_as_method("get_all_children")
def getAllChildren(widget: tk.Widget, stop_at: typing.Tuple[tk.Widget, ...] = (), stop_at_type: typing.Tuple[type, ...] = ()) -> typing.Tuple[tk.Widget, ...]:
    """
    Returns all children, childrens children, ... of the given widget.

    @param stop_at: tuple of widgets that shall not be further evaluated 
    @param stop_at_type: tuple of widget types that shall not be further evaluated 
    """

    widgets = list(widget.children.values());
    index = 0;

    while True:
        try:
            current = widgets[index];

            if isinstance(current, stop_at_type) or current in stop_at:
                pass
            else:
                widget += list(current.children.values());
        except IndexError:
            break;

        index += 1;

    return widgets;

@_add_as_method("master_history")
def masterHistory(widget: tk.Widget) -> typing.Tuple[tk.Widget, ...]:
    """
    Returns all lower masters of widget until Tk window.\nBegins with widget itself.
    """

    history = [widget];
    base_root = widget.root();
    previous = widget;

    while previous != base_root:
        previous = previous.master;
        history.append(previous);

    return history;

def plainbd(cnf: typing.Dict[str, typing.Any]) -> None:
    """
    Since bd and borderwidth mean the same plainbd picks one of both.
    Selection is made the way Tcl does it in normal widgets
    
    @param cnf: cnf to modify
    """

    for key in tuple(cnf.keys())[::-1]:
        if key == "bd":
            cnf.pop("borderwidth", None);
            break;
        elif key == "borderwidth":
            cnf["bd"] = cnf.pop("borderwidth");
            break;

def plainbg(cnf: typing.Dict[str, typing.Any]) -> None:
    """
    Since bg and background mean the same plainbg picks one of both.
    Selection is made the way Tcl does it in normal widgets
    
    @param cnf: cnf to modify
    """

    for key in tuple(cnf.keys())[::-1]:
        if key == "bg":
            cnf.pop("background", None);
            break;
        elif key == "background":
            cnf["bg"] = cnf.pop("background");
            break;

def plainfg(cnf: typing.Dict[str, typing.Any]) -> None:
    """Since fg and foreground mean the same plainfg picks one of both.
    Selection is made the way Tcl does it in normal widgets
    
    @param cnf: cnf to modify
    """

    for key in tuple(cnf.keys())[::-1]:
        if key == "fg":
            cnf.pop("foreground", None);
            break;
        elif key == "foreground":
            cnf["fg"] = cnf.pop("foreground");
            break;

def filtercnf(cnf: typing.Dict[str, typing.Any], kw: typing.Dict[str, typing.Any], *kwargs: typing.Tuple[str, ...], **stdkwargs: typing.Dict[str, typing.Any]) -> typing.Tuple[typing.Dict[str, typing.Any], typing.Dict[str, typing.Any]]:
    """
    Filters out arguments and assign standartarguments if not found in cnf or kw.
    If no kwarg and no stdkwarg is given it will just merge cnf and kw and return
    (<merged>, {}).

    @param cnf: configuration of a tkinters widget
    @param kw: extra configuration of a tkinters widget
    @param kwargs: arguments to get filtered out if in cnf-kw-merge (*optional)
    @param stdkwargs: arguments to get filtered out of cnf-kw-merge - if not found the argument will be used as standard (*optional)
    """

    if kw: cnf = tk._cnfmerge((cnf, kw));
    filtered = {};

    plainbg(cnf), plainbd(cnf), plainfg(cnf);

    for key in cnf.copy():
        if key in kwargs or key in stdkwargs:
            filtered[key] = cnf.pop(key);
    for key in stdkwargs:
        if key not in filtered:
            filtered[key] = stdkwargs[key];

    return cnf, filtered;

def checkcnf(cnf: typing.Dict[str, typing.Any], filter: typing.Tuple[str, ...]) -> bool:
    """
    Checks widget arguments for any unwanted arguments (filter).
    Returns False if unwanted argument was found, True else.
    """

    for element in filter:
        if element in cnf:
            #raise tk.TclError(f"unknown option '{element}'");
            break;
    else:
        return False;
    return True;

@_add_as_method("wait_event")
def waitEvent(widget: tk.Widget, event: str) -> None:
    """
    Blocks tkinter application until desired event occured.
    """

    validate = tk.BooleanVar(widget, False);
    bindID = widget.bind('<' + event + '>', lambda event: validate.set(True), True);

    widget.wait_variable(validate);

    widget.unbind(None, bindID);

@_add_as_method("winfo_exists")
def exists(widget: tk.Widget) -> bool:
    """
    Return true if this widget exists.

    Modified version of tkinter.Widget.winfo_exists()
    to return True or False but don't throw an error.
    """

    try: tk.Widget.winfo_exists(widget);
    except tk.TclError: return False;
    else: return True;

@_add_as_method("__contains__")
def contains(widget: tk.Widget, other: tk.Widget) -> bool:
    """
    Return wether or not the other is contained in widget.
    """

    last, baseroot = widget, widget._root();

    while other != last != baseroot:
        last = last.master;

    return last == other;

@_add_as_method("combine_with_alpha")
def alpha(widget: tk.Widget, fg: typing.Union[str, typing.Tuple[int, int, int]], bg: typing.Union[str, typing.Tuple[int, int, int]], a: float) -> typing.Tuple[int, int, int]:
    """
    Calculates the seen color when fg lays over bg with an alpha value of a.

    @param fg: foreground color
    @param bg: background color
    @param a: alpha value of fg
    """

    if isinstance(fg, str):
        fg_r, fg_g, fg_b = widget.winfo_rgb(fg);
    else:
        fg_r, fg_g, fg_b = fg;
    if isinstance(bg, str):
        bg_r, bg_g, bg_b = widget.winfo_rgb(bg);
    else:
        bg_r, bg_g, bg_b = bg;

    return (a * fg_r + (1 - a) * bg_r, a * fg_g + (1 - a) * bg_g, a * fg_b + (1 - a) * bg_b);

def RGBtoTkRGB(rgb: typing.Tuple[int, int, int]) -> str:
    """
    Convert an RGB tuple into tkinters #rrggbb format.
    """
    
    return "#%02x%02x%02x" % tuple(rgb);