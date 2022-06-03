#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import _cnfmerge as cnfmerge, ttk, font
from tkinter import *
from numpy import array
from math import cos,sin,pi,acos,radians as rad
from threading import Thread
import sys
import time
from datetime import datetime
from functools import wraps
from pynput.mouse import Controller, Button as ButtonType
from inspect import signature

_std_tkinter_widgets=[Tk,Toplevel,Frame,Button,Canvas,Checkbutton,Message,Menu,Menubutton,Radiobutton,Scrollbar,Text,Spinbox,LabelFrame,PanedWindow,Entry,Label,Listbox]

TkinterColors = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace', 'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
                 'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender', 'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
                 'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue', 'slate blue', 'medium slate blue', 'light slate blue',
                 'medium blue', 'royal blue',  'blue', 'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue', 'light blue', 'powder blue',
                 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise', 'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
                 'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green', 'lawn green', 'medium spring green', 'green yellow', 'lime green',
                 'yellow green', 'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow', 'light yellow', 'yellow', 'gold', 'light goldenrod',
                 'goldenrod', 'dark goldenrod', 'rosy brown', 'indian red', 'saddle brown', 'sandy brown', 'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange', 'coral',
                 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink', 'pale violet red', 'maroon', 'medium violet red', 'violet red', 'medium orchid',
                 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple', 'thistle', 'snow2', 'snow3', 'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1',
                 'AntiqueWhite2', 'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2', 'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
                 'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3', 'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4', 'LavenderBlush2',
                 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3', 'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3', 'SlateBlue4',
                 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4', 'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2', 'SteelBlue3', 'SteelBlue4',
                 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4', 'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2', 'LightSkyBlue3', 'LightSkyBlue4',
                 'SlateGray1', 'SlateGray2', 'SlateGray3', 'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3', 'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3',
                 'LightBlue4', 'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2', 'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
                 'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3', 'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
                 'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3', 'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
                 'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4', 'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4', 'OliveDrab1',
                 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2', 'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4', 'LightGoldenrod1',
                 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4', 'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4', 'gold2', 'gold3', 'gold4',
                 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4', 'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4', 'RosyBrown1', 'RosyBrown2', 'RosyBrown3',
                 'RosyBrown4', 'IndianRed1', 'IndianRed2', 'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1', 'burlywood2', 'burlywood3', 'burlywood4',
                 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1', 'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', 'brown1',
                 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2', 'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2', 'orange3', 'orange4', 'DarkOrange1',
                 'DarkOrange2', 'DarkOrange3', 'DarkOrange4', 'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2', 'OrangeRed3', 'OrangeRed4', 'red2', 'red3',
                 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4', 'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4', 'LightPink1', 'LightPink2', 'LightPink3',
                 'LightPink4', 'PaleVioletRed1', 'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2', 'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3',
                 'VioletRed4', 'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1', 'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2',
                 'MediumOrchid3', 'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4', 'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
                 'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4', 'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
                 'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19', 'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27',
                 'gray28', 'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37', 'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45',
                 'gray46', 'gray47', 'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56', 'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62',
                 'gray63', 'gray64', 'gray65', 'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74', 'gray75', 'gray76', 'gray77', 'gray78', 'gray79',
                 'gray80', 'gray81', 'gray82', 'gray83', 'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92', 'gray93', 'gray94', 'gray95', 'gray97',
                 'gray98', 'gray99']
SystemColors = ['SystemActiveBorder', 'SystemActiveCaption', 'SystemAppWorkspace', 'SystemBackground', 'SystemButtonFace', 'SystemButtonHighlight', 'SystemButtonShadow', 'SystemButtonText',
                'SystemCaptionText', 'SystemDisabledText', 'SystemHighlight', 'SystemHighlightText', 'SystemInactiveBorder', 'SystemInactiveCaption', 'SystemInactiveCaptionText', 'SystemMenu',
                'SystemMenuText', 'SystemScrollbar', 'SystemWindow', 'SystemWindowFrame', 'SystemWindowText']

ADD,PIXEL,READONLY='+','pixel','readonly'
READ, WRITE, UNSET = 'read', 'write', 'unset'
WINDOW, AUTO = 'window', 'auto'

_tk = Tk()
_style = ttk.Style()
_style.configure("texted.TEntry", foreground='#555555')
#more?
del _style
_tk.destroy()
del _tk

def empty(*args,**kwargs):
    'Does nothing.'
    pass

def createdict(**kwargs):
    'Creates a dict without the need of typing \' or ".'
    return kwargs

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global indent
        indent += 4
        print('\n' + ' ' * indent, 'START', func.__name__, 'with:', args[1:], kwargs)
        ret = func(*args, **kwargs)
        print(' ' * indent, 'STOP', func.__name__, 'with:', ret, end='\n'*2)
        indent -= 4
        return ret
    return wrapper

def pointer_over(root,dx=0,dy=0,left=0,right=0,top=0,bottom=0):
    '''Returns if the pointer is in given area.'''
    x,y=root.winfo_rootx(),root.winfo_rooty()
    return x-left<=root.winfo_pointerx()-dx<=x+root.winfo_width()+right and y-top<=root.winfo_pointery()-dy<=y+root.winfo_height()+bottom

def event(func):
    @wraps(func)
    def event_wrapper(self, event=None): return func(self)
    return event_wrapper

def exclude(*args: str):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs): return function(*args, **kwargs)
        sig = signature(function)
        wrapper.__signature__ = sig.replace(parameters=(parameter for key, parameter in sig.parameters.items() if key not in args))
        return wrapper
    return decorator

@exclude('arg')
def merge(arg, *args: str, start='(', sep=', ', end=')'): #technically just an example how exclude can help with estatics -> str.join has nearly the same functionality
    text = start + str(arg)
    for arg in args: text += sep + arg
    return text + end

def parsegeom(geometry,bbox=False):
    'Parses tkinters geometry output into x,y,width,height or an x0,y0,x1,y1 bbox.'
    size,x,y=geometry.split('+')
    x,y=int(x),int(y)
    width,height=map(int,size.split('x'))
    if bbox: return x,y,x+width,y+height
    else: return x,y,width,height

def getallchildren(widget):
    'Returns all children, childrens children, ... of the given Widget.'
    lst,i=list(widget.children.values()),0
    while True:
        try:
            now=lst[i]
            if isinstance(now,(Display,Scrollframe,Table,Comparetable,Displaybutton,InfoBox,WarnEntry,RotaryButton,CustomButton,CustomScrollbar)): pass
            elif isinstance(now,hvFrame): lst+=list(now.mf.children.values())
            else: lst+=list(now.children.values())
        except IndexError: break
        i+=1
    return lst

def _getallchildren(widget):
    '''Returns all (in this function really ALL) children, childrens children, ... of the given Widget.
    If possible use getallchildren since this function ignores wether or not something is a multiwidget or not'''
    lst,i=list(widget.children.values()),0
    while True:
        try: lst+=list(lst[i].children.values())
        except IndexError: break
        i+=1
    return lst

def masterhistory(widget):
    '''Returns all lower masters of widget until Tk window.\nBegins with widget itself.'''
    history, master = [widget], widget._root()
    while history[-1] != master: history.append(history[-1].master)
    return history

def plainbd(cnf):
    '''Since bd and borderwidth mean the same plainbg picks one of both.
    Selection is made the way Tcl does it in normal widgets
    
    @param cnf: cnf from which to pick
    @type cnf: dict'''
    for key in tuple(cnf.keys())[::-1]:
        if key=='bd':
            cnf.pop('borderwidth',None)
            break
        elif key=='borderwidth':
            cnf['bd']=cnf.pop('borderwidth')
            break

def plainbg(cnf):
    '''Since bg and background mean the same plainbg picks one of both.
    Selection is made the way Tcl does it in normal widgets
    
    @param cnf: cnf from which to pick
    @type cnf: dict'''
    for key in tuple(cnf.keys())[::-1]:
        if key=='bg':
            cnf.pop('background',None)
            break
        elif key=='background':
            cnf['bg']=cnf.pop('background')
            break

def plainfg(cnf):
    '''Since fg and foreground mean the same plainbg picks one of both.
    Selection is made the way Tcl does it in normal widgets
    
    @param cnf: cnf from which to pick
    @type cnf: dict'''
    for key in tuple(cnf.keys())[::-1]:
        if key=='fg':
            cnf.pop('foreground',None)
            break
        elif key=='foreground':
            cnf['fg']=cnf.pop('foreground')
            break

def filtercnf(cnf,kw,*kwargs,**stdkwargs):
    '''Filters out arguments and assign standartarguments if not found in cnf or kw.
    If no kwarg and no stdkwarg is given it will just merge cnf and kw and return
    (<cnf>,{}).

    @param cnf: configuration of a tkinters widget
    @type cnf: dict
    @param kw: extra configuration of a tkinters widget
    @type kw: dict
    @param kwargs: arguments to get filtered out if in cnf-kw-merge (*optional)
    @type kwargs: tuple (of strings)
    @param stdkwargs: arguments to get filtered out of cnf-kw-merge - if not found the argument will be used as standard (*optional)
    @type stdkwargs: dict (of strings:all)

    @return: cleaned cnf and kwargs that got filtered out
    @rtype: tuple (of 2 dicts)
    '''
    if kw: cnf=cnfmerge((cnf,kw))
    filtered={}
    plainbg(cnf),plainbd(cnf),plainfg(cnf)
    for key in cnf.copy():
        if key in kwargs or key in stdkwargs: filtered[key]=cnf.pop(key)
    for key in stdkwargs:
        if key not in filtered: filtered[key]=stdkwargs[key]
    return cnf,filtered

def checkcnf(cnf, filter):
    for element in filter:
        if element in cnf: raise TclError('unknown option "-%s"'%element)

def wait_event(self, event):
    validate = StringVar(self, '')
    bindID = self.bind('<' + event + '>', self.validate.set, True)
    self.wait_variable(validate)
    self.unbind(None, bindID)

def exists(self):
    '''Return true if this widget exists.

    modified version of Widget.winfo_exists()
    -> return True/False but no error'''
    try: Widget.winfo_exists(self)
    except TclError: return False
    else: return True

def contains(self, widget):
    '''Return wether or not the given widget is contained in self.'''
    last, baseroot = widget, widget._root()
    while self != last != baseroot: last = last.master
    return last == self

for widget in _std_tkinter_widgets:
    setattr(widget, 'winfo_exists', exists)
    setattr(widget, '__contains__', contains)
    setattr(widget, 'wait_event', wait_event)

class Callback:
    def __init__(self,callback,args=(),kwargs={},addargs=False,addkwargs=False): self._cb,self._a,self._kwa,self._aa,self._akw=callback,args,kwargs,addargs,addkwargs
    def __call__(self,*args,**kwargs):
        if self._akw: self._kw.update(kwargs)
        if self._aa: return self._cb(*self._a,*args,**self._kwa)
        else: return self._cb(*self._a,**self._kwa)

_tkspinbox=Spinbox
class Spinbox(_tkspinbox):
    'spinbox widget.'
    def __init__(self,master=None,cnf={},**kw):
        'Construct a spinbox widget with the parent MASTER.\n\n        STANDARD OPTIONS\n\n            activebackground, background, borderwidth,\n            cursor, exportselection, font, foreground,\n            highlightbackground, highlightcolor,\n            highlightthickness, insertbackground,\n            insertborderwidth, insertofftime,\n            insertontime, insertwidth, justify, relief,\n            repeatdelay, repeatinterval,\n            selectbackground, selectborderwidth\n            selectforeground, takefocus, textvariable\n            xscrollcommand.\n\n        WIDGET-SPECIFIC OPTIONS\n\n            buttonbackground, buttoncursor,\n            buttondownrelief, buttonuprelief,\n            command, disabledbackground,\n            disabledforeground, format, from,\n            invalidcommand, increment,\n            readonlybackground, state, to,\n            validate, validatecommand values,\n            width, wrap,\n        '
        cnf=cnfmerge((cnf,kw))
        if 'scroll' in cnf: self._scroll=cnf.pop('scroll')
        else: self._scroll=False
        _tkspinbox.__init__(self,master,cnf)
        self.bind('<MouseWheel>',self._scrollcmd,'+')
    def _scrollcmd(self,event):
        if self._scroll:
            if event.delta>0:
                for i in range(int(abs(event.delta/120))): self.invoke('buttonup')
            else:
                for i in range(int(abs(event.delta/120))): self.invoke('buttondown')

class dText(Text):
    'Text widget which can display text in various forms.'
    def __init__(self,master=None,cnf={},**kw):
        'Construct a text widget with the parent MASTER.\n\n        STANDARD OPTIONS\n\n            background, borderwidth, cursor,\n            exportselection, font, foreground,\n            highlightbackground, highlightcolor,\n            highlightthickness, insertbackground,\n            insertborderwidth, insertofftime,\n            insertontime, insertwidth, padx, pady,\n            relief, selectbackground,\n            selectborderwidth, selectforeground,\n            setgrid, takefocus,\n            xscrollcommand, yscrollcommand,\n\n        WIDGET-SPECIFIC OPTIONS\n\n            autoseparators, height, maxundo,\n            spacing1, spacing2, spacing3,\n            state, tabs, undo, width, wrap,\n\n        '
        Text.__init__(self,master,cnf,**kw)
        self.bind('<Control-BackSpace>',lambda event: self.delete(self.index(INSERT+' -1 char wordstart'),INSERT),ADD)
        self.bind('<Control-Delete>',lambda event: self.delete(INSERT,self.index(INSERT+' +1 char wordend')),ADD)
        self.bind('<Control-Alt-BackSpace>',lambda event: self.delete(self.index(INSERT+' linestart'),INSERT),ADD)
        self.bind('<Control-Alt-Delete>',lambda event: self.delete(INSERT,self.index(self.index(INSERT)+' lineend')),ADD)
        self.bind('<Control-Shift-Alt-BackSpace>',lambda event: self.delete(0.0,INSERT),ADD)
        self.bind('<Control-Shift-Alt-Delete>',lambda event: self.delete(INSERT,END),ADD)

class hText(Text):
    'Text widget which can display text in various forms.'
    def __init__(self,master=None,cnf={},**kw):
        'Construct a text widget with the parent MASTER.\n\n        STANDARD OPTIONS\n\n            background, borderwidth, cursor,\n            exportselection, font, foreground,\n            highlightbackground, highlightcolor,\n            highlightthickness, insertbackground,\n            insertborderwidth, insertofftime,\n            insertontime, insertwidth, padx, pady,\n            relief, selectbackground,\n            selectborderwidth, selectforeground,\n            setgrid, takefocus,\n            xscrollcommand, yscrollcommand,\n\n        WIDGET-SPECIFIC OPTIONS\n\n            autoseparators, height, maxundo,\n            spacing1, spacing2, spacing3,\n            state, tabs, undo, width, wrap,\n\n        '
        Text.__init__(self,master,cnf,**kw)
        self.master.bind('<Key>',self._keyhandler,ADD)
        self._text=''
    def _keyhandler(self,event): #\x7f \x08
        'Intern function'
        if event.char=='\x08':
            self._text=self._text[:-1]
            self.delete(0.0,END)
            text=''
            for i in self._text.split('\r'): text+='*'*len(i)+'\n'
            self.insert(0.0,text[:-1])
        elif event.char=='\x7f':
            self._text=''
            self.delete(0.0,END)
        else:
            self._text+=event.char
            self.delete(0.0,END)
            text=''
            for i in self._text.split('\r'): text+='*'*len(i)+'\n'
            self.insert(0.0,text[:-1])
    def get(self):
        'Return the original typed text.'
        return self._text

class tText(Text):
    'Text widget which can display text in various forms.'
    def __init__(self,master=None,cnf={},**kw):
        'Construct a text widget with the parent MASTER.\n\n        STANDARD OPTIONS\n\n            background, borderwidth, cursor,\n            exportselection, font, foreground,\n            highlightbackground, highlightcolor,\n            highlightthickness, insertbackground,\n            insertborderwidth, insertofftime,\n            insertontime, insertwidth, padx, pady,\n            relief, selectbackground,\n            selectborderwidth, selectforeground,\n            setgrid, takefocus,\n            xscrollcommand, yscrollcommand,\n\n        WIDGET-SPECIFIC OPTIONS\n\n            autoseparators, height, maxundo,\n            spacing1, spacing2, spacing3,\n            state, tabs, undo, width, wrap,\n\n        '
        if 'text' in kw:
            self._text=kw['text']
            del kw['text']
        elif 'text' in cnf:
            self._text=cnf['text']
            del cnf['text']
        else: self._text=''
        Text.__init__(self,master,cnf,**kw)
        self._written,self._standard_fg=False,self.cget('fg')
        self.bind('<FocusIn>',self._delete,ADD)
        self.bind('<FocusOut>',self._set,ADD)
        self._set()
    def _set(self,event=None):
        'Intern function'
        if super().get(0.0,END)=='\n':
            self._written=False
            self.config(fg='#555555')
            self.delete(0.0,END)
            self.insert(0.0,self._text)
        else: self._written=True
    def _delete(self,event=None):
        'Intern function'
        if not self._written:
            self.config(fg='SystemWindowText')
            self.delete(0.0,END)
    def get(self):
        'Return the original typed text.'
        if self._written: return super().get(0.0,END)
        else: return ''

class dtText(dText):
    'Text widget which can display text in various forms.'
    def __init__(self,master=None,cnf={},**kw):
        'Construct a text widget with the parent MASTER.\n\n        STANDARD OPTIONS\n\n            background, borderwidth, cursor,\n            exportselection, font, foreground,\n            highlightbackground, highlightcolor,\n            highlightthickness, insertbackground,\n            insertborderwidth, insertofftime,\n            insertontime, insertwidth, padx, pady,\n            relief, selectbackground,\n            selectborderwidth, selectforeground,\n            setgrid, takefocus,\n            xscrollcommand, yscrollcommand,\n\n        WIDGET-SPECIFIC OPTIONS\n\n            autoseparators, height, maxundo,\n            spacing1, spacing2, spacing3,\n            state, tabs, undo, width, wrap,\n\n        '
        if 'text' in kw:
            self._text=kw['text']
            del kw['text']
        elif 'text' in cnf:
            self._text=cnf['text']
            del cnf['text']
        else: self._text=''
        dText.__init__(self,master,cnf,**kw)
        self._written,self._standard_fg=False,self.cget('fg')
        self.bind('<FocusIn>',self._delete,ADD)
        self.bind('<FocusOut>',self._set,ADD)
        self._set()
    def _set(self,event=None):
        'Intern function'
        if super().get(0.0,END)=='\n':
            self._written=False
            self.config(fg='#555555')
            self.delete(0.0,END)
            self.insert(0.0,self._text)
        else: self._written=True
    def _delete(self,event=None):
        'Intern function'
        if not self._written:
            self.config(fg=self._standard_fg)
            self.delete(0.0,END)
    def get(self):
        'Return the original typed text.'
        if self._written: return super().get(0.0,END)
        else: return ''

class dEntry(Entry):
    'Entry widget which allows displaying simple text.'
    def __init__(self,master=None,cnf={},**kw):
        'Construct a text widget with the parent MASTER.\n\n        STANDARD OPTIONS\n\n            background, borderwidth, cursor,\n            exportselection, font, foreground,\n            highlightbackground, highlightcolor,\n            highlightthickness, insertbackground,\n            insertborderwidth, insertofftime,\n            insertontime, insertwidth, padx, pady,\n            relief, selectbackground,\n            selectborderwidth, selectforeground,\n            setgrid, takefocus,\n            xscrollcommand, yscrollcommand,\n\n        WIDGET-SPECIFIC OPTIONS\n\n            autoseparators, height, maxundo,\n            spacing1, spacing2, spacing3,\n            state, tabs, undo, width, wrap,\n\n        '
        ttk.Entry.__init__(self,master,cnf,**kw)
        self.bind('<Control-BackSpace>',self._del,ADD)
        self.bind('<Control-Delete>',self._del,ADD)
        self.bind('<Control-Alt-BackSpace>',lambda event: self.delete(0,INSERT),ADD)
        self.bind('<Control-Alt-Delete>',lambda event: self.delete(INSERT,END),ADD)
    def _del(self,event):
        'Intern function'
        pos,text=self.index(INSERT),self.get()
        if pos==0: pos=1
        while text!='' and text[pos-1] not in [' ','\n']:
            if event.keysym=='BackSpace' and pos==1:
                pos=0
                break
            elif event.keysym=='BackSpace': pos-=1
            elif event.keysym=='Delete' and pos==len(text):
                pos=END
                break
            else: pos+=1
        if event.keysym=='BackSpace': self.delete(pos+1,self.index(INSERT))
        else: self.delete(self.index(INSERT),pos-2 if pos!=END else pos)

class hEntry(Entry): #useless
    'Entry widget which allows displaying simple text.'
    def __init__(self,master=None,cnf={},**kw):
        'Construct a text widget with the parent MASTER.\n\n        STANDARD OPTIONS\n\n            background, borderwidth, cursor,\n            exportselection, font, foreground,\n            highlightbackground, highlightcolor,\n            highlightthickness, insertbackground,\n            insertborderwidth, insertofftime,\n            insertontime, insertwidth, padx, pady,\n            relief, selectbackground,\n            selectborderwidth, selectforeground,\n            setgrid, takefocus,\n            xscrollcommand, yscrollcommand,\n\n        WIDGET-SPECIFIC OPTIONS\n\n            autoseparators, height, maxundo,\n            spacing1, spacing2, spacing3,\n            state, tabs, undo, width, wrap,\n\n        '
        Entry.__init__(self,master,cnf,**kw)
        self.bind('<Key>',self._keyhandler)
        self.bind('<Delete>',self._del)
        self.bind('<BackSpace>',self._del)
        self.bind('<Control-Delete>',self._cdel)
        self.bind('<Control-BackSpace>',self._cdel)
        self._text=''
    def _keyhandler(self,event):
        'Intern function'
        if event.char!='' and event.char!='\r':
            self._text+=event.char
            self.delete(0,END)
            self.insert(0,'*'*len(self._text))
        return 'break'
    def _del(self,event):
        'Intern function'
        if event.keysym=='BackSpace' and self.index(INSERT)!=0:
            text=list(self._text)
            del text[self.index(INSERT)-1]
            self._text=''.join(text)
            self.delete(0)
        elif event.keysym=='Delete' and self.index(INSERT)!=len(self._text):
            text=list(self._text)
            del text[self.index(INSERT)]
            self._text=''.join(text)
            self.delete(0)
        return 'break'
    def _cdel(self,event):
        'Intern function'
        if event.keysym=='BackSpace' and self.index(INSERT)!=0:
            self._text=self._text[self.index(INSERT):]
            self.delete(0,self.index(INSERT))
        elif event.keysym=='Delete' and self.index(INSERT)!=len(self._text):
            self._text=self._text[:self.index(INSERT)]
            self.delete(self.index(INSERT),END)
        return 'break'
    def get(self):
        'Return the originally typed text.'
        return self._text

class tEntry(Entry):
    'Entry widget which can display text in various forms.'
    def __init__(self,master=None,cnf={},**kw):
        'Construct a text widget with the parent MASTER.\n\n        STANDARD OPTIONS\n\n            background, borderwidth, cursor,\n            exportselection, font, foreground,\n            highlightbackground, highlightcolor,\n            highlightthickness, insertbackground,\n            insertborderwidth, insertofftime,\n            insertontime, insertwidth, padx, pady,\n            relief, selectbackground,\n            selectborderwidth, selectforeground,\n            setgrid, takefocus,\n            xscrollcommand, yscrollcommand,\n\n        WIDGET-SPECIFIC OPTIONS\n\n            autoseparators, height, maxundo,\n            spacing1, spacing2, spacing3,\n            state, tabs, undo, width, wrap,\n\n        '
        if 'text' in kw:
            self._text=kw['text']
            del kw['text']
        elif 'text' in cnf:
            self._text=cnf['text']
            del cnf['text']
        else: self._text=''
        Entry.__init__(self,master,cnf,**kw)
        self._written,self._standard_fg=False,self.cget('fg')
        self.bind('<FocusIn>',self._delete,ADD)
        self.bind('<FocusOut>',self._set,ADD)
        self._set()
    def _set(self,event=None):
        'Intern function'
        if super().get()=='':
            self._written=False
            self.config(fg='#555555')
            self.delete(0,END)
            self.insert(0,self._text)
        else: self._written=True
    def _delete(self,event=None):
        'Intern function'
        if not self._written:
            self.config(fg='SystemWindowText')
            self.delete(0,END)
    def get(self):
        'Return the original typed text.'
        if self._written: return super().get()
        else: return ''

class dtEntry(Entry):
    'Entry widget which allows displaying simple text.'
    def __init__(self,master=None,cnf={},**kw):
        'Construct a text widget with the parent MASTER.\n\n        STANDARD OPTIONS\n\n            background, borderwidth, cursor,\n            exportselection, font, foreground,\n            highlightbackground, highlightcolor,\n            highlightthickness, insertbackground,\n            insertborderwidth, insertofftime,\n            insertontime, insertwidth, padx, pady,\n            relief, selectbackground,\n            selectborderwidth, selectforeground,\n            setgrid, takefocus,\n            xscrollcommand, yscrollcommand,\n\n        WIDGET-SPECIFIC OPTIONS\n\n            autoseparators, height, maxundo,\n            spacing1, spacing2, spacing3,\n            state, tabs, undo, width, wrap,\n\n        '
        cnf,dictupdate=filtercnf(cnf,kw,text='',color='#555555')
        Entry.__init__(self,master,cnf)
        self.fg=super().cget('fg')
        self.__dict__.update(dictupdate)
        self.display=True
        self.bind('<FocusIn>',self.focusin,ADD)
        self.bind('<FocusOut>',self.focusout,ADD)
        super().config(fg=self.color)
        self.insert(0,self.text)
    def focusin(self,event):
        if self.display:
            super().config(fg=self.fg)
            self.delete(0,END)
        self.display=False
    def focusout(self,event):
        if super().get()=='':
            self.display=True
            super().config(fg=self.color)
            self.insert(0,self.text)
    def config(self,cnf=None,**kw):
        cnf,dictupdate=filtercnf(cnf,kw,'color','text')
        self.__dict__.update(dictupdate)
        super().config(cnf)
        self.fg=super().cget('fg')
        if self.display:
            super().config(fg=self.color)
            self.delete(0,END)
            self.insert(0,self.text)
    def cget(self,key):
        if key in ('color','text'): return getattr(self,key)
        else: super().cget(key)
    def keys(self): return super().keys()+['text','color']
    def get(self):
        'Return the original typed text.'
        if not self.display: return super().get()
        else: return ''

class dtttkEntry(ttk.Entry):
    'Entry widget which allows displaying simple text.'
    def __init__(self,master=None,cnf={},**kw):
        'Construct a text widget with the parent MASTER.\n\n        STANDARD OPTIONS\n\n            background, borderwidth, cursor,\n            exportselection, font, foreground,\n            highlightbackground, highlightcolor,\n            highlightthickness, insertbackground,\n            insertborderwidth, insertofftime,\n            insertontime, insertwidth, padx, pady,\n            relief, selectbackground,\n            selectborderwidth, selectforeground,\n            setgrid, takefocus,\n            xscrollcommand, yscrollcommand,\n\n        WIDGET-SPECIFIC OPTIONS\n\n            autoseparators, height, maxundo,\n            spacing1, spacing2, spacing3,\n            state, tabs, undo, width, wrap,\n\n        '
        cnf,dictupdate=filtercnf(cnf,kw,text='',color='#555555')
        ttk.Entry.__init__(self,master,cnf)
        self._style = ttk.Style()
        self.fg=super().cget('fg')
        self.__dict__.update(dictupdate)
        self.display=True
        self.bind('<FocusIn>',self.focusin,ADD)
        self.bind('<FocusOut>',self.focusout,ADD)
        super().config(fg=self.color)
        self.insert(0,self.text)
    def focusin(self,event):
        if self.display:
            super().config(fg=self.fg)
            self.delete(0,END)
        self.display=False
    def focusout(self,event):
        if super().get()=='':
            self.display=True
            super().config(fg=self.color)
            self.insert(0,self.text)
    def config(self,cnf=None,**kw):
        cnf,dictupdate=filtercnf(cnf,kw,'color','text')
        self.__dict__.update(dictupdate)
        super().config(cnf)
        self.fg=super().cget('fg')
        if self.display:
            super().config(fg=self.color)
            self.delete(0,END)
            self.insert(0,self.text)
    def cget(self,key):
        if key in ('color','text'): return getattr(self,key)
        else: super().cget(key)
    def keys(self): return super().keys()+['text','color']
    def get(self):
        'Return the original typed text.'
        if not self.display: return super().get()
        else: return ''

class PosObj(dict):
    def __init__(self,x,y):
        dict.__init__(self)
        self['x'],self['y']=x,y
        self.__str__=self.__repr__
    def __repr__(self):
        return '(x: %s,y: %s)' % (self['x'],self['y'])

class CustomWidget:
    def __init__(self,master=None,cnf={},**kw):
        self._master,self._cnf,self._kw=master if master!=None else Tk(),cnf,kw
        self._list=[]
        self._pos={}
    class _ObjectList(list):
        def __init__(self,*objs):
            list.__init__(self,objs)
        def __repr__(self):
            return 'ObjectList(%s)' % list(self)
        def __str__(self):
            ret=''
            for i in range(len(self)): ret+='\n%s   %s' % (i,self[i])
            ret=ret[1:]
            return ret
    def addObj(self,widget,position,cnf={},**kw):
        self._list.append([Frame(self._master,cnf=cnfmerge(cnf,self._cnf),**cnfmerge(kw,self._kw)),position])
        if self._pos!={}: self._list[len(self._list)-1][0].place(x=self._pos['x']+position['x'],y=self._pos['y']+position['y'])
        return len(self._list)-1
    def getObjs(self): return self._ObjectList(*[pos for widget,pos in self._list])
    def configObj(self,pos): return self._list[pos][0]
    def delObj(self,pos):
        if pos==END: pos=len(self._list)-1
        self._list[pos][0].destroy()
        del self._list[pos]
        return self._ObjectList(*[pos for widget,pos in self._list])
    def place(self,**pos):
        if self._pos=={}: self._pos={'x':0,'y':0}
        if 'x' not in pos: pos['x']=self._pos['x']
        if 'y' not in pos: pos['y']=self._pos['y']
        self._pos=pos
        for i in self._list: i[0].place(x=pos['x']+i[1]['x'],y=pos['y']+i[1]['y'])
    def place_info(self): return self._pos

class Display(Frame):
    'Display to show x and y coordinates.'
    def __init__(self,master=None,height=None,width=None,bg='SystemButtonFace',fg='SystemButtonText',bd=0,relief=FLAT):
        relLabel=Label(text='Position: ')
        Frame.__init__(self,master,height=height if height!=None else relLabel.winfo_reqheight(),width=width if width!=None else relLabel.winfo_reqwidth()*7//3,bd=bd,relief=relief,bg=bg)
        self.text=Label(self,text='Position:',anchor=W,bg=bg,fg=fg)
        self.text.place(relheight=1.0,relwidth=3/7,x=0,y=0)
        self.x=Label(self,text='',bg='SystemWindow',bd=1,relief=SUNKEN)
        self.x.place(relheight=1.0,relwidth=2/7,relx=3/7,rely=0.0)
        self.y=Label(self,text='',bg='SystemWindow',bd=1,relief=SUNKEN)
        self.y.place(relheight=1.0,relwidth=2/7,relx=3/7+2/7,rely=0.0)
        self.config=self.configure
    def keys(self):
        'Return a list of all resource names of this widget.'
        return ['height','width','bg','fg','bd','relief']
    def end(self):
        'Resets display.'
        self.configxy()
    def configxy(self,x=None,y=None):
        'Refreshes x and y values.'
        self.x.config(text=str(x) if x!=None else '')
        self.y.config(text=str(y) if y!=None else '')
    def configure(self,cnf=None,**kw):
        'Configure resources of a widget.\n\n        The values for resources are specified as keyword\n        arguments. To get an overview about\n        the allowed keyword arguments call the method keys.\n        '
        configdict,cnf={'height':lambda cnf: Frame.config(self,cnf),'width':lambda cnf: Frame.config(self,cnf),'fg':self.text,'bd':lambda cnf: Frame.config(self,cnf),'relief':lambda cnf: Frame.config(self,cnf)},cnfmerge(cnf,kw)
        for key in cnf:
            if key not in ['height','width','bg','fg','bd','relief']: raise TclError("unknown option '-%s'" % key)
        for key in cnf:
            if key!='bg': configdict[key].config({key:cnf[key]})
            else:
                Frame.config(self,bg=cnf[key])
                self.text.config(bg=cnf[key])

class WidgetSizeMapper(Toplevel):
    '''Mapper for Size of Widget on grid.
    Returns None if canceled, else dictionary with height and width.'''
    def __init__(self,master=None,bd=5,bg='gainsboro',cellsize=[10,10],framesize=[100,100],toolwindow=False,iconname=''):
        Toplevel.__init__(self,master,height=500,width=500)
        if iconname!='': self.iconbitmap(os.path.dirname(sys.argv[0])+'\WSM.ico')
        self.grab_set()
        self.focus_force()
        self.title('Mapper')
        self.attributes('-toolwindow',toolwindow)
        self.minsize(170,170)
        
        self.xaxis,self.yaxis=cellsize
        fheight,fwidth=framesize
        self.bd,self.mode,self.result,self.keys=bd,None,None,[]

        self.bind('<Alt-s>',self.configgrid)
        self.bind('<Return>',self.confirm)
        self.bind('<Escape>',lambda event: self.destroy())
        
        self.bottom=Frame(self,height=46,bg='gainsboro')
        self.bottom.pack(side=BOTTOM,fill=X)
        Button(self.bottom,height=1,text='Bestätigen',command=self.confirm).pack(padx=10,pady=10,side=LEFT)
        Button(self.bottom,height=1,text='Abbrechen',command=self.destroy,width=10).pack(padx=(0,10),pady=10,side=RIGHT)

        self.canvas=Canvas(self,height=454,width=500,bg='white')
        self.canvas.pack(side=TOP,fill=BOTH,expand=True)
        self.canvas.bind('<Configure>',self.gridder)

        self.frame=Frame(self.canvas,height=fheight-1,width=fwidth-1,bd=bd,bg=bg,relief=RIDGE)
        self.frame.place(x=3,y=3)

        self.geometry('%sx%s' % (fwidth+20,fheight+66))

        self.frame.bind('<ButtonPress-1>',self.clickframe)
        self.frame.bind('<Button1-Motion>',self.motionframe)
        self.frame.bind('<ButtonRelease-1>',self.releaseframe)
        self.bind('<KeyPress>',self.keypress)
        self.bind('<KeyRelease>',self.keyrelease)
    def gridder(self,event=None):
        'Intern function'
        width,height=self.canvas.winfo_width(),self.canvas.winfo_height()
        self.canvas.delete('grid_line')
        for i in range(0,width,self.xaxis): self.canvas.create_line([(i+2,0),(i+2,height)],tag='grid_line')
        for i in range(0,height,self.yaxis): self.canvas.create_line([(0,i+2),(width,i+2)],tag='grid_line')
    def confirm(self,event=None):
        'Intern function'
        self.result={key:self.frame[key]+1 for key in ['height','width']}
        self.destroy()
    def configgrid(self,event=None):
        'Intern function'
        self.inputwindow=Toplevel(self,height=132,width=200)
        self.inputwindow.attributes('-toolwindow',True)
        self.inputwindow.resizable(False,False)
        self.inputwindow.grab_set()
        self.inputwindow.focus_force()
        xvar,yvar=IntVar(value=self.xaxis),IntVar(value=self.yaxis)
        
        leftframe=Frame(self.inputwindow,height=100,width=100)
        leftframe.pack_propagate(False)
        leftframe.place(x=0,y=0)
        rightframe=Frame(self.inputwindow,height=100,width=100)
        rightframe.pack_propagate(False)
        rightframe.place(x=100,y=0)
        
        Entry(leftframe,textvar=xvar,justify=CENTER,bg='white').pack(fill=BOTH,expand=True)
        Entry(rightframe,textvar=yvar,justify=CENTER,bg='white').pack(fill=BOTH,expand=True)

        Button(self.inputwindow,text='Ok',command=self.inputwindow.destroy).place(x=87,y=103)

        self.inputwindow.wait_window()
        self.xaxis,self.yaxis=xvar.get(),yvar.get()
        self.gridder()
    def clickframe(self,event):
        'Intern function'
        if self.frame['width']-self.bd<=event.x<=self.frame['width'] and self.frame['height']-self.bd<=event.y<=self.frame['height']:
            self.mode=SE
            self.config(cursor='bottom_right_corner')
        elif self.frame['width']-self.bd<=event.x<=self.frame['width']:
            self.mode=E
            self.config(cursor='right_side')
        elif self.frame['height']-self.bd<=event.y<=self.frame['height']:
            self.mode=S
            self.config(cursor='bottom_side')
    def motionframe(self,event):
        'Intern function'
        if self.mode==SE: self.frame.config(height=event.y_root-self.frame.winfo_rooty() if event.y_root-self.frame.winfo_rooty()>0 else 1,width=event.x_root-self.frame.winfo_rootx() if event.x_root-self.frame.winfo_rootx()>0 else 1)
        elif self.mode==E: self.frame['width']=event.x_root-self.frame.winfo_rootx() if event.x_root-self.frame.winfo_rootx()>0 else 1
        elif self.mode==S: self.frame['height']=event.y_root-self.frame.winfo_rooty() if event.y_root-self.frame.winfo_rooty()>0 else 1
    def releaseframe(self,event):
        'Intern function'
        self.mode=None
        self.config(cursor='arrow')
    def keypress(self,event):
        'Intern function'
        if event.keysym not in self.keys: self.keys.append(event.keysym)
        if event.keysym in ['Up','Down','Left','Right']:
            for key in self.keys:
                if key=='Up': self.frame['height']-=1 if self.frame['height']>1 else 1
                elif key=='Down': self.frame['height']+=1
                elif key=='Left': self.frame['width']-=1 if self.frame['width']>1 else 1
                elif key=='Right': self.frame['width']+=1
    def keyrelease(self,event):
        'Intern function'
        if event.keysym in self.keys: del self.keys[self.keys.index(event.keysym)]
    def mainloop(self):
        'Call the mainloop for WidgetSizeMapper'
        self.wait_window()
        return self.result

class TkList(list):
    def __init__(self,iterable,magicarg):
        list.__init__(self,iterable)
        self._arg=magicarg
        self.__str__=self.__repr__
    def __contains__(self,obj,arg=None):
        if not isinstance(obj,str): return super().__contains__(obj)
        else: return obj in self.arglist(arg)
    def arglist(self,arg):
        arg=arg if arg!=None else self._arg
        return [widget[arg] for widget in self]
    def count(self,value,arg=None):
        if not isinstance(value,str): return super().count(value)
        else: return self.arglist(arg).count(value)
    def index(self,value,arg=None,start=0,stop=END):
        if not isinstance(value,str): return super().index(value,start,stop if stop!=END else len(self))
        else: return self.arglist(arg).index(value,start,stop if stop!=END else len(self))
    def sort(self,arg=None,key=None,reverse=None):
        if arg is None: super().sort()
        else:
            d={}
            for widget in self: d[obj]=obj[arg]
            dvals=list(d.values())
            sortedvals,self[:]=dvals,[]
            sortedvals.sort()
            for key in d: self.insert(dvals.index(d[key]),key)
    def remove(self,value,arg=None):
        if not isinstance(value,str): super().remove(value)
        else: del self[self.arglist(arg).index(value)]
    def setArg(self,arg):
        self._arg=arg
    def __repr__(self):
        return 'TkList(['+','.join([repr(widget) for widget in self])+'])'

class hvFrame(Frame):
    'hvFrame widget which may contain other widgets, can have a 3D border\nand can be scrolled horizontal and vertical. [MULTIWIDGET, MAP ON hvFrame.mf]'
    def __init__(self,master=None,cnf={},**kw): #minsize=[w,h] #sticky in [NS,EW,NSEW,NONE]
        'Construct a frame widget with the parent MASTER.\n\n        Valid resource names: background, bd, bg, borderwidth, class,\n        colormap, container, cursor, height, highlightbackground,\n        highlightcolor, highlightthickness, relief, takefocus, visual, width,\nyscrollcommand, xscrollcommand, sticky, minsize.'
        cnf,dictupdate=filtercnf(cnf,kw,yscrollcommand=None,xscrollcommand=None,sticky=NONE,minsize=None,showfocus=NONE,minwidth=None,minheight=None)
        if dictupdate['sticky'] not in [NS,EW,NSEW,NONE]: raise TclError('Unknown mode \'{}\'. Please use \'{}\', \'{}\', \'{}\' or \'{}\''.format(dictupdate['sticky'],NS,EW,NSEW,NONE))
        self.__dict__.update(dictupdate)
        self.x=self.y=self.yscroll=self.xscroll=0
        self.focused={}
        if self.minsize is not None: self.minwidth,self.minheight=self.minsize
        else: self.minsize=(self.minwidth,self.minheight)
        Frame.__init__(self,master,cnf)
        self.pack_propagate(False)
        self.oldheight,self.oldwidth,self.internal=self.winfo_reqheight(),self.winfo_reqwidth(),False
        self._support=Frame(self,bg=self['bg'])
        self._support.pack(fill=BOTH,expand=True)
        self.mf=Frame(self._support,bg=self['bg'])
        placecnf={'x':0,'y':0}
        if self.sticky in [EW,NSEW] and (self.minwidth is None or self.oldwidth<self.minwidth): placecnf['relwidth']=1
        if self.sticky in [NS,NSEW] and (self.minheight is None or self.oldheight<self.minheight): placecnf['relheight']=1
        if self.sticky in [NS,NONE] and self.minwidth is not None: placecnf['width']=self.minwidth
        if self.sticky in [EW,NONE] and self.minheight is not None: placecnf['height']=self.minheight
        self.mf.place(cnf=placecnf)
        self.bind('<Configure>',self._adopt)
        self.mf.bind('<Configure>',self._adopt)
    def __getitem__(self,key): return self.cget(key)
    def _adoptmf(self,event=None):
        'Internal function'
        if not self.internal:
            self.internal=True
            placeinfo=self.mf.place_info().copy()
            if self.minheight is not None and self.mf.winfo_reqheight()<=self.minheight:
                if placeinfo['height']!=self.minheight: self.mf.place_configure(relheight='',height=self.minheight)
            elif self.sticky in [NS,NSEW]:
                if placeinfo['relheight']!=1: self.mf.place_configure(relheight=1,height='')
            else: self.mf.place_configure(relheight='',height='')
            if self.minwidth is not None and self.mf.winfo_reqwidth()<=self.minwidth:
                if placeinfo['width']!=self.minwidth: self.mf.place_configure(relwidth='',width=self.minwidth)
            elif self.sticky in [EW,NSEW]:
                if placeinfo['relwidth']!=1: self.mf.place_configure(relwidth=1,width='')
            else: self.mf.place_configure(relwidth='',width='')
            self.internal=False
    def _adopt(self,event=None,newx=None,newy=None):
        'Internal function'
        self.mf.update(),self.update()
        self._adoptmf()
        smheight,sheight,smwidth,swidth=self.mf.winfo_height(),self.winfo_height(),self.mf.winfo_width(),self.winfo_width()
        #print('adopt:',smheight,sheight,smwidth,swidth,'\n')
        self.y+=sheight-self.oldheight if sheight-self.oldheight>=0 else 0
        self.x+=swidth-self.oldwidth if swidth-self.oldwidth>=0 else 0
        if newx is not None: self.x=newx
        if newy is not None: self.y=newy
        if self.x>0: self.x=0
        elif swidth-smwidth<=0 and self.x<swidth-smwidth: self.x=swidth-smwidth
        if self.y>0: self.y=0
        elif sheight-smheight<=0 and self.y<sheight-smheight: self.y=sheight-smheight
        self.mf.place_configure(x=self.x,y=self.y)
        self.oldheight,self.oldwidth=sheight,swidth
        if self.yscrollcommand is not None and smheight>sheight:
            perc,self.yscroll=abs(self.y/(smheight-sheight)),sheight/smheight
            self.yscrollcommand(perc-perc*self.yscroll,perc-perc*self.yscroll+self.yscroll)
        elif self.yscrollcommand is not None:
            self.yscroll=0
            self.yscrollcommand(0,1)
        if self.xscrollcommand is not None and smwidth>swidth:
            perc,self.xscroll=abs(self.x/(smwidth-swidth)),swidth/smwidth
            self.xscrollcommand(perc-perc*self.xscroll,perc-perc*self.xscroll+self.xscroll)
        elif self.xscrollcommand is not None:
            self.xscroll=0
            self.xscrollcommand(0,1)
        if self.showfocus!=NONE:
            current=list(self.focused.keys())
            for widget in getallchildren(self.mf):
                if widget in current: current.remove(widget)
                else: self.focused[widget]=widget.bind('<FocusIn>',self.focus)
            for widget in current: 
                try: widget.unbind('',self.focused.pop(widget))
                except TclError: self.focused.pop(widget,None)
                except KeyError: pass
    def focus(self,child):
        if isinstance(child,Event): mh=masterhistory(child.widget)
        else: mh=masterhistory(child)
        x,y=None,None
        for widget in self.mf.children.values():
            if widget in mh: break
        else: return 'break'
        realy,realx,subheight,subwidth=widget.winfo_y()+self.y,widget.winfo_x()+self.x,self._support.winfo_height()-widget.winfo_height(),self._support.winfo_width()-widget.winfo_width()
        if self.showfocus in (N,NW,NE) and not 0<=realy<=subheight: y=-widget.winfo_y()
        elif self.showfocus in (S,SW,SE) and not 0<=realy<=subheight: y=subheight-widget.winfo_y()
        if self.showfocus in (W,NW,SW) and not 0<=realx<=subwidth: x=-widget.winfo_x()
        elif self.showfocus in (E,NE,SE) and not 0<=realx<=subwidth: x=subheight-widget.winfo_x()
        self._adopt(newx=x,newy=y)
    def yview(self,*args):
        'Query and change the vertical position of the view.'
        try:
            if self.yscroll>0:
                maxnegscroll=self.winfo_height()-self.mf.winfo_height()
                if len(args)==1: type,val=args[0],args[0].delta
                elif len(args)==2: type,val=args
                else: type,val,mode=args
                val=float(val)
                if type==MOVETO: self.y=round(maxnegscroll*val/(1-self.yscroll))
                elif type==PIXEL: self.y+=val
                elif isinstance(type,Event):
                    for widget in masterhistory(type.widget):
                        if isinstance(widget,Scrollbar) or hasattr(widget,'yview'): break
                    if widget==self: self.y+=val/4
                elif type==SCROLL and mode==UNITS and abs(val)==1: self.y-=val*10
                elif type==SCROLL and mode==UNITS: self.y-=round(-val*.1*maxnegscroll/4)
                elif type==SCROLL and mode==PAGES: self.y-=round(-val*.2*maxnegscroll)
                if self.y<maxnegscroll: self.y=maxnegscroll
                elif self.y>0: self.y=0
                perc=abs(self.y/maxnegscroll)
                self.mf.place_configure(y=self.y)
                self.yscrollcommand(perc-perc*self.yscroll,perc-perc*self.yscroll+self.yscroll)
        except RecursionError: pass
        return 'break'
    def xview(self,*args):
        'Query and change the horizontal position of the view.'
        try:
            if self.xscroll>0:
                maxnegscroll=self.winfo_width()-self.mf.winfo_width()
                if len(args)==1: type,val=args[0],args[0].delta
                elif len(args)==2: type,val=args
                else: type,val,mode=args
                val=float(val)
                if type==MOVETO: self.x=round(maxnegscroll*val/(1-self.xscroll))
                elif type==PIXEL: self.x+=val
                elif isinstance(type,Event):
                    for widget in masterhistory(type.widget):
                        if hasattr(widget,'xview'): break
                    if widget==self: self.x+=val/4
                elif type==SCROLL and mode==UNITS and abs(val)==1: self.x-=val*10
                elif type==SCROLL and mode==UNITS: self.x-=round(-val*.1*maxnegscroll/4)
                elif type==SCROLL and mode==PAGES: self.x-=round(-val*.2*maxnegscroll)
                if self.x<maxnegscroll: self.x=maxnegscroll
                elif self.x>0: self.x=0
                perc=abs(self.x/maxnegscroll)
                self.mf.place_configure(x=self.x)
                self.xscrollcommand(perc-perc*self.xscroll,perc-perc*self.xscroll+self.xscroll)
        except RecursionError: pass
        return 'break'
    def place(self,cnf={},**kw):
        'Place a widget in the parent widget. Use as options:\n        in=master - master relative to which the widget is placed\n        in_=master - see \'in\' option description\n        x=amount - locate anchor of this widget at position x of master\n        y=amount - locate anchor of this widget at position y of master\n        relx=amount - locate anchor of this widget between 0.0 and 1.0\n                      relative to width of master (1.0 is right edge)\n        rely=amount - locate anchor of this widget between 0.0 and 1.0\n                      relative to height of master (1.0 is bottom edge)\n        anchor=NSEW (or subset) - position anchor according to given direction\n        width=amount - width of this widget in pixel\n        height=amount - height of this widget in pixel\n        relwidth=amount - width of this widget between 0.0 and 1.0\n                          relative to width of master (1.0 is the same width\n                          as the master)\n        relheight=amount - height of this widget between 0.0 and 1.0\n                           relative to height of master (1.0 is the same\n                           height as the master)\n        bordermode="inside" or "outside" - whether to take border width of\n                                           master widget into account\n        '
        super().place(cnf,**kw)
        self._adoptmf()
    place_configure=place
    def pack(self,cnf={},**kw):
        'Pack a widget in the parent widget. Use as options:\n        after=widget - pack it after you have packed widget\n        anchor=NSEW (or subset) - position widget according to\n                                  given direction\n        before=widget - pack it before you will pack widget\n        expand=bool - expand widget if parent size grows\n        fill=NONE or X or Y or BOTH - fill widget if widget grows\n        in=master - use master to contain this widget\n        in_=master - see \'in\' option description\n        ipadx=amount - add internal padding in x direction\n        ipady=amount - add internal padding in y direction\n        padx=amount - add padding in x direction\n        pady=amount - add padding in y direction\n        side=TOP or BOTTOM or LEFT or RIGHT -  where to add this widget.\n        '
        super().pack(cnf,**kw)
        self._adoptmf()
    pack_configure=pack
    def grid(self,cnf={},**kw):
        'Position a widget in the parent widget in a grid. Use as options:\n        column=number - use cell identified with given column (starting with 0)\n        columnspan=number - this widget will span several columns\n        in=master - use master to contain this widget\n        in_=master - see \'in\' option description\n        ipadx=amount - add internal padding in x direction\n        ipady=amount - add internal padding in y direction\n        padx=amount - add padding in x direction\n        pady=amount - add padding in y direction\n        row=number - use cell identified with given row (starting with 0)\n        rowspan=number - this widget will span several rows\n        sticky=NSEW - if cell is larger on which sides will this\n                      widget stick to the cell boundary\n        '
        super().grid(cnf,**kw)
        self._adoptmf()
    grid_configure=grid
    def keys(self):
        'Return a list of all resource names of this widget.'
        return super().keys()+['yscrollcommand','xscrollcommand','sticky','minsize','showfocus','minwidth','minheight']
    def config(self,cnf=None,**kw):
        'Configure resources of a widget.\n\n        The values for resources are specified as keyword\n        arguments. To get an overview about\n        the allowed keyword arguments call the method keys.\n        '
        self.update()
        cnf,dictupdate=filtercnf(cnf,kw,'yscrollcommand','xscrollcommand','sticky','minsize','showfocus','minwidth','minheight')
        self.__dict__.update(dictupdate)
        if 'yscrollcommand' in dictupdate: self.yview(None,None)
        if 'xscrollcommand' in dictupdate: self.xview(None,None)
        if 'sticky' in dictupdate: self._adoptmf()
        if 'minsize' in dictupdate:
            self.minwidth,self.minheight=self.minsize
        if 'minheight' in dictupdate or 'minwidth' in dictupdate:
            placeinfo=self.mf.place_info()
            if placeinfo['width']!='': self.mf.place_configure(width=self.minwidth)
            if placeinfo['height']!='': self.mf.place_configure(height=self.minheight)
            self.minsize=self.minwidth,self.minheight
            self._adoptmf()
        if 'showfocus' in dictupdate: 
            if self.showfocus!=NONE: self._adopt()
            else:
                for widget in self.focused.keys():
                    try: widget.unbind('',self.focused.pop(widget))
                    except TclError: self.focused.pop(widget,None)
                    except KeyError: pass
        if 'bg' in cnf:
            self._support.config(bg=cnf['bg'])
            self.mf.config(bg=cnf['bg'])
        super().config(cnf=cnf)
    configure=config
    def cget(self,key):
        'Return the resource value for a key given as string.'
        if key in ('yscrollcommand','xscrollcommand','sticky','minsize','showfocus','minwidth','minheight'): return getattr(self,key)
        else: return super().cget(key)
    __getitem__=cget

class Table(Frame):
    'hvFrame widget which may contain other widgets, can have a 3D border\nand can be scrolled horizontal and vertical. [MULTIWIDGET, DO NOT MAP ON IT]'
    def __init__(self,master=None,horizontal=None,vertical=None,map=None,cnf={},**kw):
        cnf,dictupdate=filtercnf(cnf,kw,horizontalanchor=N,verticalanchor=W,padx=1,pady=1,corner='',cellcnf={},hvcnf={})
        self.__dict__.update(dictupdate)

        Frame.__init__(self,master,cnf)
        self.grid_propagate(False)
        self.rowconfigure(0,weight=True)
        self.columnconfigure(0,weight=True)
        self.ysb=Scrollbar(self)
        self.ysb.grid(row=0,column=1,sticky=NS)
        self.xsb=Scrollbar(self,orient=HORIZONTAL)
        self.xsb.grid(row=1,column=0,sticky=EW)
        self.table=hvFrame(self,self.hvcnf,yscrollcommand=self.ysb.set,xscrollcommand=self.xsb.set,sticky=NSEW,bg='black')
        self.table.grid(row=0,column=0,sticky=NSEW)
        self.ysb.config(command=self.table.yview),self.xsb.config(command=self.table.xview)
        self.h,self.v,self.m=TkList([],'text'),TkList([],'text'),[]
        self.setup(horizontal,vertical,map)
    def setup(self,horizontal=None,vertical=None,map=None):
        if horizontal is None: horizontal=['']
        if vertical is None: vertical=['']
        if map is None: map=[['']*len(horizontal)]*len(vertical)
        if len(map)==len(vertical)!=0 and len(map[0])==len(vertical)!=0:
            for widget in list(self.table.mf.children.values()): widget.destroy()
            #print(len(self.v),len(vertical),len(self.v)!=len(vertical))
            if len(self.v)!=len(vertical):
                for row in range(len(self.v)+1): self.table.mf.rowconfigure(row,weight=False)
                for row in range(len(vertical)+1): self.table.mf.rowconfigure(row,weight=True)
            #print(len(self.h),len(horizontal),len(self.h)!=len(horizontal))
            if len(self.h)!=len(horizontal):
                for col in range(len(self.h)+1): self.table.mf.columnconfigure(col,weight=False)
                for col in range(len(horizontal)+1): self.table.mf.columnconfigure(col,weight=True)
            self.h,self.v,self.m,iN,iW,iS,iE,heights,widths=TkList([],'text'),TkList([],'text'),[],int(self.horizontalanchor==N),int(self.verticalanchor==W),int(self.horizontalanchor==S),int(self.verticalanchor==E),[],[]
            self.cl=Label(self.table.mf,cnf=self.cellcnf,text=self.corner)
            self.cl.grid(row=iS*len(vertical),column=iE*len(horizontal),sticky=NSEW,pady=(3*iS,3*iN),padx=(3*iE,3*iW))
            cwidth,cheight=self.cl.winfo_reqwidth(),self.cl.winfo_reqheight()
            pady,padx,width=(3*iS,3*iN),(self.padx*iW,self.padx*iE),cwidth
            for col,text in enumerate(horizontal):
                self.h.append(Label(self.table.mf,cnf=self.cellcnf,text=text))
                self.h[-1].grid(row=iS*len(vertical),column=col+iW,sticky=NSEW,padx=padx,pady=pady)
                width+=self.h[-1].winfo_reqwidth()
            widths.append(width)
            pady,padx,height=(self.pady*iN,self.pady*iS),(3*iE,3*iW),cheight
            for row,text in enumerate(vertical):
                self.v.append(Label(self.table.mf,cnf=self.cellcnf,text=text))
                self.v[-1].grid(row=row+iN,column=iE*len(horizontal),sticky=NSEW,padx=padx,pady=pady)
                height+=self.v[-1].winfo_reqheight()
            padx,pady=(self.padx*iW,self.padx*iE),(self.pady*iN,self.pady*iS)
            for row,rowlist in enumerate(map):
                self.m.append([])
                height,width=cheight,cwidth
                for col,text in enumerate(rowlist):
                    self.m[row].append(Label(self.table.mf,cnf=self.cellcnf,text=text))
                    self.m[row][-1].grid(row=row+iN,column=col+iW,sticky=NSEW,padx=padx,pady=pady)
                    height+=self.m[row][-1].winfo_reqheight()
                    width+=self.m[row][-1].winfo_reqwidth()
                widths.append(width),heights.append(height)
            self.table.config(minsize=(max(widths),max(heights)))
            self.table._adopt()
    def keys(self,):
        return super().keys()+['horizontalanchor','verticalanchor','padx','pady','corner','cellcnf','hvcnf']
    def config(self,cnf=None,**kw):
        cnf,dictupdate=filtercnf(cnf,kw,'horizontalanchor','verticalanchor','padx','pady','corner','cellcnf','hvcnf')
        self.__dict__.update(dictupdate)
        
        for key in ['horizontalanchor','verticalanchor','padx','pady','cellcnf']:
            if key in dictupdate: self.setup(self.h.arglist('text'),self.v.arglist('text'),[TkList.arglist(line,'text') for line in self.m]);break
        if 'corner' in dictupdate: self.cl['text']=self.corner
        if 'hvcnf' in dictupdate: self.table.config(self.hvcnf)
        super().config(cnf=cnf)
    def cget(self,key):
        if key in ['horizontalanchor','verticalanchor','padx','pady','corner','cellcnf','hvcnf']: return eval('self.'+key)
        return  super().cget(key)

class Comparetable(Frame):
    'Comparetable widget which can have a 3D border.\n[MULTIWIDGET, DO NOT MAP ON IT]'
    def __init__(self,master=None,head=None,body=None,cnf={},**kw):
        'Construct a frame widget with the parent MASTER.\n\n        Valid resource names: background, bd, bg, borderwidth, class,\n        colormap, container, cursor, height, highlightbackground,\n        highlightcolor, highlightthickness, relief, takefocus, visual, width,\n        padx, pady, separatorwidth, cellcnf.'
        cnf,dictupdate=filtercnf(cnf,kw,padx=1,pady=1,separatorwidth=3,cellcnf={},hvcnf={})
        self.__dict__.update(dictupdate)

        Frame.__init__(self,master,cnf)
        self.grid_propagate(False)
        self.rowconfigure(0,weight=True)
        self.columnconfigure(0,weight=True)
        ysb=Scrollbar(self)
        xsb=Scrollbar(self,orient=HORIZONTAL)
        ysb.grid(row=0,column=1,sticky=NS)
        xsb.grid(row=1,column=0,sticky=EW)
        self.table=hvFrame(self,self.hvcnf,yscrollcommand=ysb.set,xscrollcommand=xsb.set,sticky=NSEW,bg='black')
        self.table.mf.rowconfigure(0,weight=True),self.table.mf.rowconfigure(1,weight=True)
        self.table.grid(row=0,column=0,sticky=NSEW)
        ysb.config(command=self.table.yview),xsb.config(command=self.table.xview)
        self.h,self.b=TkList([],'text'),[[]]
        self.setup(head,body)
    def setup(self,head=None,body=None):
        'Updates head or body when given.\nbody should at least be an empty list in a list.'
        if head is None: head=['']
        if body is None: body=[['']*len(head)]
        bh,bw,obh,obw=len(body),len(body[0]),len(self.b),len(self.b[0])
        if obw|len(head)>0:
            for row in range(bh+1,obh+1):
                self.table.mf.rowconfigure(row,weight=False)
                for widget in self.b[-1]: widget.destroy()
                del self.b[-1]
            for col in range(bw,obw):
                self.table.mf.columnconfigure(col,weight=False)
                self.h[-1].destroy()
                del self.h[-1]
                for row in range(len(self.b)):
                    self.b[row][-1].destroy()
                    del self.b[row][-1]
            for col in range(obw,bw):
                self.table.mf.columnconfigure(col,weight=True)
                self.h.append(Label(self.table.mf,cnf=self.cellcnf))
                for row in range(len(self.b)): self.b[row].append(Label(self.table.mf,cnf=self.cellcnf))
            for row in range(obh+1,bh+1):
                self.table.mf.rowconfigure(row,weight=True)
                self.b.append([Label(self.table.mf,cnf=self.cellcnf) for i in range(bw)])
            for i,text in enumerate(head): self.h[i]['text']=text
            for row,rowlist in enumerate(body):
                for col,text in enumerate(rowlist):
                    self.b[row][col]['text']=text
            self.table['minsize']=self._regrid()
            self.table._adopt()
    def _regrid(self):
        'Internal function.'
        heights,widths=[],[]
        padx,pady,sep=(self.padx,0),(self.pady,0),(self.separatorwidth-self.pady)*bool(self.separatorwidth)
        self.h[0].grid(row=0,column=0,pady=(0,sep),sticky=NSEW)
        heights.append(self.h[0].winfo_reqheight())
        widths.append(self.h[0].winfo_reqwidth())
        for i in range(1,len(self.h)):
            self.h[i].grid(row=0,column=i,padx=padx,pady=(0,sep),sticky=NSEW)
            heights.append(self.h[i].winfo_reqheight())
            widths[0]+=self.h[i].winfo_reqwidth()
        for row,rowlist in enumerate(self.b):
            rowlist[0].grid(row=row+1,column=0,pady=pady,sticky=NSEW)
            widths.append(rowlist[0].winfo_reqwidth())
            heights[0]+=rowlist[0].winfo_reqheight()
        for row,rowlist in enumerate(self.b):
            for i in range(1,len(rowlist)):
                self.b[row][i].grid(row=row+1,column=i,padx=padx,pady=pady,sticky=NSEW)
                heights[i]+=self.b[row][i].winfo_reqheight()
                widths[row+1]+=self.b[row][i].winfo_reqwidth()
        return max(widths),max(heights)
    def __getitem__(self,key):
        'Return the resource value for a key given as string.'
        return self.cget(key)
    def keys(self):
        'Return a list of all resource names of this widget.'
        return super().keys()+['padx','pady','separatorwidth','cellcnf','hvcnf']
    def config(self,cnf=None,**kw):
        'Configure resources of a widget.\n\n        The values for resources are specified as keyword\n        arguments. To get an overview about\n        the allowed keyword arguments call the method keys.'
        cnf,dictupdate=filtercnf(cnf,kw,'padx','pady','separatorwidth','cellcnf','hvcnf')
        if 'cellcnf' in dictupdate:
            self.cellcnf=dictupdate.pop('cellcnf')
            if 'text' in self.cellcnf: del self.cellcnf['text']
            for widget in self.h: widget.config(cnf=self.cellcnf)
            for row in self.b.copy():
                for widget in row.copy(): widget.config(cnf=self.cellcnf)
        if 'hvcnf' in dictupdate:
            self.hvcnf=dictupdate.pop('hvcnf')
            for key in ('sticky','yscrollcommand','xscrollcommand'):
                if key in self.hvcnf: del self.hvcnbf[key]
            self.table.config(cnf=self.hvcnf)
        self.__dict__.update(dictupdate)
        if len(dictupdate)>0: self._regrid()
        super().config(cnf=cnf)
    def cget(self,key):
        'Return the resource value for a key given as string.'
        if key in ('anchor','padx','pady','separatorwidth','cellcnf','hvcnf'): return eval('self.'+key)
        return super().cget(key)

class Displaybutton(Frame):
    'Displaybutton widget.'
    def __init__(self,master=None,cnf={},**kw):
        'Construct a button widget with the parent MASTER.\n\n        STANDARD OPTIONS\n\n            activebackground, activeforeground, anchor,\n            background, bitmap, borderwidth, cursor,\n            disabledforeground, font, foreground\n            highlightbackground, highlightcolor,\n            highlightthickness, image, justify,\n            padx, pady, relief, repeatdelay,\n            repeatinterval, takefocus, text,\n            textvariable, underline, wraplength\n\n        WIDGET-SPECIFIC OPTIONS\n\n            command, compound, default, height,\n            overrelief, state, width, command,\n            maxheight,displaybackground\n        '
        cnf,dictupdate=filtercnf(cnf,kw,maxheight=200,command=empty,displaybackground='SystemButtonFace')
        self.__dict__.update(dictupdate)
        Frame.__init__(self,master)
        self.button=Button(self,cnf,command=self.toggle)
        self.button.pack(side=TOP,fill=X,expand=True)
        self.frame=Frame(self)
        self.frame.pack_propagate(False)
        scrollbar=Scrollbar(self.frame)
        scrollbar.pack(side=RIGHT,fill=Y)
        self.scrollframe=hvFrame(self.frame,yscrollcommand=scrollbar.set,sticky=EW,bg=self.displaybackground)
        self.scrollframe.pack(side=LEFT,fill=BOTH,expand=True)
        scrollbar.config(command=self.scrollframe.yview)
        master.winfo_toplevel().bind('<MouseWheel>',self.scrollframe.yview,ADD)
        self.widgets={}
        self.configure=self.config
    def toggle(self):
        '''Toggles wether the hvFrame should be displayed or not.'''
        if self.frame.winfo_ismapped():
            self.frame.pack_forget()
            self.after(1,self.command)
        else:
            self.update()
            self.frame.pack(side=BOTTOM,fill=X,expand=True)
            self.after(1,self.command)
    def keys(self):
        'Return a list of all resource names of this widget.'
        return self.button.keys()+['maxheight','command','displaybackground']
    def addItem(self,widget,cnf={},**kw):
        '''Adds tkinter widget to Dislaybuttons hvFrame.

        @param widget: tkinter widget
        @type widget: Subclass of tkinter.Widget
        @param cnf: configuration of widget (*optional)
        @type cnf: dict
        @param kw: keywords to extend cnf or replace cnf keys (*optional)
        @type kw: dict

        @return: id of added widget
        @rtype: int
        '''
        new=widget(self.scrollframe.mf,cnf,**kw)
        new.pack(fill=X,expand=True)
        new.bind('<Destroy>',self._destroyitem,ADD)
        id=new.winfo_id()
        self.widgets[id]=new

        newheight=self.frame['height']
        if newheight<self.maxheight:
            newheight+=new.winfo_reqheight()
            if newheight>self.maxheight: newheight=self.maxheight
            self.frame['height']=newheight
        return id
    def _destroyitem(self,event):
        '''Internal function
        Deletes widget from listing if it got destroyed externally.

        @param event: tkinters Event object given by Bind
        @type event: tkinter.Event
        '''
        if event.widget in self.widgets.values(): del self.widgets[list(self.widgets.keys())[list(self.widgets.values()).index(event.widget)]]
    def getItem(self,id):
        '''Returns the widget identified by id.

        @param id: identifier of widget
        @type id: int

        @return: widget identified by id
        @rtype: subclass of tkinter.Widget
        '''
        return self.widgets[id]
    def delItem(self,id):
        '''Deletes the widget identified by id.

        @param id: identifier of widget
        @type id: int
        '''
        try: self.widgets[id].destroy()
        except TclError: del self.widgets[id]
    def config(self,cnf=None,**kw):
        'Configure resources of a widget.\n\n        The values for resources are specified as keyword\n        arguments. To get an overview about\n        the allowed keyword arguments call the method keys.\n        '
        cnf,dictupdate=filtercnf(cnf,kw,'maxheight','command','displaybackground')
        if 'maxheight' in dictupdate: self.scrollframe.config(height=maxheight)
        if 'command' in dictupdate: self.command=dictupdate['command']
        if 'displaybackground' in dictupdate: self.scrollframe['bg']=self.displaybackground
        self.button.config(cnf)
    def cget(self,key):
        'Return the resource value for a KEY given as string.'
        if key in ('maxheight','command','displaybackground'): return eval('self.'+key)
        return self.button.cget(key)
    def __getitem__(self,key):
        'Return the resource value for a KEY given as string.'
        return self.cget(key)

class SearchDialog(Toplevel): #157x183
    def __init__(self,master,selectcommand,generatorcommand,title=''):
        self.scmd,self.gcmd=selectcommand,generatorcommand
        self.pos=0
        
        Toplevel.__init__(self,master,height=183,width=300)
        self.title(title)
        self.resizable(False,False)
        self.grid_propagate(False)
        self.attributes('-toolwindow',True)
        self.attributes('-topmost',True)
        for row in range(5): self.rowconfigure(row,weight=True)
        self.columnconfigure(0,weight=True)
        self.columnconfigure(1,weight=True)
        
        Label(self,text='Suchen:').grid(sticky=W,padx=10,pady=10)
        self.entry=dEntry(self)
        self.entry.grid(columnspan=2,sticky=EW,padx=10)
        Button(self,text='Bestätigen',command=self.generate).grid(column=1,sticky=E,padx=10,pady=10)
        
        self.buttons=Frame(self)
        self.buttons.grid(columnspan=2,sticky=EW,padx=10,pady=(5,0))
        self.priorbutton=Button(self.buttons,text='Vorheriges',command=self.prior,state=DISABLED)
        self.priorbutton.pack(side=LEFT)
        self.nextbutton=Button(self.buttons,text='Nächstes',command=self.next,state=DISABLED)
        self.nextbutton.pack(side=LEFT)

        Button(self,text='Abbrechen',command=self.destroy).grid(column=1,sticky=E,padx=10,pady=10)

        self.entry.focus()
        self.focus_force()
        self.wait_window()
    def generate(self):
        entry=self.entry.get()
        self.returns=self.gcmd(entry)
        if self.returns=='invalid': mb.showerror('NotFoundError',repr(entry)+' konnte nicht gefunden werden.')
        else:
            try: self.scmd(*self.returns[self.pos])
            except: pass
            self.pos=0
            self.scmd(*self.returns[self.pos])
            self.priorbutton.config(state=NORMAL),self.nextbutton.config(state=NORMAL)
            self.master.focus_force()
    def prior(self):
        if len(self.returns)!=1: self.scmd(*self.returns[self.pos])
        self.pos=(self.pos-1)%len(self.returns)
        self.scmd(*self.returns[self.pos])
        self.master.focus_force()
    def next(self):
        if len(self.returns)!=1: self.scmd(*self.returns[self.pos])
        self.pos=(self.pos+1)%len(self.returns)
        self.scmd(*self.returns[self.pos])
        self.master.focus_force()

class InfoBox(Toplevel):
    def __init__(self,master=None,text='',entercmd=None,leavecmd=None,rimcolor='#646464',rimwidth=1,**kw):
        self._entercmd,self._leavecmd=entercmd,leavecmd
        Toplevel.__init__(self,master,bg=rimcolor)
        master.bind('<Enter>',self._show_init,ADD)
        master.bind('<Leave>',self.hide,ADD)
        self._text=Label(self,kw,text=text,bg='#ffffe1')
        self._text.pack(fill=BOTH,expand=True,padx=rimwidth,pady=rimwidth)
        self.resizable(False,False)
        self.overrideredirect(True)
        self.update()
        self.width,self.height=self.winfo_width(),self.winfo_height()
        self.geometry('+%i+%i'%(self.winfo_screenwidth()+1,self.winfo_screenheight()+1))
    def _show_init(self,event=None):
        self.after(750,self.show)
    def config(self,cnf=None,**kw):
        cnf,other=filtercnf(cnf,kw,'bg','entercmd','leavecmd','rimcolor','rimwidth')
        if 'entercmd' in other: self._entercmd=other['entercmd']
        if 'leavecmd' in other: self._leavecmd=other['leavecmd']
        if 'rimcolor' in other: self.config(bg=other['rimcolor'])
        if 'rimwidth' in other: self._text.pack_configure(padx=cnf['rimwidth'],pady=cnf['rimwidth'])
        self._text.config(cnf)
        if self.state()!='withdrawn':
            sw,sh,mh,sx,sy=self.winfo_screenwidth(),self.winfo_screenheight(),self.master.winfo_height(),self.winfo_pointerx(),self.master.winfo_rooty()
            self.geometry('%i+%i'%(sx if sx+self.width<=sw else sx-self.width,sy+mh+5 if sy+mh+self.height+5<=sh else sy-self.height-5))
    configure=config
    def cget(self,key):
        if key=='entercmd' or key=='leavecmd': return getattr(self,'_'+key)
        else: return self._text.cget(key)
    __getitem__=cget
    def keys(self):
        return ['activeforeground', 'anchor', 'bd', 'bitmap', 'borderwidth', 'compound', 'cursor', 'disabledforeground', 'fg', 'font', 'foreground', 'height', 'highlightbackground',
                'highlightcolor', 'highlightthickness', 'image', 'justify', 'padx', 'pady', 'relief', 'state', 'takefocus', 'text', 'textvariable', 'underline', 'width', 'wraplength',
                'entercmd', 'leavecmd']
    def hide(self,event=None):
        self.state('withdrawn')
        if self._leavecmd: self._leavecmd()
    def show(self):
        masterwindow=self.master.winfo_toplevel()
        if masterwindow.winfo_containing(*self.winfo_pointerxy())==self.master:
            self.state('normal')
            sw,sh,mh,sx,sy=masterwindow.winfo_rootx()+masterwindow.winfo_width(),masterwindow.winfo_rooty()+masterwindow.winfo_height(),self.master.winfo_height(),self.winfo_pointerx(),self.master.winfo_rooty()
            x,y=sx if sx+self.width<=sw else sx-self.width,sy+mh+5 if sy+mh+self.height+5<=sh else sy-self.height-5
            self.tkraise(masterwindow)
            self.geometry('+%i+%i'%(x,y))
            if self._entercmd: self._entercmd()

class MouseMove:
    'MouseMove(master [, yview, xview, button, scrolltype, scrollfaktor, scrollmode, over, sleep])'
    def __init__(self,master,yscrollcommand=None,xscrollcommand=None,button=2,scrolltype=SCROLL,scrollfactor=4,scrollmode=UNITS,over=None,sleep=1):
        self.master,self.ysc,self.xsc,self.st,self.f,self.sm,self.over,self.sleep=master,yscrollcommand,xscrollcommand,scrolltype,scrollfactor,scrollmode,over,sleep
        self.x,self.dx,self.y,self.dy=None,0,None,0
        self.master.bind('<ButtonPress-%i>'%button,self.press,ADD)
        self.master.bind('<Motion>',self.motion,ADD)
        self.master.bind('<Escape>',self.release,ADD)
    def _cursor(self,dx,dy):
        if -5<=dx<=5:
            if dy>5: return 'bottom_side'
            elif dy<-5: return 'top_side'
        elif -5<=dy<=5:
            if dx>5: return 'right_side'
            elif dx<5: return 'left_side'
        elif dx<-5:
            if dy>5: return 'bottom_left_corner'
            elif dy<-5: return 'top_left_corner'
        elif dx>5:
            if dy>5: return 'bottom_right_corner'
            elif dy<-5: return 'top_right_corner'
        return 'fleur'
    def press(self,event):
        if self.x is not None: self.release(event)
        elif not self.over or self.over in masterhistory(self.master.winfo_containing(event.x_root,event.y_root)):
            toplevel=self.master.winfo_toplevel()
            self.widget=Frame(toplevel,bg='white',bd=5,relief=RIDGE,height=10,width=10)
            self.widget.place(x=event.x_root-toplevel.winfo_rootx()-5,y=event.y_root-toplevel.winfo_rooty()-5)
            self.widget.focus()
            self.widget.bind('<FocusOut>',self.release)
            self.x,self.y,self.oldcursor=event.x_root,event.y_root,self.master['cursor']
            self.master.config(cursor='fleur')
            self.loop()
    def motion(self,event): #type,val,mode
        if self.x is not None:
            self.dx,self.dy=event.x_root-self.x,event.y_root-self.y
            self.master.config(cursor=self._cursor(self.dx,self.dy))
    def loop(self):
        if self.x is not None:
            if self.ysc and not -5<self.dy<5: self.ysc(self.st,int(self.dy*self.f),self.sm)
            if self.xsc and not -5<self.dx<5: self.xsc(self.st,int(self.dx*self.f),self.sm)
            self.master.after(self.sleep,self.loop)
    def release(self,event):
        if self.x is not None:
            self.x,self.y=None,None
            self.master.config(cursor=self.oldcursor)
            self.widget.destroy()

class WarnEntry(Frame):
    def __init__(self,master=None,cnf={},**kw):
        cnf,dictupdate=filtercnf(cnf,kw,checkcommand=None,warnchar='*',warncolor='red',bell=False)
        self.__dict__.update(dictupdate)
        Frame.__init__(self,master,relief=SUNKEN)
        self.entry=dEntry(self,bd=0)
        self.entry.pack(side=LEFT,fill=BOTH,expand=True)
        self.entry.bind('<FocusIn>',self._focusin,ADD)
        self.entry.bind('<FocusOut>',self._focusout,ADD)
        self.label=Label(self,width=1,bd=0,bg=self.entry['bg'],fg=self.warncolor)
        self.label.pack(side=RIGHT,fill=Y)
        self.config(cnf)
        self.mode,self.bg=True,super().cget('bg')
        self.get=self.entry.get
        self.insert=self.entry.insert
        self.delete=self.entry.delete
    def toggle(self,mode=None):
        if mode is None: self.mode=not self.mode
        else: self.mode=mode
        if self.mode:
            super().config(bg=self.bg)
            self.label['text']=''
        else:
            super().config(bg=self.warncolor)
            self.label['text']=self.warnchar
            if self.bell: self.entry.bell()
    def _focusin(self,event):
        if self.checkcommand is not None: self.toggle(True)
    def _focusout(self,event):
        if self.checkcommand is not None: self.toggle(self.checkcommand(self.entry.get()))
    def keys(self):
        return self.entry.keys()+['checkcommand','warnchar','warncolor','bell']
    def cget(self,key):
        if key in ['checkcommand','warnchar','warncolor','bell']: return eval('self.'+key)
        elif key in ['borderwidth','bd','cursor','relief','state']: return super().cget(key)
        else: return self.entry.cget(key)
    __getitem__=cget
    def config(self,cnf=None,**kw):
        cnf,dictupdate=filtercnf(cnf,kw,'background','bg','borderwidth','bd','cursor','disabledforeground','font','relief','state','width','checkcommand','warnchar','warncolor','bell')
        if 'bg' in dictupdate:
            bg=dictupdate['bg']
            self.entry['bg'],self.label['bg']=bg,bg
            super().config(bg=bg)
        elif 'background' in dictupdate:
            bg=dictupdate['background']
            self.entry['bg'],self.label['bg']=bg,bg
            super().config(bg=bg)
        if 'bd' in dictupdate: super().config(bd=dictupdate['bd'])
        elif 'borderwidth' in dictupdate: super().config(bd=dictupdate['borderwidth'])
        if 'cursor' in dictupdate:
            cursor=dictupdate['cursor']
            self.entry['cursor'],self.label['cursor']=cursor,cursor
            super().config(cursor=cursor)
        if 'disabledforeground' in dictupdate:
            dfg=dictupdate['disabledforeground']
            self.entry['disabledforeground'],self.label['disabledforeground']=dfg,dfg
        if 'font' in dictupdate:
            font=dictupdate['font']
            self.entry['font'],self.label['font']=font,font
        if 'relief' in dictupdate: super().config(relief=dictupdate['relief'])
        if 'state' in dictupdate:
            state=dictupdate['state']
            self.entry['state'],self.label['state']=state,state
            super().config(state=state)
        if 'width' in dictupdate: self.entry['width']=dictupdate['width']-1 if dictupdate['width']>0 else 0
        if 'checkcommand' in dictupdate: self.checkcommand=dictupdate['checkcommand']
        if 'warnchar' in dictupdate: self.warnchar=dictupdate['warnchar']
        if 'warncolor' in dictupdate: self.label['fg']=dictupdate['warncolor']
        if 'bell' in dictupdate: self.bell=dictupdate['bell']
        self.entry.config(cnf)
    configure=config
    

class EventHandler:
    def __init__(self,func,event=None,*args,**kwargs): self.func,self.event,self.args,self.kwargs=func,event,args,kwargs
    def __call__(self,event):
        if self.event is None: self.func(*self.args,**self.kwargs)
        elif self.event=='': self.func(event,*self.args,**self.kwargs)
        else:
            kw=self.kwargs.copy()
            kw[self.event]=event
            self.func(*args,**kw)

class CheckDot(Canvas):
    def __init__(self,master,cnf={},**kw):
        cnf,dictupdate=filtercnf(cnf,kw,onvalue=True,offvalue=False,color='#000000',command=None,var=None,onlyon=False)
        color=cnf['bg']
        cnf['bg']=master['bg']
        Canvas.__init__(self,master,cnf,highlightthickness=0)
        self.__dict__.update(dictupdate)
        self.state=False
        if self.var is not None: self.var.set(self.offvalue)
        self.bind('<Configure>',self._adopt)
        self.bind('<Button-1>',self.toggle)
        self.create_oval(0,0,self.winfo_height(),self.winfo_width(),fill=color,outline=color,tag='border')
        self.update()
        self._adopt()
    def _adopt(self,event=None):
        height,width=self.winfo_height(),self.winfo_width()
        self.coords('border',0,0,height,width)
        if self.state:
            bd=int(super().cget('bd'))
            width-=2*bd
            height-=2*bd
            self.coords('circle',bd+.1*width,bd+.1*height,.9*width,.9*height)
    def toggle(self,value=None):
        if value is None or isinstance(value,Event): self.state=not self.state
        else: self.state=bool(value)
        if self.state:
            bd=int(super().cget('bd'))
            width,height=self.winfo_width()-2*bd,self.winfo_height()-2*bd
            self.create_oval(bd+.1*width,bd+.1*height,.9*width,.9*height,fill=self.color,outline=self.color,tag='circle')
            if self.var is not None: self.var.set(self.onvalue)
        elif not (self.onlyon and isinstance(value,Event)):
            self.delete('circle')
            if self.var is not None: self.var.set(self.offvalue)
        if self.command is not None: return self.command()
    def keys(self): return ['height','width','bd','relief','state','bg','color','onvalue','offvalue','command','var','onlyon']
    def cget(self,key):
        'Return the resource value for a KEY given as string.'
        if key in ['onvalue','offvalue','command','var','color']: return self.__dict__[key]
        else: return super().cget(key)
    __getitem__=cget
    def config(self,cnf=None,**kw):
        cnf,dictupdate=filtercnf(cnf,kw,'color','onvalue','offvalue','command','var','onlyon')
        super().config(cnf)
        self.__dict__.update(dictupdate)
        if 'color' in dictupdate: self.itemconfig('1',fill=self.color,outline=self.color)
    configure=config
    def get(self): return self.state

class SizeFrame(Frame): #CONTINUE
    def __init__(self,master,height=1,width=1,geom='pack',cnf={},**kw):
        Frame.__init__(self,master,height=height,width=width)
        self.pack_propagate(False)
        self.grid_propagate(False)
        eval('self.'+geom+'(cnf,**kw)')

def alpha(master,fg,bg,a):
    '''Calculates the seen color when fg lays over bg with an alpha value of a.

    @param fg: foreground color
    @type fg: str (#xxxxxx) or iterable (xx,xx,xx)
    @param bg: background color
    @type bg: see fg
    @param a: alpha value of fg
    @type a: float (0<=a<=1)'''
    fg,bg=255*array(master.winfo_rgb(fg))/65535,255*array(master.winfo_rgb(bg))/65535
    return tuple(map(int,bg+a*fg-a*bg))

def rotate(xy,a,cx=0,cy=0,degree=False):
    if degree: a=rad(a)
    out=[]
    for i in range(0,len(xy),2):
        x=xy[i]-cx
        y=xy[i+1]-cy
        out+=[cos(a)*x-sin(a)*y+cx,sin(a)*x+cos(a)*y+cy]
    return out

def RGBtoTkRGB(rgb):
    return "#%02x%02x%02x"%tuple(rgb)

class Trail(Thread):
    def __init__(self,master,diameter,duration,fg,bg=None,maxlen=None):
       '''Setup for Tracertrail. Either duration or length need to be defined.

        @param master: master canvas in wich the trail should get displayed
        @type master: tkinter.Canvas
        @param diamerter: diameter of the traced dot / generated trail
        @type diameter: int
        @param duration: lifespan of the end of the trail
        @type duration: float
        @param bg: backgroundcolor
        @type bg: str (format: '#xxxxxx')'''

       Thread.__init__(self)
       self.c,self.diameter,self.duration,self.maxlen=master,diameter,duration,maxlen
       self.fg,self.bg=fg,bg if bg is not None else master['bg']
       self.active,self.storage={},[]
       self.x,self.running=None,False
    def reset(self): self.x=None
    def update(self,x,y):
        if self.x is None: pass
        elif len(self.storage)>0:
            tag=self.storage.pop()
            self.active[tag]=time.time()
            self.c.coords(tag,self.x,self.y,x,y)
            self.c.itemconfig(tag,fill=self.fg,width=self.diameter)
            if not self.running:
                self.running=True
                self.loop()
        elif (self.maxlen is not None and len(self.active)<self.maxlen) or self.maxlen is None:
            self.active[self.c.create_line(self.x,self.y,x,y,fill=self.fg,width=self.diameter)]=time.time()
            if not self.running:
                self.running=True
                self.loop()
        else:
            tag=list(self.active.keys())[0]
            del self.active[tag]
            self.active[tag]=time.time()
            self.c.coords(tag,self.x,self.y,x,y)
            self.c.itemconfig(tag,fill=self.fg,width=self.diameter)
            if not self.running:
                self.running=True
                self.loop()
        self.x,self.y=x,y
    def loop(self):
        try:
            for tag,tme in list(self.active.copy().items())[::-1]:
                span=time.time()-tme
                if span>=self.duration:
                    self.c.coords(tag,-10,-10,-5,-5)
                    del self.active[tag]
                    self.storage.append(tag)
                else:
                    self.c.itemconfig(tag,fill=RGBtoTkRGB(alpha(self.c,self.fg,self.bg,1-span/self.duration)),width=self.diameter*(1-span/self.duration))
                    self.c.lift(tag)
            self.c.update()
            if len(self.active)>0 and self.running: self.c.after(0,self.loop)
            else: self.running=False
        except TclError as error:
            if str(error)=='invalid command name ".!canvas"': self.running=False
            else: raise error

class RotaryButton(Canvas):
    def __init__(self,master=None,cnf={},**kw):
        '''RotaryButton is an fancy slider. [MULTIWIDGET]

        Valid widget specific resource names:
        from (actually from_ because from is already claimed by Python), to, increment, values, textvar, fg, indicator, minpos, maxpos, startpos, drawback, height, var, exact, command, entrycnf
        All other resource names correspond to the base Canvas.
        '''
        cnf,dictupdate=filtercnf(cnf,kw,'from_','to','values','textvar',
                                 fg='light gray',indicator='#cdcdcd',minpos=SW,maxpos=SE,increment=1,startpos=0,drawback=False,height='',var=None,exact=False,width=120,command=None,entrycnf={})
        self.__dict__.update(dictupdate)
        Canvas.__init__(self,master,cnf,bd=0,highlightthickness=0,width=self.width)
        if 'values' in dictupdate:
            if type(self.values)!=list: self.values=[str(val) for val in self.values]
        elif 'from_' in dictupdate and 'to' in dictupdate: self.values=[str(val) for val in range(self.from_,self.to+1,self.increment)]
        else: self.values=[''] #config
        self.len=len(self.values)-1 #config
        self.angles={S:0,SW:pi/4,W:pi/2,NW:3*pi/4,N:pi,NE:5*pi/4,E:3*pi/2,SE:7*pi/4} #constants
        self.min,self.max=self.angles[self.minpos],self.angles[self.maxpos] #config
        self.diff=self.max-self.min #config - after min,max
        self.startangle=self.angle=self.min+self.startpos*self.diff #config - after diff
        self.width=self.winfo_width() #adopt
        self.c=self.width/2 #adopt - after width
        self.groundpos=[self.c,self.width,.48*self.width,.96*self.width,.48*self.width,.76*self.width,.52*self.width,.76*self.width,.52*self.width,.96*self.width] #adopt - after c
        self.writing=False #modes

        self.create_oval(0,0,1,1,fill='black',outline='black',tags=('shadow','widget'))
        self.create_oval(0,0,1,1,fill=self.fg,outline=self.fg,tags=('circle','widget'))
        self.create_polygon(0,0,fill=self.indicator,outline=self.indicator,tags=('indicator','widget'))
        self.display=Entry(self,self.entrycnf,bd=1,validate='focusout',vcmd=(self.register(self.callback),'%P'),textvar=self.textvar if 'textvar' in dictupdate else '',justify=CENTER,invcmd=self.bell,font=('Segoe UI',round(.075*self.width)))
        self.value=self.values[int(round(self.startpos*self.len))]
        self.display.insert(0,self.value)
        self.create_window(0,0,window=self.display,anchor=NW,tags=('display','widget'))
        if self.var is not None: var.set(self.startpos)

        self.bind('<Configure>',self.adopt)
        self.bind('<Button-1>',self.click)
        self.bind('<Button1-Motion>',self.motion)
        self.bind('<ButtonRelease-1>',self.release)
        self.display.bind('<Return>',self.callback)
    def callback(self,value=None):
        if not isinstance(value,str):
            value=self.display.get()
            self.master.focus()
        if value in self.values:
            if self.var is not None: var.set(self.values.index(value)/self.len)
            if self.command is not None:
                try: self.command(value)
                except TypeError: self.command()
            self.angle=self.min+self.diff*self.values.index(value)/self.len
            self.coords('indicator',*rotate(self.groundpos,self.c,self.c,self.angle))
            self.value=value
            return True
        else:
            self.display.delete(0,END)
            self.display.insert(0,self.value)
            return False
    def adopt(self,event=None):
        width=self.winfo_width()
        if width==self.width: return
        self.width,self.c=width,width/2
        self.groundpos=[self.c,self.width,.48*self.width,.96*self.width,.48*self.width,.76*self.width,.52*self.width,.76*self.width,.52*self.width,.96*self.width]
        self.coords('circle',0,0,width,width)
        self.coords('shadow',0,.017*width,width,1.017*width)
        self.coords('indicator',*rotate(self.groundpos,self.angle,self.c,self.c))
        self.coords('display',width/5,1.059*width)
        self.itemconfig('display',width=.6*width,anchor=NW)
        self.display.config(font=('Segoe UI',round(.075*self.width)))
    def click(self,event):
        if event.widget!=self.display: self.master.focus()
        self.motion(event)
    def motion(self,event):
        dx,dy=event.x-self.c,event.y-self.c
        self.angle=acos(dy/(dx**2+dy**2)**.5)
        if event.x>self.c: self.angle=2*pi-self.angle
        if self.angle<self.min: self.angle=self.min
        elif self.angle>self.max: self.angle=self.max
        self.coords('indicator',*rotate(self.groundpos,self.angle,self.c,self.c))
        self.display.delete(0,END)
        self.value=self.values[int(round(self.len*(self.angle-self.min)/self.diff))]
        self.display.insert(0,self.value)
        if self.exact: self.callback(self.value)
        if self.var is not None: var.set((self.angle-self.min)/self.diff)
        if self.command is not None:
            try: self.command(self.value)
            except TypeError: self.command()
    def release(self,event):
        if not self.drawback: return
        self.coords('indicator',*rotate(self.groundpos,self.c,self.c,self.startangle))
        self.display.delete(0,END)
        self.value=self.values[int(round(self.startpos*self.len))]
        self.display.insert(0,self.value)
        if self.exact: self.callback(self.value)
        self.angle=self.startangle
        if self.var is not None: var.set(self.startpos)
        if self.command is not None:
            try: self.command(self.value)
            except TypeError: self.command()
    def get(self):
        return self.display.get()
    def set(self,value):
        self.display.delete(0,END)
        self.display.insert(0,value)
    def pack_configure(self,cnf={},**kw):
        '''Pack a widget in the parent widget. Use as options:
        after=widget - pack it after you have packed widget
        anchor=NSEW (or subset) - position widget according to
                                  given direction
        before=widget - pack it before you will pack widget
        expand=bool - expand widget if parent size grows
        fill=NONE or X or Y or BOTH - fill widget if widget grows
        in=master - use master to contain this widget
        in_=master - see 'in' option description
        ipadx=amount - add internal padding in x direction
        ipady=amount - add internal padding in y direction
        padx=amount - add padding in x direction
        pady=amount - add padding in y direction
        side=TOP or BOTTOM or LEFT or RIGHT -  where to add this widget.'''
        super().pack(cnf,**kw)
        self.update()
        self.adopt()
        if self.height == '': super().config(height=self.bbox('widget')[3]+.042*self.width)
    pack=pack_configure
    def grid_configure(self,cnf={},**kw):
        '''Position a widget in the parent widget in a grid. Use as options:
        column=number - use cell identified with given column (starting with 0)
        columnspan=number - this widget will span several columns
        in=master - use master to contain this widget
        in_=master - see 'in' option description
        ipadx=amount - add internal padding in x direction
        ipady=amount - add internal padding in y direction
        padx=amount - add padding in x direction
        pady=amount - add padding in y direction
        row=number - use cell identified with given row (starting with 0)
        rowspan=number - this widget will span several rows
        sticky=NSEW - if cell is larger on which sides will this
                      widget stick to the cell boundary'''
        super().grid(cnf,**kw)
        self.update()
        self.adopt()
        if self.height == '': super().config(height=self.bbox('widget')[3]-1+.042*self.width)
    grid=grid_configure
    def config(self,cnf={},**kw):
        '''Configure resources of a widget.

        The values for resources are specified as keyword
        arguments. To get an overview about
        the allowed keyword arguments call the method keys.'''
        cnf,dictupdate=filtercnf(cnf,kw,'from_','to','values','textvar','fg','indicator','minpos','maxpos','increment','startpos','drawback','var','exact','command','entrycnf')
        super().config(cnf)
        self.__dict__.update(dictupdate)
        if 'values' in dictupdate:
            if type(self.values)!=list:
                self.values=[str(val) for val in self.values]
                self.len=len(self.values)-1
        elif 'from_' in dictupdate or 'to' in dictupdate or 'increment' in dictupdate:
            self.values=[str(val) for val in range(self.from_,self.to+1,self.increment)]
            self.len=len(self.values)-1
        if 'min' in dictupdate: self.min=self.angles[self.minpos]
        if 'max' in dictupdate: self.max=self.angles[self.maxpos]
        if 'min' or 'max' in dictupdate: self.diff=self.max-self.min
        self.startangle=self.angle=self.min+self.startpos*self.diff
        if 'fg' in dictupdate: self.itemconfig('circle',fill=self.fg,outline=self.fg)
        if 'indicator' in dictupdate: self.itemconfig('indicator',fill=self.indicator,outline=self.indicator)
        if 'textvar' in dictupdate: self.display.config(textvar=self.textvar)
        if 'entrycnf' in dictupdate: self.display.config(cnf)
    configure=config
    def cget(self,key):
        'Return the resource value for a KEY given as string.'
        if key in ['from_','to','values','textvar','fg','indicator','minpos','maxpos','increment','startpos','drawback','var','exact','command','entrycnf']: return self.__dict__[key]
        else: super().cget(key)
    __getitem__=cget
    def keys(self):
        'Return a list of all resource names of this widget.'
        return super().keys()+['from_','to','values','textvar','fg','indicator','minpos','maxpos','increment','startpos','drawback','var','exact','command','entrycnf']

def negative(master,color):
    return '#%02x%02x%02x'%tuple(map(int,[255,255,255]-(array(master.winfo_rgb(color))>>8)))

class Store:
    def __init__(self,**kw): self.__dict__.update(kw)

class Debug:
    def __init__(self,prgname,directory,live=False):
        self.c=1
        self.live=live
        self.filename=directory+'/{name}-{now.day}_{now.month}_{now.year}-{now.hour}_{now.minute}_{now.second}.log'.format(now=datetime.now(),name=prgname)
        with open(self.filename,'w+') as file: file.write(prgname+'-log from {now.day}.{now.month}.{now.year}\n\n'.format(now=datetime.now()))
    def log(self,**values):
        items=tuple(values.items())
        if len(items)==0: return
        text='{}: {}={}'.format(str(self.c).zfill(5),items[0][0],items[0][1])
        for varname,value in items[1:]: text+='; {}={}'.format(varname,value)
        with open(self.filename,'a') as file: file.write(text+'\n')
        if self.live: print('debug',text)
        self.c+=1

class CustomButton(Canvas):
    _REMOVE=('closeenough','confine','insertbackground','insertborderwidth','insertofftime','insertontime','insertwidth','offset','scrollregion',
             'selectbackground','selectborderwidth','selectforeground','xscrollcommand','xscrollincrement','yscrollcommand','yscrollincrement')
    _PASS=('background','bd','bg','borderwidth','cursor','height','highlightbackground','highlightcolor','highlightthickness','relief','state',
           'takefocus','width')
    _EXTRA=('args','kwargs','form','activecolor','color','ipadx','ipady','irelheight','irelwidth','ratio','anchor','activerelief','movewidth',
            'activebackground','command','overrelief','repeatdelay','repeatinterval','disabledcolor')
    
    CROSS=(10,0,25,15,40,0,50,10,35,25,50,40,40,50,25,35,10,50,0,40,15,25,0,10)
    CIRCLE=(20.0,10.0,19.88,11.56,19.51,13.09,18.91,14.54,18.09,15.88,17.07,17.07,15.88,18.09,14.54,18.91,13.09,19.51,11.56,19.88,10.0,20.0,8.44,
            19.88,6.91,19.51,5.46,18.91,4.12,18.09,2.93,17.07,1.91,15.88,1.09,14.54,0.49,13.09,0.12,11.56,0.0,10.0,0.12,8.44,0.49,6.91,1.09,5.46,
            1.91,4.12,2.93,2.93,4.12,1.91,5.46,1.09,6.91,0.49,8.44,0.12,10.0,0.0,11.56,0.12,13.09,0.49,14.54,1.09,15.88,1.91,17.07,2.93,18.09,4.12,
            18.91,5.46,19.51,6.91,19.88,8.44)
    ARROW_LEFT=(0,20,30,2.68,30,37.32)
    ARROW_RIGHT=(0,2.68,30,20,0,37.32)
    ARROW_UP=(20,0,37.32,30,2.68,30)
    ARROW_DOWN=(20,30,2.68,0,37.32,0)
    PLUS=(0,22,22,22,22,0,37,0,37,22,59,22,59,37,37,37,37,59,22,59,22,37,0,37)
    def __init__(self,master=None,cnf={},**kw):
        cnf,dictupdate=filtercnf(cnf,kw,activebackground='SystemButtonFace',command=None,overrelief=None,
                                 repeatdelay=0,repeatinterval=0,#from button
                                 form=None,args=(),kwargs={},ipadx=0,ipady=0,irelheight=1,irelwidth=1,ratio=None,anchor=CENTER,activerelief=SUNKEN,
                                 activecolor='SystemButtonText',color='SystemButtonText',disabledcolor='SystemDisabledText',movewidth=None) #extra
        if 'relief' not in cnf: cnf['relief']=self.relief=RAISED
        else: self.relief=cnf['relief']
        if 'bd' not in cnf and 'borderwidth' not in cnf: cnf['bd']=2
        Canvas.__init__(self,master,cnf)
        self.state=super().cget('state')
        self.bg=super().cget('bg')
        self._cleancnf(cnf)
        self.__dict__.update(dictupdate)
        if self.movewidth is None: self.movewidth=int(super().cget('bd'))

        self._ispressed=False
        self._adopting=False
        self._form=Store()
        
        self.create_polygon([0,0,0,0],tag='form',width=0)
        self._changeform()
        self._configform()

        self.bind('<ButtonPress-1>',self._press,ADD)
        self.bind('<ButtonRelease-1>',self._release,ADD)
        self.bind('<Enter>',self._enter,ADD)
        self.bind('<Leave>',self._leave,ADD)
        self.bind('<Configure>',self._adopt,ADD)
    def _cleancnf(self,cnf):
        for key in self._REMOVE: cnf.pop(key,None)
    def _commandloop(self):
        if not self._ispressed: return
        if self.command: self.command(*self.args,**self.kwargs)
        if self.repeatinterval>0: self.after(self.repeatinterval,self._commandloop)
    def _press(self,event):
        if self.state!=DISABLED:
            self._ispressed=True
            super().config(relief=self.activerelief,bg=self.activebackground)
            if self.movewidth: self.move('form',self.movewidth,self.movewidth)
            self._configform()
            self.update()
            if self.command: self.command(*self.args,**self.kwargs)
            if self.repeatinterval>0: self.after(self.repeatdelay,self._commandloop)
            return 'break'
    def _release(self,event):
        if self._ispressed:
            self._ispressed=False
            if self.movewidth: self.move('form',-self.movewidth,-self.movewidth)
            super().config(relief=self.relief,bg=self.bg)
            if self.state==DISABLED:
                self.state=NORMAL
                self._configform()
                self.state=DISABLED
            else: self._configform()
            self.update()
    def _enter(self,event):
        if self.overrelief: super().config(relief=self.overrelief)
    def _leave(self,event):
        if super().cget('relief')!=self.relief: super().config(relief=self.relief)
    def _changeform(self,event=None):
        if not self.form: return
        x,y=array(self.form[::2]),array(self.form[1::2])
        if self.ratio:
            self._form.width,self._form.height=max(y)*self.ratio,max(y)
            self._form.ratio=self.ratio
            self._form.x=self.ratio*(x-min(x))
            self._form.y=y-min(y)
        else:
            self._form.width,self._form.height=max(x),max(y)
            self._form.ratio=self._form.width/self._form.height
            self._form.x=x-min(x)
            self._form.y=y-min(y)
    def _configform(self):
        if self.state==DISABLED: self.itemconfig('form',fill=self.disabledcolor)
        elif self._ispressed: self.itemconfig('form',fill=self.activecolor)
        else: self.itemconfig('form',fill=self.color)
    def _adopt(self,event=None):
        if not self.form: return
        if not self._adopting:
            self._adopting=True
            border=int(super().cget('bd'))+int(super().cget('highlightthickness'))
            canvaswidth,canvasheight=self.winfo_width(),self.winfo_height()
            xoff,yoff=self.ipadx+(1-self.irelwidth)*canvaswidth/2,self.ipady+(1-self.irelheight)*canvasheight/2
            width,height=self.irelwidth*(canvaswidth-2*(border+self.ipadx)),self.irelheight*(canvasheight-2*(border+self.ipady))
            if self.ratio is not False:
                displayratio=width/height
                if(displayratio>=1 and self._form.ratio<=displayratio) or (displayratio<1 and self._form.ratio<=displayratio):
                    ratio=height/self._form.height
                    xoff+=(width-ratio*self._form.width)/2
                elif (displayratio>=1 and self._form.ratio>=displayratio) or (displayratio<1 and self._form.ratio>=displayratio):
                    ratio=width/self._form.width
                    yoff+=(height-ratio*self._form.height)/2
                x,y=ratio*self._form.x+border,ratio*self._form.y+border
            else: x,y=border+width*self._form.x/self._form.width,border+height*self._form.y/self._form.height
            if self.anchor==CENTER:
                x+=xoff
                y+=yoff
            else:
                if S in self.anchor:
                    y+=2*yoff
                if E in self.anchor:
                    x+=2*xoff
            self.coords('form',[x[i//2] if i%2==0 else y[i//2] for i in range(2*len(x))])
            self.update_idletasks()
            self._adopting=False
    #
    def pack(self,cnf={},**kw):
        super().pack(cnf,**kw)
        self.update()
        self._adopt()
    pack_configure=pack
    def grid(self,cnf={},**kw):
        super().grid(cnf,**kw)
        self.update()
        self._adopt()
    grid_configure=grid
    def place(self,cnf={},**kw):
        super().place(cnf,**kw)
        self.update()
        self._adopt()
    place_configure=place
    #
    def config(self,cnf=None,**kw):
        cnf,dictupdate=filtercnf(cnf,kw,*self._EXTRA,'relief')
        self._cleancnf(cnf)
        self.__dict__.update(dictupdate)
        cnf['relief']=self.relief
        if 'state' in cnf:
            self.state=cnf['state']
            self._configform()
        if 'form' in dictupdate or 'ipadx' in dictupdate or 'ipadx' in dictupdate or 'irelheight' in dictupdate or 'irelwidth': self._changeform()
        if 'color' in dictupdate or 'activecolor' in dictupdate or 'disabledcolor' in dictupdate: self._configform()
        if 'ratio' in dictupdate or 'anchor' in dictupdate:
            self._changeform()
            self._adopt()
        super().config(cnf)
        if self.movewidth is None: self.movewidth=int(super().cget('bd'))
    configure=config
    def cget(self,key):
        if key in self._EXTRA: return getattr(self,key)
        else: return super().cget(key)
    __getitem__=cget
    def keys(self):
        return self._EXTRA+self._PASS

class CustomScrollbar(Frame):
    _KEYWORDS=['activebackground', 'command', 'elementborderwidth', 'jump', 'orient', 'repeatdelay', 'repeatinterval', 'troughcolor', 'bg', 'width',
               'activelementrelief','elementrelief','fg','activeforeground','disabledforeground','cursor','length','state','slidercolor']
    _FRAME=['bd', 'borderwidth', 'relief', 'cursor', 'highlightbackground', 'highlightcolor', 'highlightthickness', 'takefocus']
    _REMOVE=['class', 'colormap', 'container', 'padx', 'pady', 'visual']

    _UP=[12.0, 9.0, 6.0, 4.0, 0.0, 9.0, 0.0, 5.0, 6.0, 0.0, 12.0, 5.0]
    _DOWN=[0, 0, 6, 5, 12, 0, 12, 4, 6, 9, 0, 4]
    _LEFT=[10.5, -1.5, 5.5, 4.5, 10.5, 10.5, 6.5, 10.5, 1.5, 4.5, 6.5, -1.5]
    _RIGHT=[1.5, 10.5, 6.5, 4.5, 1.5, -1.5, 5.5, -1.5, 10.5, 4.5, 5.5, 10.5]
    def __init__(self,master=None,cnf={},**kw):
        cnf,dictupdate=filtercnf(cnf,kw,activebackground='#606060',command=None,elementborderwidth=0,jump=False,orient=VERTICAL,repeatdelay=300,repeatinterval=100,
                                 troughcolor='SystemButtonFace',bg='SystemButtonFace',width=26,activeelementrelief=FLAT,elementrelief=RAISED,fg='#606060',
                                 activeforeground='SystemButtonFace',disabledforeground='#606060',cursor='arrow',length=60,state=NORMAL,slidercolor='SystemScrollbar')
        self._cleancnf(cnf)
        Frame.__init__(self,master,cnf,bg='green')
        self.pack_propagate(False)
        self.__dict__.update(dictupdate)

        self._button1=CustomButton(self,activecolor=self.activeforeground,color=self.fg,activerelief=self.activeelementrelief,movewidth=self.elementborderwidth,
                                   activebackground=self.activebackground,command=self._buttoncmd,repeatdelay=self.repeatdelay,irelwidth=10/26,irelheight=9/26,
                                   repeatinterval=self.repeatinterval,bg=self.bg,bd=self.elementborderwidth,cursor=self.cursor,height=26,highlightthickness=0,
                                   relief=self.elementrelief,width=26,ratio=False,args=('-1',),disabledcolor=self.disabledforeground,state=self.state)
        self._button2=CustomButton(self,activecolor=self.activeforeground,color=self.fg,activerelief=self.activeelementrelief,movewidth=self.elementborderwidth,
                                   activebackground=self.activebackground,command=self._buttoncmd,repeatdelay=self.repeatdelay,irelwidth=10/26,irelheight=9/26,
                                   repeatinterval=self.repeatinterval,bg=self.bg,bd=self.elementborderwidth,cursor=self.cursor,height=26,highlightthickness=0,
                                   relief=self.elementrelief,width=26,ratio=False,args=('1',),disabledcolor=self.disabledforeground,state=self.state)
        self._trough=Frame(self,bg=self.troughcolor,cursor=self.cursor)
        self._slider=Frame(self._trough,relief=self.elementrelief,bd=self.elementborderwidth,cursor=self.cursor,bg=self.slidercolor)

        self._moving=False
        self._relpos,self._length=0.0,1.0
        self._build()
        
        self._trough.bind('<Button-1>',self._clicktrough,ADD)
        self._trough.bind('<MouseWheel>',self._scroll,ADD)
        self._trough.bind('<Shift-MouseWheel>',self._scroll,ADD)
        self._slider.bind('<MouseWheel>',self._scroll,ADD)
        self._slider.bind('<Shift-MouseWheel>',self._scroll,ADD)
        self._slider.bind('<ButtonPress-1>',self._pressslider,ADD)
        self._slider.bind('<Button1-Motion>',self._moveslider,ADD)
        self._slider.bind('<ButtonRelease-1>',self._releaseslider,ADD)
    def _cleancnf(self,cnf):
        for key in self._REMOVE: cnf.pop(key,None)
    def _build(self):
        self._button1.pack_forget()
        self._button2.pack_forget()
        self._trough.pack_forget()
        self._slider.place_forget()
        if self.orient==VERTICAL:
            super().config(height=self.length,width=self.width)
            self._button1.config(form=self._UP)
            self._button2.config(form=self._DOWN)
            self._button1.pack(side=TOP,fill=X)#,expand=True)
            self._button2.pack(side=BOTTOM,fill=X)#,expand=True)
            self._trough.pack(side=BOTTOM,fill=BOTH,expand=True)
            self._slider.place(relwidth=1,x=0)
        else:
            super().config(width=self.length,height=self.width)
            self._button1.config(form=self._LEFT)
            self._button2.config(form=self._RIGHT)
            self._button1.pack(side=LEFT,fill=Y)#,expand=True)
            self._button2.pack(side=RIGHT,fill=Y)#,expand=True)
            self._trough.pack(side=RIGHT,fill=BOTH,expand=True)
            self._slider.place(relheight=1,y=0)
        self.set()
    def _buttoncmd(self,direction):
        if self.state==DISABLED or not self._active or not self.command: return
        self.command('scroll',direction,'units')
    def _clicktrough(self,event): #'scroll' '1'/'-1' 'pages'
        if self.state==DISABLED or not self._active or not self.command: return
        if self.orient==VERTICAL: direction='-1' if event.y<self._slider.winfo_y() else '1'
        else: direction='-1' if event.x<self._slider.winfo_x() else '1'
        self.command('scroll',direction,'pages')
    def _scroll(self,event): #delta/-30
        if (event.state==0 and self.orient==HORIZONTAL) or (event.state==1 and self.orient==VERTICAL) or self.state==DISABLED or not self._active or not self.command: return
        self.command('scroll',str(int(event.delta/-30)),'units')
    def _pressslider(self,event):
        if self.state==DISABLED or not self._active or not self.command: return
        self._moving=True
        if self.orient==VERTICAL:
            self._now=event.y
            self._step=1/(self._trough.winfo_height()-self._length)
        else:
            self._now=event.x
            self._step=1/(self._trough.winfo_width()-self._length)
        self._max=1-self._length
    def _moveslider(self,event): #'moveto' '<0 bis 1>'
        if not self._moving: return
        if self.orient==VERTICAL: self._relpos+=self._step*(event.y-self._now)
        else: self._relpos+=self._step*(event.x-self._now)
        if self._relpos<0: self._relpos=0.0
        elif self._relpos>self._max: self._relpos=self._max
        if not self.jump:
            if self.orient==VERTICAL: self._slider.place(rely=self._relpos)
            else: self._slider.place(relx=self._relpos)
        self.command('moveto',str(self._relpos))
    def _releaseslider(self,event):
        self._moving=False
        if not self.state==DISABLED and self._active: self.set()
    def set(self,first=None,last=None):
        if self.state==DISABLED: return
        if first is not None and last is not None: self._relpos,self._length=float(first),round(float(last)-float(first),15)
        if self._moving: return
        if self._length>=1:
            self._active=False
            self._slider.place_forget()
            return
        elif self.orient==VERTICAL:
            self._slider.place(rely=self._relpos,relheight=self._length,relwidth=1)
            if not self._active: self._active=True
        else:
            self._slider.place(relx=self._relpos,relwidth=self._length,relheight=1)
            if not self._active: self._active=True
        if self._relpos<=0: self._button1.config(state=DISABLED)
        elif 1-self._length<=self._relpos: self._button2.config(state=DISABLED)
        else:
            if self._button1.cget('state')==DISABLED: self._button1.config(state=NORMAL)
            if self._button2.cget('state')==DISABLED: self._button2.config(state=NORMAL)
    def config(self,cnf=None,**kw):
        cnf,dictupdate=filtercnf(cnf,kw,*self._KEYWORDS)
        self._cleancnf(cnf)
        super().config(cnf)
        self.__dict__.update(dictupdate)
        if 'activeforeground' in dictupdate or 'fg' in dictupdate or 'activeelementrelief' in dictupdate or 'activebackground' in dictupdate or \
            'repeatdelay'  in dictupdate or 'repeatinterval' in dictupdate or 'bg' in dictupdate or 'disabledforeground' in dictupdate:
            self._button1.config(activecolor=self.activeforeground,color=self.fg,activerelief=self.activeelementrelief,activebackground=self.activebackground,
                                 repeatdelay=self.repeatdelay,repeatinterval=self.repeatinterval,bg=self.bg,disabledcolor=self.disabledforeground)
            self._button2.config(activecolor=self.activeforeground,color=self.fg,activerelief=self.activeelementrelief,activebackground=self.activebackground,
                                 repeatdelay=self.repeatdelay,repeatinterval=self.repeatinterval,bg=self.bg,disabledcolor=self.disabledforeground)
        if 'troughcolor' in dictupdate:
            self._trough.config(bg=self.troughcolor)
        if 'slidercolor' in dictupdate:
            self._slider.config(bg=self.slidercolor)
        if 'cursor' in dictupdate:
            self._button1.config(cursor=self.cursor)
            self._button2.config(cursor=self.cursor)
            self._slider.config(cursor=self.cursor)
            self._trough.config(cursor=self.cursor)
        if 'elementborderwidth' in dictupdate:
            self._slider.config(bd=self.elementborderwidth)
            self._button1.config(bd=self.elementborderwidth,movewidth=self.elementboderwidth)
            self._button2.config(bd=self.elementborderwidth,movewidth=self.elementboderwidth)
        if 'orient' in dictupdate:
            self._build()
        elif 'length' in dictupdate or 'width' in dictupdate:
            if self.orient==VERTICAL: super().config(height=self.length,width=self.width)
            else: super().config(width=self.length,height=self.width)
        if 'state' in dictupdate:
            self._button1.config(state=self.state)
            self._button2.config(state=self.state)
            if self.state==DISABLED: self._slider.place_forget()
            else: self.set()
    configure=config
    def cget(self,key):
        if key in self._KEYWORDS: return getitem(self,key)
        else: super().cget(key)
    __getitem__=cget
    def keys(self):
        return self._KEYWORDS+self._FRAME

class HyperlinkManager:
    def __init__(self,text,foreground='blue'):
        self.text=text
        self.text.tag_config('hyper', foreground=foreground, underline=1)
        self.text.tag_bind('hyper', '<Enter>', self._enter)
        self.text.tag_bind('hyper', '<Leave>', self._leave)
        self.text.tag_bind('hyper', '<Button-1>', self._click)

        self.links={}
    def reset(self):
        self.links={}
    def add(self,action):
        tag = 'hyper-%d' % len(self.links)
        self.links[tag] = action
        return 'hyper', tag
    def _enter(self,event):
        self._insertwidth=self.text.cget('insertwidth')
        self.text.config(cursor='hand2',insertwidth=0)
    def _leave(self,event):
        self.text.config(cursor='',insertwidth=self._insertwidth)
        tag=self._getcwt()
        if tag: self.text.mark_set(INSERT,self.text.index(tag+'.last'))
    def _getcwt(self): #yes this is a reference to os.getcwd and means get current "working" tag
        for tag in self.text.tag_names(CURRENT):
            if tag.startswith('hyper-'): return tag
    def _click(self,event):
        tag=self._getcwt()
        if tag: self.links[tag]()

class DebugArrow(Toplevel):
    top=(50,0,100,50,100,60,55,15,55,180,45,180,45,15,0,60,0,50)
    right=(140.0, 90.0, 90.0, 140.0, 80.0, 140.0, 125.0, 95.0, -40.0, 95.0, -40.0, 85.0, 125.0, 85.0, 80.0, 40.0, 90.0, 40.0)
    bottom=(50, 180.0, 7, 130.0, 7, 120.0, 45, 165.0, 44, 0.0, 54, 0.0, 55, 165.0, 100.0, 120.0, 100.0, 130.0)
    left=(-40.0, 90.0, 10.0, 40.0, 20, 40.0, -25.0, 85.0, 140.0, 85.0, 140.0, 95.0, -25.0, 95.0, 20, 140.0, 10.0, 140.0)
    def __init__(self,master=None,color='SystemHighlight',side=TOP,topmost=True):
        Toplevel.__init__(self,master)
        ban=negative(self,color)
        c=Canvas(self,highlightthickness=0,bg=ban)
        c.pack(fill=BOTH,expand=True)
        c.create_polygon(getattr(self,side),width=0,fill=color)
        c.tag_bind(1,'<Button-1>',self.destroy)
        self.attributes('-transparentcolor',ban)
        self.attributes('-topmost',topmost)
        self.overrideredirect(True)
        self.place(-1000,-1000)
    def place(self,x,y):
        self.geometry(f'+{x-50}+{y}')
    def destroy(self,event=None):
        super().destroy()

class CustomNotebook(Frame):
    _ARGS=('bd', 'borderwidth', 'relief', 'background', 'bg', 'height', 'width')
    _EXTRAS=('deletecommand', 'tabbackground', 'radius', 'addcommand', 'tabheight', 'dynamictabheight', 'jumptreshold', 'addbuttoncnf', 'padx', 'tabcycle',
             'changecommand')
    _TABARGS=('text', 'background', 'bg', 'activebackground', 'foreground', 'fg', 'activeforeground', 'width', 'wraplength', 'takefocus', 'image', 'bitmap',
              'font', 'compound', 'containerbackground')
    def __init__(self,master=None,cnf={},**kw):
        cnf,dictupdate=filtercnf(cnf,kw,deletecommand=None,tabbackground='white',radius=10,addcommand=None,tabheight=40,dynamictabheight=True,
                                 addbuttoncnf={},jumptreshold=.5,padx=10,tabcycle=True,changecommand=None)
        self._checkcnf(cnf,self._ARGS)
        Frame.__init__(self,master,cnf)
        self.__dict__.update(dictupdate)

        self.tabsection=Frame(self,bg=self.tabbackground,height=self.tabheight,padx=self.padx)
        self.tabsection.pack(side=TOP,fill=X)
        self.tabsection.update()
        self.tabsection.pack_propagate(self.dynamictabheight)
        cnf,predev=filtercnf(self.addbuttoncnf,None,form=CustomButton.PLUS,activecolor='SystemHighlight',ipady=5,movewidth=1,
                                activebackground=self.tabbackground,bg=self.tabbackground,bd=0,takefocus=False,highlightthickness=0,
                                irelheight=.6,irelwidth=.6)
        cnf.update(predev)
        self.addbutton=CustomButton(self.tabsection,cnf,ratio=False,height=self.tabheight,width=self.tabheight,command=self.addcommand)
        if self.addcommand:
            self.addbutton.pack(side=LEFT,fill=Y)
        self.ghost=Frame(self.tabsection,bg=self.tabbackground)

        self._tags={}
        self._tagcounter=0
        self._focused=None
        self._grabbed=None

        self._tl=self.winfo_toplevel()
        self._tl.bind('<Button-1>',self._select,ADD)
        self._tl.bind('<Button1-Motion>',self._drag,ADD)
        self._tl.bind('<ButtonRelease>',self._drop,ADD)
        if self.tabcycle:
            self._next=self._tl.bind('<Control-Tab>',self.next,ADD)
            self._previous=self._tl.bind('<Control-Shift-Tab>',self.previous,ADD)
        else: self._next=self._previous=''

        self.mouse=Controller()
    def _checkcnf(self,cnf,valid):
        for key in cnf:
            if key not in valid: raise TclError('unknown option "-%s"'%key)
    def _select(self,arg):
        slaves=self.order
        if isinstance(arg,Event) and arg.widget.master in slaves:
            self._focus(arg.widget.master,False)
            self._grab(arg.widget.master)
        elif arg in slaves:
            self._focus(arg)
    def _drag(self,event):
        pointerover=pointer_over(self.tabsection,bottom=40)
        if self._grabbed and self._dx and self._focused==self._grabbed and not self._focused.windowed:
            if pointerover:
                newx,max=self.winfo_pointerx()-self.tabsection.winfo_rootx()-self._dx,self.tabsection.winfo_width()-self._focused.winfo_width()-self.padx
                if newx<self.padx: newx=self.radius
                elif newx>max: newx=max
                diff=newx-self._focused.winfo_x()
                self._focused.place(x=newx)
                slaves=self.order.copy()
                ghostpos=slaves.index(self.ghost)
                if diff<0 and ghostpos>0:
                    before=slaves[ghostpos-1]
                    if newx<=before.winfo_x()+before.winfo_width()*(1-self.jumptreshold): self.ghost.pack(before=before)
                elif ghostpos<len(slaves)-1:
                    after=slaves[ghostpos+1]
                    if newx+self.ghost.winfo_width()>=after.winfo_x()+self.jumptreshold*after.winfo_width(): self.ghost.pack(after=after)
            else:
                self.dx=None
                self._free(self._focused)
    def _dragwindow(self,event):
        if self._grabbed and self._grabbed.toplevel==event.widget: tab=self._grabbed
        else: return
        x,y=tab.toplevel.winfo_rootx(),tab.toplevel.winfo_rooty()
        offset=self.tabsection.winfo_height()
        if tab.windowed and (tab.lastx!=x or tab.lasty!=y) and pointer_over(self.tabsection):
            tab.lastx,tab.lasty=x,y
            self._lock(self._grabbed)
        elif tab.windowed and (tab.lastx!=x or tab.lasty!=y) and pointer_over(self.tabsection,top=offset,bottom=offset):
            tab.lastx,tab.lasty=x,y
            if self.ghost.winfo_ismapped(): self._moveprelock()
            else: self._prelock(tab)
        elif tab.windowed and (tab.lastx!=x or tab.lasty!=y) and self.ghost.winfo_ismapped():
            tab.lastx,tab.lasty=x,y
            self.ghost.pack_forget()
    def _drop(self,event):
        if self._grabbed and self._dx is not None and not self._grabbed.windowed and self._focused==self._grabbed:
            try: self._focused.pack(side=LEFT,fill=Y,before=self.ghost)
            except TclError: return
            self.ghost.pack_forget()
            self._grabbed,self._dx=None,None
    def _prelock(self,tab):
        x=self.winfo_pointerx()-self.tabsection.winfo_rootx()
        self.ghost.config(width=tab.winfo_width())
        for widget in self.order.copy():
            widgetx,widgetwidth=widget.winfo_x(),widget.winfo_width()
            if widgetx<=x<=widgetx+widgetwidth:
                if x<=widgetx+widgetwidth//2: self.ghost.pack(side=LEFT,before=widget)
                else: self.ghost.pack(side=LEFT,after=widget)
                break
        else:
            if self.addcommand: self.ghost.pack(side=LEFT,before=self.addbutton)
            else: self.ghost.pack(side=LEFT)
    def _moveprelock(self):
        newx,max=self.winfo_pointerx()-self.tabsection.winfo_rootx()-self._dx,self.tabsection.winfo_width()-self._focused.winfo_width()-self.padx
        if newx<self.padx: newx=self.radius
        elif newx>max: newx=max
        diff=newx-self._focused.winfo_x()
        slaves=self.order.copy()
        ghostpos=slaves.index(self.ghost)
        if diff<0 and ghostpos>0:
            before=slaves[ghostpos-1]
            if newx<=before.winfo_x()+before.winfo_width()*(1-self.jumptreshold): self.ghost.pack(before=before)
        elif ghostpos<len(slaves)-1:
            after=slaves[ghostpos+1]
            if newx+self.ghost.winfo_width()>=after.winfo_x()+self.jumptreshold*after.winfo_width(): self.ghost.pack(after=after)
    def _focus(self,tab,setactive=True):
        if self._focused!=tab:
            if self._focused:
                self._focused.left.grid_forget()
                self._focused.right.grid_forget()
                self._focused.label.config(state=NORMAL)
                self._focused.close.config(bg=self._focused.normalcolor,activebackground=self._focused.normalcolor)
                self._focused.container.pack_forget()
            self._focused=tab
            tab.left.grid(row=0,column=0,sticky=NS)
            tab.right.grid(row=0,column=3,sticky=NS)
            tab.label.config(state=ACTIVE)
            tab.close.config(bg=tab.activecolor,activebackground=tab.activecolor)
            tab.container.pack(side=BOTTOM,fill=BOTH,expand=True)
            tab.update()
            if setactive and self.changecommand: self.changecommand(tab)
    def _grab(self,tab):
        tab.update()
        x=tab.winfo_x()
        self._dx=self.winfo_pointerx()-tab.winfo_rootx()
        self.ghost.config(width=tab.winfo_width())
        self.ghost.pack(after=tab,side=LEFT)
        tab.place(x=x,y=0,bordermode=OUTSIDE)
        tab.update()
        self._grabbed=tab
        tab.lift()
        if self.changecommand: self.changecommand(tab)
    def _free(self,tab):
        tab.toplevel.config(use='')
        tab.windowed=True
        self._searchfocus(self.ghost,False)
        self.ghost.pack_forget()
        tab.place_forget()
        tab.update()
        x,y=self.mouse.position
        width=tab.toplevel.winfo_width()
        self.mouse.release(ButtonType.left)
        tab.toplevel.geometry('+{x}+{y}'.format(x=x-width//3,y=y-22))
        self.mouse.press(ButtonType.left)
    def _lock(self,tab):
        tab.toplevel.config(use=tab.frameid)
        self.mouse.release(ButtonType.left)
        tab.windowed=False
        if self.ghost.winfo_ismapped():
            tab.pack(side=LEFT,fill=Y,after=self.ghost)
            self.ghost.pack_forget()
        else:
            x=self.winfo_pointerx()-self.tabsection.winfo_rootx()
            for widget in self.order.copy():
                widgetx,widgetwidth=widget.winfo_x(),widget.winfo_width()
                if widgetx<=x<=widgetx+widgetwidth:
                    if x<=widgetx+widgetwidth//2: tab.pack(side=LEFT,fill=Y,before=widget)
                    else: tab.pack(side=LEFT,fill=Y,after=widget)
                    break
            else:
                if self.addcommand: tab.pack(side=LEFT,fill=Y,before=self.addbutton)
                else: tab.pack(side=LEFT,fill=Y)
        self._focus(tab)
        tab.update()
    def _createcorners(self,tab):
        tab.update()
        height,d=tab.winfo_height(),2*self.radius
        tab.left.config(bg=tab.activecolor)
        tab.left.create_arc(-self.radius,height-d,self.radius,height,width=0,fill=self.tabbackground,outline=self.tabbackground,start=-90) #bottom
        tab.left.move(1,-1,0)
        tab.left.create_polygon(0,0,d,0,d,self.radius,self.radius,self.radius,self.radius,height-self.radius,0,height-self.radius,width=0,fill=self.tabbackground) #bg
        tab.left.create_arc(self.radius,0,self.radius+d,d,width=0,fill=tab.activecolor,outline=tab.activecolor,start=90) #top
        tab.right.config(bg=tab.activecolor)
        tab.right.create_arc(self.radius,height-d,d+self.radius,height,width=0,fill=self.tabbackground,outline=self.tabbackground,start=180) #bottom
        tab.right.create_polygon(0,0,d,0,d,height-self.radius,self.radius,height-self.radius,self.radius,self.radius,0,self.radius,width=1,fill=self.tabbackground) #bg
        tab.right.create_arc(-self.radius,0,self.radius,d,width=0,fill=tab.activecolor,outline=tab.activecolor) #top
        tab.right.move(3,-1,0)
    def _getTab(self,child):
        if isinstance(child,Widget) and child.master.master in self.tabsection.pack_slaves(): return child.master.master
        elif isinstance(child,str): return self._tags[child]
        elif isinstance(child,int): return self.order[child]
        else: raise TclError(f'can\'t resolve child "{child}"')
    def _searchfocus(self,from_,setactive=True):
        slaves=self.order.copy()
        pos,len_=slaves.index(from_),len(slaves)
        if len_==1: return
        elif pos==len_-1: self._focus(slaves[pos-1],setactive)
        else: self._focus(slaves[pos+1],setactive)
    def _remove(self,tab):
        if self._grabbed==tab: self._grabbed=None
        if self._focused==tab: self._searchfocus(tab)
        if self.deletecommand: self.deletecommand(tab)
        tab.toplevel.destroy()
        tab.container.destroy()
        tab.destroy()
    def _focussubwindow(self,event):
        tab=event.widget.master
        if tab.windowed and self._grabbed!=tab and self.changecommand: self.changecommand(tab)
    def next(self,cycle=False):
        slaves=self.order.copy()
        index=slaves.index(self._focused)
        if index==len(slaves)-1:
            if cycle: self._focus(slaves[0])
        else: self._focus(slaves[index+1])
    def previous(self,cycle=False):
        slaves=self.order.copy()
        index=slaves.index(self._focused)
        if index==0:
            if cycle: self._focus(slaves[-1])
        else: self._focus(slaves[index-1])
    def focus(self,child):
        self._focus(self._getTab(child))
    def add(self,cnf={},**kw):
        cnf=cnfmerge((cnf,kw))
        self._checkcnf(cnf,self._TABARGS)
        if 'width' not in cnf and 'text' not in cnf: cnf['width']=2
        if 'bg' not in cnf: cnf['bg']=self.tabbackground
        containerbackground=cnf.pop('containerbackground',cnf['activebackground'])
        tab=Frame(self.tabsection,bg=self.tabbackground)
        tab.columnconfigure((0,3),minsize=2*self.radius)
        tab.columnconfigure(1,weight=1)
        tab.rowconfigure(0,weight=1)
        tab.left=Canvas(tab,highlightthickness=0,width=2*self.radius)
        tab.label=Label(tab,cnf)
        tab.label.grid(row=0,column=1,sticky=NSEW)
        tab.close=CustomButton(tab,args=(tab,),form=CustomButton.CROSS,activecolor='red',irelwidth=.75,irelheight=.75,movewidth=1,command=self._remove,bd=0,
                               disabledcolor='SystemDisabledText',cursor='hand2',height=2*self.radius,width=2*self.radius,ratio=False,highlightthickness=0)
        tab.close.grid(row=0,column=2,sticky=NSEW)
        tab.right=Canvas(tab,highlightthickness=0,width=2*self.radius)
        if self.addcommand: tab.pack(side=LEFT,fill=Y,before=self.addbutton)
        else: tab.pack(side=LEFT,fill=Y)

        tab.container=Frame(self,container=True,bg=containerbackground)
        tab.frameid=tab.container.winfo_id()
        tab.toplevel=Toplevel(tab,use=tab.frameid)
        tab.toplevel.title(tab.label.cget('text'))
        tab.toplevel.geometry('400x400')
        tab.toplevel.protocol('WM_DETELE_PROTOCOL',lambda tab=tab: self._remove(tab))
        tab.baseframe=Frame(tab.toplevel,height=400,width=400)
        tab.baseframe.pack(fill=BOTH,expand=True)
        
        tab.windowed=False

        tab.label.bind('<FocusIn>',lambda event: self._focus(event.widget.master))
        tab.label.bind('<Delete>',lambda event: self._remove(event.widget.master))
        tab.toplevel.bind('<Configure>',self._dragwindow)
        tab.toplevel.bind('<FocusIn>',self._focussubwindow)
        
        tab.update()
        tab.activecolor=tab.label.cget('activebackground')
        tab.normalcolor=tab.label.cget('bg')
        tab.windowed=False
        tab.tag=tab.baseframe.tag=f'tag{self._tagcounter}'
        tab.lastx,tab.lasty=tab.toplevel.winfo_rootx(),tab.toplevel.winfo_rooty()

        self._createcorners(tab)
        tab.update()

        self._tags[tab.tag]=tab
        self._tagcounter+=1

        self._focus(tab)

        return tab.baseframe
    def insert(self,at,cnf={},**kw):
        cnf=cnfmerge((cnf,kw))
        self._checkcnf(cnf,self._TABARGS)
        if 'width' not in cnf and 'text' not in cnf: cnf['width']=2
        if 'bg' not in cnf: cnf['bg']=self.tabbackground
        containerbackground=cnf.pop('containerbackground',cnf['activebackground'])
        tab=Frame(self.tabsection)
        tab.columnconfigure((0,3),minsize=2*self.radius)
        tab.columnconfigure(1,weight=1)
        tab.rowconfigure(0,weight=1)
        tab.left=Canvas(tab,highlightthickness=0,width=2*self.radius)
        tab.label=Label(tab,cnf,anchor=CENTER)
        tab.label.grid(row=0,column=1,sticky=NSEW)
        tab.close=CustomButton(tab,args=(tab,),form=CustomButton.CROSS,activecolor='red',irelwidth=.75,irelheight=.75,movewidth=1,command=self._remove,bd=0,
                               disabledcolor='SystemDisabledText',cursor='hand2',height=2*self.radius,width=2*self.radius,ratio=False,highlightthickness=0)
        tab.close.grid(row=0,column=2,sticky=NSEW)
        tab.right=Canvas(tab,highlightthickness=0,width=2*self.radius)
        tab.pack(side=LEFT,fill=Y,before=self._getTab(at))

        tab.container=Frame(self,container=True,bg=containerbackground)
        tab.frameid=tab.container.winfo_id()
        tab.toplevel=Toplevel(tab,use=tab.frameid)
        tab.toplevel.title(tab.label.cget('text'))
        tab.toplevel.protocol('WM_DETELE_PROTOCOL',lambda tab=tab: self._remove(tab))
        tab.baseframe=Frame(tab.toplevel,height=400,width=400)
        tab.baseframe.pack(fill=BOTH,expand=True)

        tab.label.bind('<FocusIn>',lambda event: self._focus(event.widget.master))
        tab.label.bind('<Delete>',lambda event: self._remove(event.widget.master))
        tab.toplevel.bind('<Configure>',self._dragwindow)
        tab.toplevel.bind('<FocusIn>',self._focussubwindow)
        
        tab.update()
        tab.activecolor=tab.label.cget('activebackground')
        tab.normalcolor=tab.label.cget('bg')
        tab.windowed=False
        tab.tag=tab.baseframe.tag=f'tag{self._tagcounter}'
        
        self._createcorners(tab)
        tab.update()

        self._tags[tab.tag]=tab
        self._tagcounter+=1

        self._focus(tab)
        
        return tab.baseframe
    def remove(self,child):
        self._remove(self._getTab(child))
    def itemconfig(self,child,cnf={},**kw):
        tab=self._getTab(child)
        cnf=cnfmerge((cnf,kw))
        self._checkcnf(cnf,self._TABARGS)
        if 'containerbackground' in cnf: tab.container.config(bg=cnf.pop('containerbackground'))
        tab.label.config(cnf)
        if 'text' in cnf: tab.toplevel.title(cnf['text'])
        if 'activebackground' in cnf:
            tab.activecolor=cnf['activebackground']
            tab.left['bg']=tab.right['bg']=tab.activecolor
            if tab==self._focused: tab.close.config(bg=tab.activecolor)
        if 'background' in cnf or 'bg' in cnf:
            tab.normalcolor=tab.label.cget('bg')
            if tab!=self._focused: tab.close.config(bg=tab.normalcolor)
    itemconfigure=itemconfig
    def itemcget(self,child,key):
        if key in self._TABARGS:
            if key=='containerbackground': return self._getTab(child).container.cget('bg')
            else: return self._getTab(child).label.cget(key)
        raise TclError(f'unknown tab option "-{key}"')
        
    @classmethod
    def itemkeys(cls):
        return cls._TABARGS
    def fromTag(self,child):
        return self._getTab(child).baseframe
    @property
    def order(self):
        return self.tabsection.pack_slaves()[:-1] if self.addcommand else self.tabsection.pack_slaves()
    def config(self,cnf=None,**kw):
        cnf,dictupdate=filtercnf(cnf,kw,self._EXTRAS)
        self.__dict__.update(dictupdate)
        super().config(cnf)
        if 'tabbackground' in dictupdate:
            self.tabsection.config(bg=self.tabbackground)
            self.addbutton.config(bg=self.tabbackground)
            if 'radius' not in dictupdate:
                for tab in self.order:
                    tab.config(bg=self.tabbackground)
                    tab.left.itemconfig(0,fill=self.tabbackground)
                    tab.left.itemconfig(1,fill=self.tabbackground)
                    tab.left.itemconfig(2,fill=self.tabbackground)
                    tab.right.itemconfig(0,fill=self.tabbackground)
                    tab.right.itemconfig(1,fill=self.tabbackground)
                    tab.right.itemconfig(2,fill=self.tabbackground)
        if 'radius' in dictupdate:
            for tab in self.order: self._createcorners(tab)
        if 'addcommand' in dictupdate:
            mapped=self.addbutton.winfo_ismapped()
            if self.addcommand and not mapped: self.addbutton.pack(side=LEFT,expand=True)
            elif not self.addcommand and mapped: self.addbutton.pack_forget()
        if 'tabheight' in dictupdate: self.tabsection.config(height=self.tabheight)
        if 'dynamictabheight' in dictupdate: self.tabsection.pack_propagate(self.dynamictabheight)
        if 'addbuttonnf' in dictupdate: self.addbutton.config(cnf)
        if 'padx' in dictupdate: self.tabsection.config(padx=self.padx)
        if 'tabcycle' in dictupdate:
            if self.tabcycle and not self._next:
                self._next=self._tl.bind('<Control-Tab>',self.next,ADD)
                self._previous=self._tl.bind('<Control-Shift-Tab>',self.previous,ADD)
            elif self._next:
                self._tl.unbind(None,self._next)
                self._tl.unbind(None,self._previous)
        self.update()
    configure=config
    def cget(self,key):
        if key in self._EXTRAS: return getattr(self,key)
        elif key in self._ARGS: return super().cget(key)
        else: raise TclError(f'unknown option "-{key}"')
    __getitem__=cget
    @classmethod
    def keys(cls):
        return self._EXTRAS+self._ARGS

class Validator:
    def __init__(self, value = False):
        self.value = value
    def __enter__(self):
        if not self.value:
            self.value = True
            return empty
        else: return Validator._raise
    @classmethod
    def _raise(cls): raise cls.Break("Can't interfear with active process.")
    def __exit__(self, error, errormsg, trace):
        if not error: self.value = False
        elif issubclass(error, self.Break): return True
    @staticmethod
    class Break(Exception): pass

class Scrollframe(Frame):
    '''Frame widget which may contain other widgets, can have a 3D border
    and can be scrolled both hozitontally and vertically.'''
    _OUTER = ('bd', 'borderwidth', 'colormap', 'container', 'height', 'highlightthickness', 'width', 'highlightcolor', 'highlightbackground', 'padx', 'pady',
             'relief', 'takefocus')
    _INNER = ('ipadx', 'ipady', 'visual', 'ibd', 'iborderwidth', 'irelief')
    _BOTH = ('bg', 'background', 'class', 'cursor')
    _EXTRA = ('yscrollcommand', 'xscrollcommand', 'fill', 'focus', 'minheight', 'minwidth', 'bordermode', 'unit', 'page', 'segment')
    _ONLY_INITIAL = ('container', 'colormap', 'class', 'visual')
    _focusSwitch = {CENTER: (1, 1), N: (1, 0), NE: (2, 0), E: (2, 1), SE: (2, 2),
                    S: (1, 2), SW: (0, 2), W: (0, 1), NW: (0, 0)}
    def __init__(self, master=None, cnf={}, **kw):
        '''Construct a scrollframe widget with the parent MASTER.

        STANDARD OPTIONS

            background, bd, bg, borderwidth, class,
            colormap, container, cursor, height,
            highlightbackground, highlightcolor,
            highlightthickness, relief, takefocus,
            visual, width

        WIDGET-SPECIFIC OPTIONS

            ipadx, ipady, visual, ibd, iborderwidth,
            irelief, yscrollcommand, xscrollcommand,
            sticky, focus, minheight, minwidth, 
            bordermode, unit, page, segment'''
        cnf, extra = filtercnf(cnf, kw, yscrollcommand=None, xscrollcommand=None, fill=NONE, focus=NONE, minheight=0, minwidth=0, bordermode=INSIDE,
                               unit=30, page=400, segment=.5)
        cnf, both = filtercnf(cnf, None, *self._BOTH, width=extra['minwidth'], height=extra['minheight'])
        outer, inner = filtercnf(cnf, None, *self._INNER, width=extra['minwidth'], height=extra['minheight'])
        for option, value in inner.copy().items():
            if option.startswith('i'):
                inner[option[1:]] = value
                del inner[option]
        outer.update(both), inner.update(both)
        
        self._outer = Frame(master, outer)
        self._support = Frame(self._outer, both) #otherwise placing the inner frame would ignore borders completely
        self._support.place(x=0, y=0, relheight=1, relwidth=1, bordermode=extra['bordermode']) #using place over pack/grid because it doesn't resize the master
        Frame.__init__(self, self._support, inner)
        self.__dict__.update({'_'+key: value for key, value in extra.items()})
        Frame.place(self, x=0, y=0)
        self.master = master

        self._adopting = Validator()
        self._x, self._y = 0, 0
        self._focusregister = {}
        self._focused = None

        self._outer.bind('<Configure>', self._adopt_outer, True)
        self._support.bind('<Configure>', self._adopt_outer, True)
        Frame.bind(self, '<Configure>', self._adopt_outer, True)

        self._adopt_outer()

    def _adopt_inner(self, event=None):
        '''Internal function
        
        adopts inner frames size according to
        minsize and fill settings'''
        with self._adopting as test:
            test()
            placeinfo = Frame.place_info(self).copy()
            if event: width, height = event.width, event.height
            else: width, height = Frame.winfo_width(self), Frame.winfo_height(self)
            reqwidth, reqheight = Frame.winfo_reqwidth(self), Frame.winfo_reqheight(self)

            if self._fill == X or self._fill == BOTH:
                if self._minwidth and reqwidth >= self._minwidth: Frame.place(self, width='', relwidth=1)
                elif self._minwidth and width < self._minwidth: Frame.place(self, width=self._minwidth, relwidth='')
                elif placeinfo['relwidth']=='': Frame.place(self, width='', relwidth=1)
            elif self._minwidth:
                if placeinfo['relwidth']!='': Frame.place(self, relwidth='')
                if reqwidth >= self._minwidth: Frame.place(self, width='')
                elif width < self._minwidth: Frame.place(self, width=self._minwidth)
            elif placeinfo['relwidth']=='1' or placeinfo['width']!='': Frame.place(self, width='', relwidth='')
            if self._fill == Y or self._fill == BOTH:
                if self._minheight and reqheight >= self._minheight: Frame.place(self, height='', relheight=1)
                elif self._minheight and height < self._minheight: Frame.place(self, height=self._minheight, relheight='')
                elif placeinfo['relheight']=='': Frame.place(self, height='', relheight=1)
            elif self._minheight:
                if placeinfo['relheight']!='': Frame.place(self, relheight='')
                if reqheight >= self._minheight: Frame.place(self, height='')
                elif height < self._minheight: Frame.place(self, height=self._minheight)
            elif placeinfo['relheight']=='1' or placeinfo['height']!='': Frame.place(self, height='', relheight='')

            Frame.update(self)
            Frame.update_idletasks(self)
    def _adopt_outer(self, event=None, *, newx=None, newy=None, output=None):
        '''Internal function
        
        Adopt the inner frames position upon
        size/position/border changes to the outer
        frame. Can also be used to shift the inner
        frames position.'''
        self.update()
        self.update_idletasks()
        if event:
            if event.widget == self:
                self._adopt_inner(event)
                innerWidth, innerHeight = event.width, event.height
                outerWidth, outerHeight = self._support.winfo_width(), self._support.winfo_height()
            else:
                self._adopt_inner()
                innerWidth, innerHeight = Frame.winfo_width(self), Frame.winfo_height(self)
                outerWidth, outerHeight = event.width, event.height
                newx, newy = self._focus_set()
        elif self._outer.winfo_ismapped():
            self._adopt_inner()
            outerWidth, outerHeight = self._support.winfo_width(), self._support.winfo_height()
            innerWidth, innerHeight = Frame.winfo_width(self), Frame.winfo_height(self)
        else: return #Might this create complications? -> maybe rather get w/h here by reqwidth/reqheight?
        maxNegX, maxNegY = outerWidth - innerWidth, outerHeight - innerHeight
        xRatio, yRatio = outerWidth / innerWidth , outerHeight / innerHeight

        if newx is not None: self._x = newx
        if self._x < maxNegX: self._x = maxNegX
        if self._x > 0: self._x = 0
        if newy is not None: self._y = newy
        if self._y < maxNegY: self._y = maxNegY
        if self._y > 0: self._y = 0
        
        if self._xscrollcommand and xRatio<1:
            firstVal = (self._x / maxNegX) * (1 - xRatio)
            self._xscrollcommand(firstVal, firstVal + xRatio)
        elif self._xscrollcommand: self._xscrollcommand(0,1)
        if self._yscrollcommand and yRatio<1:
            firstVal = (self._y / maxNegY) * (1 - yRatio)
            self._yscrollcommand(firstVal, firstVal + yRatio)
        elif self._yscrollcommand: self._yscrollcommand(0,1)

        Frame.place(self, x=self._x, y=self._y)

        self._outer.update()
        self._outer.update_idletasks()
        if output == X: return maxNegX, xRatio
        elif output == Y: return maxNegY, yRatio
    def focus_register(self, child, useAdd=True):
        '''Register child widget to automatic frame repositioning.'''
        if child not in self: raise TclError(f'{child} is not a child of {self}, thus can\'t be focused on it.')
        FocusIn = child.bind('<FocusIn>', lambda event: self._focus_set(event.widget), useAdd)
        FocusOut = child.bind('<FocusOut>', self._losefocus, useAdd)
        Destroy = child.bind('<Destroy>', lambda event:  self._focusregister.pop(event.widget,''), True)
        self._focusregister[child] = (FocusIn, FocusOut, Destroy)
    def focus_unregister(self, child):
        '''Unregister child widget from automatic frame repositioning.'''
        if child not in self._focusregister: raise TclError(f'{child} is not registered.')
        for tag in self._focusregister.pop(child): child.unbind(None, tag)
    def _autofocus(self, event):
        '''Internal function'''
        if event.widget in self._focusregister:
            self._focused = event.widget
            self.focus_set(event.widget)
        else: raise TclError(f'Got <FocusIn> event from unregistered widget {event.widget}. Please register this widget first.')
    def _losefocus(self, event):
        '''Internal function'''
        if event.widget == self._focused: self._focused = None
        else: raise TclError(f'Got <FocusOut> event from unregistered widget {event.widget}. Please register this widget first.')
    def _getFocusCoords(self, focus, child):
        childNegX, childNegY = Frame.winfo_rootx(self) - child.winfo_rootx(), Frame.winfo_rooty(self) - child.winfo_rooty()
        xPad, yPad = (self._support.winfo_width() - child.winfo_width()) // 2, (self._support.winfo_height() - child.winfo_height()) // 2
        xFactor, yFactor = self._focusSwitch[focus]

        return childNegX + xFactor * xPad, childNegY + yFactor * yPad
    def _focus_set(self, child=None):
        if self._focus == NONE:
            if child: self._focused = child
            return None, None #maybe consider something else?
        if not child:
            if not self._focused: return None, None
            child = self._focused
            output = True
        else:
            self._focused = child
            output = False
        
        if self._focus == AUTO:
            left, top, right, bottom = 0, 0, self._support.winfo_width(), self._support.winfo_height()
            childLeft, childTop = child.winfo_rootx() - self._support.winfo_rootx(), child.winfo_rooty() - self._support.winfo_rooty()
            childRight, childBottom = childLeft + child.winfo_width(), childTop + child.winfo_height()
            
            if childBottom >= bottom:
                if childLeft <= left: #bl
                    newx, newy = self._getFocusCoords(SW, child)
                elif left < childLeft and childRight < right: #b with percent
                    newx, newy = -childLeft, self._getFocusCoords(S, child)[1]
                else: #br
                    newx, newy = self._getFocusCoords(SE, child)
            elif childTop <= top:
                if childLeft <= left: #tl
                    newx, newy = self._getFocusCoords(NW, child)
                elif left < childLeft and childRight < right: #t with percent
                    newx, newy = -childLeft, self._getFocusCoords(N, child)[1]
                else: #tr
                    newx, newy = self._getFocusCoords(NE, child)
            else:
                if childLeft < left: #l with percent
                    newx, newy = self._getFocusCoords(N, child)[0], -childTop
                elif childRight > right: #r with percent
                    newx, newy = self._getFocusCoords(N, child)[1], -childTop
                else: newx = newy = None
        else: newx, newy = self._getFocusCoords(self._focus, child)
            
        if output: return newx, newy
        else: self._adopt_outer(newx=newx, newy=newy)
    def focus_set(self, child):
        '''Direct input focus to the child widget and reposition the frame.

        If the application currently does not have the focus
        this widget will get the focus if the application gets
        the focus through the window manager.
        Repositioning will happen according to the focus option.'''
        if child not in self: raise TclError(f'Can\'t focus {child} since it\'s not mapped on {self}.')
        self._focus_set(child)
    def xview(self, mode=None, value=None, submode=None):
        '''Query and change the vertical position of the view.'''
        maxNegX, xRatio = self._adopt_outer(output=X)
        if not mode:
            firstVal = (self._x / outerWidth - innerWidth) * xRatio
            return (firstVal, firstVal + xRatio)
        elif self._xscrollcommand:
            x = self._x
            if mode == MOVETO:
                perc = (float(value) / (1 - xRatio))
                x = round(perc * maxNegX)
            elif mode == SCROLL:  x -= int(value) * (self._unit if submode == UNITS else self._page)
            elif isinstance(mode, Event):
                if not pointer_over(self._outer): return
                elif mode.delta: x += int(mode.delta / 60) * self._unit
                else: x += self._unit
            else: x -= round((int(mode) / 4) * (self._segment * innerWidth))

            self._adopt_outer(newx=x)
    def yview(self, mode=None, value=None, submode=None):
        '''Query and change the vertical position of the view.'''
        maxNegY, yRatio = self._adopt_outer(output=Y)
        if not mode:
            firstVal = (self._y / outerWidth - innerWidth) * yRatio
            return (firstVal, firstVal + yRatio)
        elif self._yscrollcommand:
            y = self._y
            if mode == MOVETO:
                perc = (float(value) / (1 - yRatio))
                y = round(perc * maxNegY)
            elif mode == SCROLL:  y -= int(value) * (self._unit if submode == UNITS else self._page)
            elif isinstance(mode, Event):
                if not pointer_over(self._outer): return
                elif mode.delta: y += int(mode.delta / 60) * self._unit
                else: y += self._unit
            else: y -= round((int(mode) / 4) * (self._segment * innerWidth))

            self._adopt_outer(newy=y)
    def config(self, cnf=None, **kw):
        '''Configure resources of a widget.

        yscrollcommand = None, callable
        xscrollcommand = None, callable
        fill = X, Y, BOTH, NONE
        focus = NONE, AUTO, CENTER, N, NE, E, SE, S, SW, W, NW
        minheight = None, int (> 0)
        minwidth = None, int (> 0)
        bordermode = INSIDE, OUTSIDE
        unit = int
        page = int
        segment = float'''
        if cnf or kw:
            cnf, forbidden = filtercnf(cnf, kw, *self._ONLY_INITIAL)
            if forbidden: raise TclError('The following arguments may not be configured after initialization: "-' + '", "-'.join(forbidden.keys()) + '"')
            cnf, both = filtercnf(cnf, None, *self._BOTH)
            cnf, extra = filtercnf(cnf, None, *self._EXTRA)
            outer, inner = filtercnf(cnf, None, *self._INNER)
            for option, value in inner.items():
                if option.startswith('i'):
                    inner[option[1:]] = value
                    del inner[option]
            outer.update(both), inner.update(both)
            if 'minwidth' in extra: inner['width'] = both['width'] = extra['minwidth']
            if 'minheight' in extra: inner['height'] = both['height'] = extra['minheight']
            
            self._outer.config(outer)
            self._support.config(both)
            Frame.config(self, inner)
            self.__dict__.update({'_'+key: value for key, value in extra.items()})
            if 'bordermode' in extra: self._support.place(bordermode=self._bordermode)
            self._adopt_outer()
        else:
            config = {'yscrollcommand': ('yscrollcommand', None, None, None, self._yscrollcommand),
                      'xscrollcommand': ('xscrollcommand', None, None, None, self._xscrollcommand),
                      'fill': ('fill', None, None, NONE, self._fill),
                      'focus': ('focus', None, None, NONE, self._focus),
                      'minheight': ('minheight', None, None, 0, self._minheight),
                      'minwidth': ('minwidth', None, None, 0, self._minwidth),
                      'bordermode': ('bordermode', None, None, INSIDE, self._bordermode),
                      'unit': ('unit', None, None, 30, self._unit),
                      'page': ('page', None, None, 400, self._page),
                      'segment': ('segment', None, None, .5, self._segment)}

            outer, inner, both = self._outer.config(), Frame.config(self), self._support.config()
            for key in self._OUTER: config[key] = outer[key]
            for key in self._INNER:
                if key.startswith('i'): key = key[1:]
                config[key] = inner[key]
            for key in self._BOTH: config[key] = both[key]

            return config
    configure = config
    def cget(self, key):
        '''Return the resource value for a KEY given as string.'''
        if key in self._OUTER: return self._outer.cget(key)
        elif key in self._INNER + self._BOTH: return Frame.cget(self, key)
        else: return getattr(self, key)
    __getitem__ = cget
    @classmethod
    def keys(cls):
        '''Return a list of all resource names of this widget.'''
        return list(cls._BOTH + cls._INNER + cls._OUTER)


    ### override some methods because the widget itself isn't the base for this
    def bind(self, sequence=None, func=None, add=None):
        '''Bind to this widget at event SEQUENCE a call to function FUNC.

        SEQUENCE is a string of concatenated event
        patterns. An event pattern is of the form
        <MODIFIER-MODIFIER-TYPE-DETAIL> where MODIFIER is one
        of Control, Mod2, M2, Shift, Mod3, M3, Lock, Mod4, M4,
        Button1, B1, Mod5, M5 Button2, B2, Meta, M, Button3,
        B3, Alt, Button4, B4, Double, Button5, B5 Triple,
        Mod1, M1. TYPE is one of Activate, Enter, Map,
        ButtonPress, Button, Expose, Motion, ButtonRelease
        FocusIn, MouseWheel, Circulate, FocusOut, Property,
        Colormap, Gravity Reparent, Configure, KeyPress, Key,
        Unmap, Deactivate, KeyRelease Visibility, Destroy,
        Leave and DETAIL is the button number for ButtonPress,
        ButtonRelease and DETAIL is the Keysym for KeyPress and
        KeyRelease. Examples are
        <Control-Button-1> for pressing Control and mouse button 1 or
        <Alt-A> for pressing A and the Alt key (KeyPress can be omitted).
        An event pattern can also be a virtual event of the form
        <<AString>> where AString can be arbitrary. This
        event can be generated by event_generate.
        If events are concatenated they must appear shortly
        after each other.

        FUNC will be called if the event sequence occurs with an
        instance of Event as argument. If the return value of FUNC is
        "break" no further bound function is invoked.

        An additional boolean parameter ADD specifies whether FUNC will
        be called additionally to the other bound function or whether
        it will replace the previous function.

        Bind will return an identifier to allow deletion of the bound function with
        unbind without memory leak.

        If FUNC or SEQUENCE is omitted the bound function or list
        of bound events are returned.'''
        return Frame.bind(self._outer, sequence, func, add)

    def bindtags(self, tagList=None):
        '''Set or get the list of bindtags for this widget.

        With no argument return the list of all bindtags associated with
        this widget. With a list of strings as argument the bindtags are
        set to this list. The bindtags determine in which order events are
        processed (see bind).'''
        return Frame.bindtags(self._outer, tagList)

    def event_add(self, virtual, *sequences):
        '''Bind a virtual event VIRTUAL (of the form <<Name>>)
        to an event SEQUENCE such that the virtual event is triggered
        whenever SEQUENCE occurs.'''
        return Frame.event_add(self._outer, virtual, *sequences)

    def event_delete(self, virtual, *sequences):
        '''Unbind a virtual event VIRTUAL from SEQUENCE.'''
        return Frame.event_delete(self._outer, virtual, *sequences)

    def event_generate(self, sequence, **kw):
        '''Generate an event SEQUENCE. Additional
        keyword arguments specify parameter of the event
        (e.g. x, y, rootx, rooty).'''
        return Frame.event_generate(self._outer, sequence, **kw)

    def event_info(self, virtual=None):
        '''Return a list of all virtual events or the information
        about the SEQUENCE bound to the virtual event VIRTUAL.'''
        return Frame.event_info(self._outer, virtual)

    def unbind(self, sequence, funcid=None):
        '''Unbind the function identified with FUNCID for
        this widget for event SEQUENCE.'''
        return Frame.unbind(self._outer, sequence, funcid)

    #########################################################

    def bind_inner(self, sequence=None, func=None, add=None):
        '''Bind to this widgets inner frame at event SEQUENCE
        a call to function FUNC.

        SEQUENCE is a string of concatenated event
        patterns. An event pattern is of the form
        <MODIFIER-MODIFIER-TYPE-DETAIL> where MODIFIER is one
        of Control, Mod2, M2, Shift, Mod3, M3, Lock, Mod4, M4,
        Button1, B1, Mod5, M5 Button2, B2, Meta, M, Button3,
        B3, Alt, Button4, B4, Double, Button5, B5 Triple,
        Mod1, M1. TYPE is one of Activate, Enter, Map,
        ButtonPress, Button, Expose, Motion, ButtonRelease
        FocusIn, MouseWheel, Circulate, FocusOut, Property,
        Colormap, Gravity Reparent, Configure, KeyPress, Key,
        Unmap, Deactivate, KeyRelease Visibility, Destroy,
        Leave and DETAIL is the button number for ButtonPress,
        ButtonRelease and DETAIL is the Keysym for KeyPress and
        KeyRelease. Examples are
        <Control-Button-1> for pressing Control and mouse button 1 or
        <Alt-A> for pressing A and the Alt key (KeyPress can be omitted).
        An event pattern can also be a virtual event of the form
        <<AString>> where AString can be arbitrary. This
        event can be generated by event_generate.
        If events are concatenated they must appear shortly
        after each other.

        FUNC will be called if the event sequence occurs with an
        instance of Event as argument. If the return value of FUNC is
        "break" no further bound function is invoked.

        An additional boolean parameter ADD specifies whether FUNC will
        be called additionally to the other bound function or whether
        it will replace the previous function.

        Bind will return an identifier to allow deletion of the bound function with
        unbind without memory leak.

        If FUNC or SEQUENCE is omitted the bound function or list
        of bound events are returned.'''
        return Frame.bind(self, sequence, func, add)

    def bindtags_inner(self, tagList=None):
        '''Set or get the list of bindtags for this widgets
        inner frame.

        With no argument return the list of all bindtags associated with
        this widget. With a list of strings as argument the bindtags are
        set to this list. The bindtags determine in which order events are
        processed (see bind).'''
        return Frame.bindtags(self, tagList)

    def unbind_inner(self, sequence, funcid=None):
        '''Unbind the function identified with FUNCID for
        this widgets inner frame for event SEQUENCE.'''
        return Frame.unbind(self, sequence, funcid)

    #############################################################

    def focus(self):
        '''Direct input focus to this widget.

        If the application currently does not have the focus
        this widget will get the focus if the application gets
        the focus through the window manager.'''
        return Frame.focus(self._outer)

    def focus_force(self):
        '''Direct input focus to this widget even if the
        application does not have the focus. Use with
        caution!'''
        return Frame.focus_force(self._outer)

    def forget(self):
        '''Unmap this widget and do not use it for the packing order.'''
        return Frame.forget(self._outer)

    def grid(self, cnf={}, **kw):
        '''Position a widget in the parent widget in a grid. Use as options:
        column=number - use cell identified with given column (starting with 0)
        columnspan=number - this widget will span several columns
        in=master - use master to contain this widget
        in_=master - see 'in' option description
        ipadx=amount - add internal padding in x direction
        ipady=amount - add internal padding in y direction
        padx=amount - add padding in x direction
        pady=amount - add padding in y direction
        row=number - use cell identified with given row (starting with 0)
        rowspan=number - this widget will span several rows
        sticky=NSEW - if cell is larger on which sides will this
                      widget stick to the cell boundary
        '''
        output = Frame.grid(self._outer, cnf, **kw)
        self._adopt_outer()
        return output

    grid_configure = grid

    def grid_forget(self):
        '''Unmap this widget.'''
        return Frame.grid_forget(self._outer)

    def grid_info(self):
        '''Return information about the options
        for positioning this widget in a grid.'''
        return Frame.grid_info(self._outer)

    def grid_remove(self):
        '''Unmap this widget but remember the grid options.'''
        return Frame.grid_remove(self._outer)

    def info(self):
        '''Return information about the packing options
        for this widget.'''
        return Frame.info(self._outer)

    def lift(self, aboveThis=None):
        '''Raise this widget in the stacking order.'''
        return Frame.lift(self._outer, aboveThis)

    def lower(self, belowThis=None):
        '''Lower this widget in the stacking order.'''
        return Frame.lower(self._outer, belowThis)

    def mainloop(self, n=0):
        '''Call the mainloop of Tk.'''
        return Frame.mainloop(self._outer, n)

    def pack(self, cnf={}, **kw):
        '''Pack a widget in the parent widget. Use as options:
        after=widget - pack it after you have packed widget
        anchor=NSEW (or subset) - position widget according to
                                  given direction
        before=widget - pack it before you will pack widget
        expand=bool - expand widget if parent size grows
        fill=NONE or X or Y or BOTH - fill widget if widget grows
        in=master - use master to contain this widget
        in_=master - see 'in' option description
        ipadx=amount - add internal padding in x direction
        ipady=amount - add internal padding in y direction
        padx=amount - add padding in x direction
        pady=amount - add padding in y direction
        side=TOP or BOTTOM or LEFT or RIGHT -  where to add this widget.
        '''
        output = Frame.pack(self._outer, cnf, **kw)
        self._adopt_outer()
        return output

    pack_configure = pack

    def pack_forget(self):
        '''Unmap this widget and do not use it for the packing order.'''
        return Frame.pack_forget(self._outer)

    def pack_info(self):
        '''Return information about the packing options
        for this widget.'''
        return Frame.pack_info(self._outer)

    def place(self, cnf={}, **kw):
        '''Place a widget in the parent widget. Use as options:
        in=master - master relative to which the widget is placed
        in_=master - see 'in' option description
        x=amount - locate anchor of this widget at position x of master
        y=amount - locate anchor of this widget at position y of master
        relx=amount - locate anchor of this widget between 0.0 and 1.0
                      relative to width of master (1.0 is right edge)
        rely=amount - locate anchor of this widget between 0.0 and 1.0
                      relative to height of master (1.0 is bottom edge)
        anchor=NSEW (or subset) - position anchor according to given direction
        width=amount - width of this widget in pixel
        height=amount - height of this widget in pixel
        relwidth=amount - width of this widget between 0.0 and 1.0
                          relative to width of master (1.0 is the same width
                          as the master)
        relheight=amount - height of this widget between 0.0 and 1.0
                           relative to height of master (1.0 is the same
                           height as the master)
        bordermode="inside" or "outside" - whether to take border width of
                                           master widget into account
        '''
        output = Frame.place(self._outer, cnf, **kw)
        self._adopt_outer()
        return output

    place_configure = place

    def place_forget(self):
        '''Unmap this widget.'''
        return Frame.place_forget(self._outer)

    def place_info(self):
        '''Return information about the placing options
        for this widget.'''
        return Frame.place_info(self._outer)

    def quit(self):
        '''Quit the Tcl interpreter. All widgets will be destroyed.'''
        return Frame.quit(self._outer)

    def tkraise(self, aboveThis=None):
        '''Raise this widget in the stacking order.'''
        return Frame.tkraise(self._outer, aboveThis)

    def update(self):
        '''Enter event loop until all pending events have been processed by Tcl.'''
        output = self._outer.update()
        self._support.update()
        Frame.update(self)
        return output

    def update_idletasks(self):
        '''Enter event loop until all idle callbacks have been called. This
        will update the display of windows but not process events caused by
        the user.'''
        output = self._outer.update_idletasks()
        self._support.update_idletasks()
        Frame.update_idletasks(self)
        return output

    def winfo_cells(self):
        '''Return number of cells in the colormap for this widget.'''
        return Frame.winfo_cells(self._outer)

    def winfo_class(self):
        '''Return window class name of this widget.'''
        return Frame.winfo_class(self._outer)

    def winfo_colormapfull(self):
        '''Return true if at the last color request the colormap was full.'''
        return Frame.winfo_colormapfull(self._outer)

    def winfo_exists(self):
        '''Return true if this widget exists.'''
        return Frame.winfo_exists(self._outer)

    def winfo_geometry(self):
        '''Return geometry string for this widget in the form "widthxheight+X+Y".'''
        return Frame.winfo_geometry(self._outer)

    def winfo_id(self):
        '''Return identifier ID for this widget.'''
        return Frame.winfo_id(self._outer)

    def winfo_ismapped(self):
        '''Return true if this widget is mapped.'''
        return Frame.winfo_ismapped(self._outer)

    def winfo_manager(self):
        '''Return the window manager name for this widget.'''
        return Frame.winfo_manager(self._outer)

    def winfo_name(self):
        '''Return the name of this widget.'''
        return Frame.winfo_name(self._outer)

    def winfo_parent(self):
        '''Return the name of the parent of this widget.'''
        return Frame.winfo_parent(self._outer)

    def winfo_height(self, mode=OUTSIDE):
        '''Return height of this widget.'''
        if mode == OUTSIDE: return self._outer.winfo_height()
        elif mode == WINDOW: return self._support.winfo_height()
        elif mode == INSIDE: return Frame.winfo_height(self)
        else: raise TclError(f'Unknown mode "{mode}".')

    def winfo_width(self, mode=OUTSIDE):
        '''Return the width of this widget.'''
        if mode == OUTSIDE: return self._outer.winfo_width()
        elif mode == WINDOW: return self._support.winfo_width()
        elif mode == INSIDE: return Frame.winfo_width(self)
        else: raise TclError(f'Unknown mode "{mode}".')

    def winfo_reqheight(self, mode=OUTSIDE):
        '''Return requested height of this widget.'''
        if mode == OUTSIDE: return self._outer.winfo_reqheight()
        elif mode == WINDOW: return self._support.winfo_reqheight()
        elif mode == INSIDE: return Frame.winfo_reqheight(self)
        else: raise TclError(f'Unknown mode "{mode}".')

    def winfo_reqwidth(self, mode=OUTSIDE):
        '''Return requested width of this widget.'''
        if mode == OUTSIDE: return self._outer.winfo_reqwidth()
        elif mode == WINDOW: return self._support.winfo_reqwidth()
        elif mode == INSIDE: return Frame.winfo_reqwidth(self)
        else: raise TclError(f'Unknown mode "{mode}".')

    def winfo_rootx(self):
        '''Return x coordinate of upper left corner of this widget on the
        root window.'''
        return Frame.winfo_rootx(self._outer)

    def winfo_rooty(self):
        '''Return y coordinate of upper left corner of this widget on the
        root window.'''
        return Frame.winfo_rooty(self._outer)

    def winfo_screen(self):
        '''Return the screen name of this widget.'''
        return Frame.winfo_screen(self._outer)

    def winfo_viewable(self):
        '''Return true if the widget and all its higher ancestors are mapped.'''
        return Frame.winfo_viewable(self._outer)

    def winfo_visual(self):
        '''Return one of the strings directcolor, grayscale, pseudocolor,
        staticcolor, staticgray, or truecolor for the
        colormodel of this widget.'''
        return Frame.winfo_visual(self._outer)

    def winfo_visualid(self):
        '''Return the X identifier for the visual for this widget.'''
        return Frame.winfo_visualid(self._outer)

    def winfo_visualsavailable(self, includeids=False):
        '''Return a list of all visuals available for the screen
        of this widget.

        Each item in the list consists of a visual name (see winfo_visual), a
        depth and if includeids is true is given also the X identifier.'''
        return Frame.winfo_visualsavailable(self._outer, includeids)

    def winfo_vrootheight(self):
        '''Return the height of the virtual root window associated with this
        widget in pixels. If there is no virtual root window return the
        height of the screen.'''
        return Frame.winfo_vrootheight(self._outer)

    def winfo_vrootwidth(self):
        '''Return the width of the virtual root window associated with this
        widget in pixel. If there is no virtual root window return the
        width of the screen.'''
        return Frame.winfo_vrootwidth(self._outer)

    def winfo_vrootx(self):
        '''Return the x offset of the virtual root relative to the root
        window of the screen of this widget.'''
        return Frame.winfo_vrootx(self._outer)

    def winfo_vrooty(self):
        '''Return the y offset of the virtual root relative to the root
        window of the screen of this widget.'''
        return Frame.winfo_vrooty(self._outer)

    def winfo_x(self):
        '''Return the x coordinate of the upper left corner of this widget
        in the parent.'''
        return Frame.winfo_x(self._outer)

    def winfo_y(self):
        '''Return the y coordinate of the upper left corner of this widget
        in the parent.'''
        return Frame.winfo_y(self._outer)

class Settings(Toplevel): #CONTINUE
    '''Simple 2 row per tab settings window.'''
    _PASS = ('bd', 'borderwidth', 'relief', 'screen', 'use', 'background', 'bg', 'colormap', 'cursor', 'height',
             'highlightbackground', 'highlightcolor', 'highlightthickness', 'padx', 'pady', 'takefocus', 'width')
    _EXTRAS = ('styleprefix', 'middlepadding', 'buttons', 'buttonanchor', 'hidecommand', 'showcommand')
    def __init__(self, master=None, cnf={}, enable_traversal=True, **kw):
        '''Construct a toplevel widget with the parent MASTER.

        Valid resource names: bd, borderwidth, relief, screen, use,
        background, bg, colormap, cursor, height, highlightbackground,
        highlightcolor, highlightthickness, padx, pady, takefocus, width.'''
        cnf, extras = filtercnf(cnf, kw, styleprefix='Settings', middlepadding=0, buttons=(), buttonanchor=CENTER, hidecommand=None, showcommand=None)
        self._checkcnf(cnf)

        Toplevel.__init__(self, master, width=650, height=700, **cnf)
        self.__dict__.update({'_' + key: value for key, value in extras.items()})
        if self._styleprefix: self._styleprefix += '.'

        self.transient(master)
        self.protocol('WM_DELETE_WINDOW', self.hide)
        self.pack_propagate(False)

        self._notebook = ttk.Notebook(self, style=self._styleprefix + 'TNotebook')
        self._notebook.pack(side=TOP, fill=BOTH, expand=True)
        self._buttonBase = ttk.Frame(self, style=self._styleprefix + 'TFrame')
        self._buttonFrame = ttk.Frame(self, padding=(5, 10), style=self._styleprefix + 'TFrame')
        self._buttonFrame.pack(fill=Y, anchor=self._buttonanchor)
        if self._buttons:
            for text, command in self._buttons:
                ttk.Button(self._buttonFrame, style=self._styleprefix + 'TButton', text=text, command=command).pack(fill=Y, side=LEFT, padx=5)
            self._buttonBase.pack(side=BOTTOM, fill=X, anchor=self._buttonanchor)
        if enable_traversal: self._notebook.enable_traversal()
        
        self._contents = {}
        self.enable_traversal = self._notebook.enable_traversal

        self.update()
        self.withdraw()

        #Layout:
        # {section1: (sectionFrame, order,
        #             {label: (Label, optionFrame,
        #                      {tag1: (option, before),
        #                       ...,
        #                       tagn: (option, before)}),
        #              ...,
        #              label2: ...}),
        #  ...,
        #  sectionn: (...)}

    # SECTIONS
    def section_add(self, section: str, **kw):
        '''Adds a new section tab.'''
        if section in self._contents: raise TclError(f'{self} - duplicate: "{section}".')

        support = ttk.Frame(self._notebook, style=self._styleprefix + 'TFrame')
        sectionFrame = Scrollframe(support, ipadx=5, ipady=5, fill=X, focus=AUTO)
        sectionFrame.pack(side=LEFT, fill=BOTH, expand=True)
        sectionFrame.columnconfigure(1, minsize=self._middlepadding)
        sectionFrame.columnconfigure(2, weight=1)
        scrollbar = ttk.Scrollbar(support, style=self._styleprefix + 'Vertical.TScrollbar', orient=VERTICAL, command=sectionFrame.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        sectionFrame.config(yscrollcommand=scrollbar.set)
        self._notebook.add(support, text=section, **kw)
        self._contents[section] = (sectionFrame, [], {})
        
    def section_insert(self, before: str, section: str, **kw):
        '''Inserts a new section tab before given tab.'''
        if section in self._contents: raise TclError(f'{self} - duplicate: "{section}".')
        elif before not in self._contents: raise TclError(f'{self} - not found: "{before}".')

        support = ttk.Frame(self._notebook, style=self._styleprefix + 'TFrame')
        sectionFrame = Scrollframe(support, ipadx=5, ipady=5, fill=X, focus=AUTO)
        sectionFrame.pack(side=LEFT, fill=BOTH, expand=True)
        sectionFrame.columnconfigure(1, minsize=self._middlepadding)
        sectionFrame.columnconfigure(2, weight=1)
        scrollbar = ttk.Scrollbar(support, style=self._styleprefix + 'Vertical.TScrollbar', orient=VERTICAL, command=sectionFrame.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        sectionFrame.config(yscrollcommand=scrollbar.set)
        self._notebook.insert(self._contents[before][0].master, support, text=section, **kw)
        self._contents[section] = (sectionFrame, [], {})
        
    def section_move(self, before: str, section: str):
        '''Moves tab before other tab'''
        if section not in self._contents: raise TclError(f'{self} - not found: "{section}".')
        if before not in self._contents: raise TclError(f'{self} - not found: "{before}".')

        self._notebook.insert(self._contents[before][0].master, self._contents[section][0].master)
        
    def section_remove(self, section: str):
        '''Completely remove section tab.'''
        if section not in self._contents: raise TclError(f'{self} - not found: "{section}".')

        self._notebook.forget(self._contents[section][0].master)
        self._contents[section][0].master.destroy()
        del self._contents[section]
        
    def section_hide(self, section: str):
        '''Temporarely remove section tab.
        
        Restore section tab with Settings.section_show.'''
        if section not in self._contents: raise TclError(f'{self} - not found: "{section}".')

        self._notebook.hide(self._contents[section][0].master)
        
    def section_show(self, section: str):
        '''Restore section tab.'''
        if section not in self._contents: raise TclError(f'{self} - not found: "{section}".')

        self._notebook.add(self._contents[section][0].master)

    def section_rename(self, section: str, new: str):
        '''Update the sections name.'''
        if section not in self._contents: raise TclError(f'{self} - not found: "{section}".')
        elif new in self._contents: raise TclError(f'{self} - duplicate: "{new}".')

        self._notebook.tab(self._contents[section][0].master, text=new)
        self._contents[new] = self._contents.pop(section)
    
    def section_config(self, section: str, **kw):
        '''Update or query the tabs options.
        
        If kw is not given returns the option dict.
        Otherwise sets given options.'''
        if section in self._contents: raise TclError(f'{self} - duplicate: "{section}".')

        return self._notebook.tab(self._contents[section][0].master, **kw)

    section_configure = section_config
    
    def section_cget(self, section: str, key: str):
        '''Query options value for given tab.'''
        if section in self._contents: raise TclError(f'{self} - duplicate: "{section}".')

        return self._notebook.tab(self._contents[section][0].master, key)
        
    # LABELS
    def label_add(self, section: str, label: str):
        '''Add a subsection to the section tab.'''
        if section not in self._contents: raise TclError(f'{self} - not found: "{section}".')
        sectionFrame, order, labels = self._contents[section]
        if label in labels: raise TclError(f'{self}:{section} - duplicate: "{label}".')

        row = len(order)
        settingLabel = ttk.Label(sectionFrame, style=self._styleprefix + 'TLabel', text=label + ':')
        settingLabel.grid(row=row, column=0, sticky=N + EW, padx=5, pady=5)
        optionFrame = ttk.Frame(sectionFrame, style=self._styleprefix + 'TFrame')
        optionFrame.grid(row=row, column=2, sticky=NSEW)

        labels[label] = (settingLabel, optionFrame, {})
        order.append(label)
        
    def label_insert(self, section: str, before: str, label: str):
        '''Insert a subsection before the given subsection to the section tab.'''
        if section not in self._contents: raise TclError(f'{self} - not found: "{section}".')
        sectionFrame, order, labels = self._contents[section]
        if label in labels: raise TclError(f'{self}:{section} - duplicate: "{label}".')
        elif before not in labels: raise TclError(f'{self}:{section} - not found: "{before}".')

        row = order.index(before)
        settingLabel = ttk.Label(sectionFrame, style=self._styleprefix + 'TLabel', text=label + ':')
        settingLabel.grid(row=row, column=0, sticky=N + EW, padx=5, pady=5)
        optionFrame = ttk.Frame(sectionFrame, style=self._styleprefix + 'TFrame')
        optionFrame.grid(row=row, column=2, sticky=NSEW)

        labels[label] = (settingLabel, optionFrame, {})
        order.insert(row, label)

        self._rearrangeLabels(labels, order, row)
        
    def label_move(self, section: str, before: str, label: str):
        '''Move subsection before other subsection.'''
        if section not in self._contents: raise TclError(f'{self} - not found: "{section}".')
        sectionFrame, order, labels = self._contents[section]
        if label not in labels: raise TclError(f'{self}:{section} - not found: "{label}".')
        elif before not in labels: raise TclError(f'{self}:{section} - not found: "{before}".')

        oldRow = order.index(label)
        newRow = order.index(before)
        order.insert(newRow, order.pop(oldRow))
        self._rearrangeLabels(labels, order, min(oldRow, newRow))
        
    def label_remove(self, section: str, label: str):
        '''Completely remove subsection.'''
        if section not in self._contents: raise TclError(f'{self} - not found: "{section}".')
        sectionFrame, order, labels = self._contents[section]
        if label not in labels: raise TclError(f'{self}:{section} - not found: "{label}".')

        row = order.index(label)
        settingLabel, optionFrame = labels[label][:2]
        settingLabel.destroy()
        optionFrame.destroy()
        order.remove(label)
        del labels[label]
        self._rearrangeLabels(labels, order, row)

    def label_rename(self, section: str, label: str, new: str):
        '''Update subsections name.'''
        if section not in self._contents: raise TclError(f'{self} - not found: "{section}".')
        sectionFrame, order, labels = self._contents[section]
        if label not in labels: raise TclError(f'{self}:{section} - not found: "{label}".')
        if new in labels: raise TclError(f'{self}:{section}  - duplicate: "{new}".')

        labels[new] = labels.pop(label)
        labels[new][0].config(text=new + ':')
        order.insert(order.index(label), new)
        order.remove(label)

    # SEPARATOR
    def separator_add(self, section: str) -> str:
        '''Add a separator into section.'''
        if section not in self._contents: raise TclError(f'{self} - not found: "{section}".')
        sectionFrame, order, labels = self._contents[section]

        row = len(order)
        separator = ttk.Separator(sectionFrame, style=self._styleprefix + 'TSeparator', orient=HORIZONTAL)
        separator.grid(row=row, column=0, columnspan=3, sticky=EW, pady=5)#, padx=5)
        tag = '<Separator>' + str(id(separator))
        order.append(tag)
        labels[tag] = separator

        return tag

    def separator_insert(self, section: str, before: str) -> str:
        '''Insert a separator before given label into section.'''
        if section not in self._contents: raise TclError(f'{self} - not found: "{section}".')
        sectionFrame, order, labels = self._contents[section]
        if before not in labels: raise TclError(f'{self}:{section} - not found: "{before}".')

        row = order.index(before)

        separator = ttk.Separator(sectionFrame, style=self._styleprefix + 'TSeparator', orient=HORIZONTAL)
        separator.grid(row=row, column=0, columnspan=3, sticky=EW, pady=5)#, padx=5)
        tag = '<Separator>' + str(id(separator))
        order.insert(row, tag)
        labels[tag] = separator

        self._rearrangeLabels(labels, order, row)

        return tag

    def separator_remove(self, section: str, separator: str):
        '''Remove given Separator from section.'''
        if section not in self._contents: raise TclError(f'{self} - not found: "{section}".')
        order, labels = self._contents[section][1:]
        if separator not in labels: raise TclError(f'{self}:{section} - not found: "{separator}".')

        row = order.index(separator)
        order.remove(separator)
        labels.pop(separator).destroy()

        self._rearrangeLabels(labels, order, row)
        
    # OPTIONS
    def option_add(self, section: str, label: str, widget: Widget) -> str:
        '''Add option widget to label.'''
        if section not in self._contents: raise TclError(f'{self} - not found: "{section}".')
        sectionFrame, order, labels = self._contents[section]
        if label not in labels: raise TclError(f'{self}:{section} - not found: "{label}".')

        optionFrame, options = labels[label][1:]
        widget.pack(side=TOP, fill=X, padx=5, pady=5, in_=optionFrame)
        tag = label + str(id(widget))
        options[tag] = (widget, {})
        return tag
        
    def option_insert(self, section: str, label: str, before: str, widget: Widget) -> str:
        '''Insert option widget before given option to label.'''
        if section not in self._contents: raise TclError(f'{self} - not found: "{section}".')
        sectionFrame, order, labels = self._contents[section]
        if label not in labels: raise TclError(f'{self}:{section} - not found: "{label}".')
        optionFrame, options = labels[label][1:]
        if before not in options: raise TclError(f'{self}:{section}:{label} - not found: "{before}".')

        widget.pack(side=TOP, fill=X, padx=5, pady=5, in_=optionFrame, before=options[before][0])
        tag = label + str(id(widget))
        options[tag] = (widget, {})
        return tag
        
    def option_move(self, section: str, label: str, before: str, option: str):
        '''Move option before given option.'''
        if section not in self._contents: raise TclError(f'{self} - not found: "{section}".')
        sectionFrame, order, labels = self._contents[section]
        if label not in labels: raise TclError(f'{self}:{section} - not found: "{label}".')
        options = labels[label][2]
        if option not in options: raise TclError(f'{self}:{section}:{label} - not found: "{option}".')
        if before not in options: raise TclError(f'{self}:{section}:{label} - not found: "{before}".')

        options[option][0].pack(before=options[before][0])
        
    def option_remove(self, section: str, label: str, option: str):
        '''Remove option from label completely.'''
        if section not in self._contents: raise TclError(f'{self} - not found: "{section}".')
        sectionFrame, order, labels = self._contents[section]
        if label not in labels: raise TclError(f'{self}:{section} - not found: "{label}".')
        options = labels[label][2]
        if option not in options: raise TclError(f'{self}:{section}:{label} - not found: "{option}".')

        options.pop(option)[0].pack_forget()

    def option_get(self, section: str, label: str, option: str) -> Widget:
        '''Get the assigned widget'''
        if section not in self._contents: raise TclError(f'{self} - not found: "{section}".')
        sectionFrame, order, labels = self._contents[section]
        if label not in labels: raise TclError(f'{self}:{section} - not found: "{label}".')
        options = labels[label][2]
        if option not in options: raise TclError(f'{self}:{section}:{label} - not found: "{option}".')

        return options[option][0]
        
    def option_hide(self, section: str, label: str, option: str):
        '''Tempoarely remove option widget from label.'''
        if section not in self._contents: raise TclError(f'{self} - not found: "{section}".')
        sectionFrame, order, labels = self._contents[section]
        if label not in labels: raise TclError(f'{self}:{section} - not found: "{label}".')
        optionFrame, options = labels[label][1:]
        if option not in options: raise TclError(f'{self}:{section}:{label} - not found: "{option}".')
        widget, packOptions = options[option]
        if packOptions: raise TclError(f'{self}:{section}:{label} - "{option}" is already hidden.')
        
        newPackOptions = widget.pack_info()
        slaves = optionFrame.pack_slaves()
        if widget != slaves[-1]: newPackOptions['before'] = slaves[slaves.index(widget) + 1]
        packOptions.update(newPackOptions)
        widget.pack_forget()
        
    def option_show(self, section: str, label: str, option: str):
        '''Restore option widget on label.'''
        if section not in self._contents: raise TclError(f'{self} - not found: "{section}".')
        sectionFrame, order, labels = self._contents[section]
        if label not in labels: raise TclError(f'{self}:{section} - not found: "{label}".')
        labelWidget, optionFrame, options = labels[label]
        if option not in options: raise TclError(f'{self}:{section}:{label} - not found: "{option}".')
        widget, packOptions = options[option]
        if not packOptions: raise TclError(f'{self}:{section}:{label} - "{option}" is not hidden.')

        widget.pack(packOptions)
        packOptions.clear()

    def option_replace(self, section: str, label: str, option: str, widget: Widget) -> str:
        '''Replace option widget.
        
        Returns new tag because internally the old option
        gets removed and the new one inserted.'''
        if section not in self._contents: raise TclError(f'{self} - not found: "{section}".')
        sectionFrame, order, labels = self._contents[section]
        if label not in labels: raise TclError(f'{self}:{section} - not found: "{label}".')
        labelWidget, optionFrame, options = labels[label]
        if option not in options: raise TclError(f'{self}:{section}:{label} - not found: "{option}".')
        
        packOptions = {'side': TOP, 'fill': BOTH, 'padx': 5, 'pady': 5, 'in_': optionFrame}
        slaves = optionFrame.pack_slaves()
        oldWidget = options.pop(option)[0]
        if oldWidget != slaves[-1]: packOptions['before'] = slaves[slaves.index(oldWidget) + 1]
        oldWidget.pack_forget()
        widget.pack(packOptions)
        tag = label + str(id(widget))
        options[tag] = (widget, {})

        return tag
        
    # OVERALL
    def setting_hide(self, section: str, label: str):
        '''Temporarely remove whole label and options.'''
        if section not in self._contents: raise TclError(f'{self} - not found: "{section}".')
        sectionFrame, order, labels = self._contents[section]
        if label not in labels: raise TclError(f'{self}:{section} - not found: "{label}".')
        settingLabel, optionFrame = labels[label][:2]
        if not settingLabel.winfo_ismapped(): raise TclError(f'{self}:{section} - "{label}" is already hidden.')

        settingLabel.grid_remove()
        optionFrame.grid_remove()
        
    def setting_show(self, section: str, label: str):
        '''Restore whole label and options.'''
        if section not in self._contents: raise TclError(f'{self} - not found: "{section}".')
        sectionFrame, order, labels = self._contents[section]
        if label not in labels: raise TclError(f'{self}:{section} - not found: "{label}".')
        settingLabel, optionFrame = labels[label][:2]
        if settingLabel.winfo_ismapped(): raise TclError(f'{self}:{section} - "{label}" is not hidden.')

        settingLabel.grid()
        optionFrame.grid()

    @event
    def hide(self):
        '''Temporarely remove settings window.'''
        self.grab_release()
        self.withdraw()
        if self._hidecommand: self._hidecommand()
        self.master.focus()

    @event
    def show(self):
        '''Redraw settings window.'''
        self.deiconify()
        self.grab_set()
        if self._showcommand: self._showcommand()
        self.focus()

    def clear(self):
        '''Remove all sections, labels and options.'''
        for section in self._contents:
            self._contents[section][0].master.destroy()
        self._contents.clear()

    @property
    def layout(self):
        '''Returns inner layout of Settings.
        
        {section: {label: (option, ..., option), ...}, ...}'''
        layout = {}
        for section in self._contents:
            sectionLayout = {}
            sectionContent = self._contents[section][2]
            for label in sectionContent:
                if label.startswith('<Separator>'): sectionLayout[label] = None
                else: sectionLayout[label] = tuple(sectionContent[label][2].keys())
            layout[section] = sectionLayout
        return layout
    @layout.setter
    def layout(self, layout):
        '''Create contents from layout.
        All previous contents will get cleared.'''
        self.clear()
        for section in layout:
            self.section_add(section)
            sectionLayout = layout[section]
            for label in sectionLayout:
                if label == '<Separator>': self.separator_add(section)
                else:
                    self.label_add(section, label)
                    for widget in sectionLayout[label]: self.option_add(section, label, widget)

    def _rearrangeLabels(self, labels: dict, order: list, row: int):
        '''Internal function'''
        for row in range(row, len(order)):
            tag = order[row]
            if tag.startswith('<Separator>'): labels[tag].grid(row=row)
            else:
                settingLabel, optionFrame = labels[tag][:2]
                settingLabel.grid(row=row)
                optionFrame.grid(row=row)

    def _checkcnf(self, cnf):
        for key in cnf:
            if key not in self._PASS: raise TclError(f'Unknown option "-{key}"')

    @staticmethod
    def prettyLayout(layout, baseindent=0):
        string = ' ' * baseindent + '{'
        indent = baseindent + 1
        sectionStrings = []
        for section in layout:
            sectionLayout = layout[section]
            sectionIndent = len(section) + 5
            indent += sectionIndent
            sectionString = repr(section) + ': {'
            labelStrings = []
            for label in sectionLayout:
                labelIndent = len(label) + 5
                labelLayout = sectionLayout[label]
                if labelLayout: labelStrings.append(repr(label) + ': (' + (',\n' + ' ' * (indent + labelIndent)).join(labelLayout) + ')')
                else: labelStrings.append(repr(label) + ': None')
            sectionString += (',\n' + ' ' * indent).join(labelStrings) + '}'
            indent -= sectionIndent
            sectionStrings.append(sectionString)
        string += (',\n' + ' ' * indent).join(sectionStrings) + '}'
        return string

    # STANDARDS
    def config(self, cnf={}, **kw):
        '''Configure resources of a widget.

        The values for resources are specified as keyword
        arguments. To get an overview about
        the allowed keyword arguments call the method keys.'''
        if (cnf or kw):
            cnf, extras = filtercnf(cnf, kw, *self._EXTRAS)
            super().config(cnf)
            self.__dict__.update(extras)
            if 'styleprefix' in extras: self._styleprefix += '.'
            if 'middlepadding' in extras:
                for contents in self._contents.values(): contents[0].columnconfigure(1, minsize=self._middlepadding)
            if 'buttons' in extras:
                if self._buttons:
                    for text, command in self._buttons:
                        ttk.Button(self._buttonFrame, style=self._styleprefix + 'TButton', text=text, command=command).pack(fill=Y, side=LEFT, padx=5)
                    self._buttonBase.pack(side=BOTTOM, fill=X, anchor=self._buttonanchor)
                else: self._buttonBase.pack_forget()
            elif 'buttonanchor' in extras and self._buttonBase.winfo_ismapped(): self._buttonBase.pack(anchor=self._buttonanchor)
        else:
            cnf = super().config()
            cnf.update({'styleprefix': ('styleprefix', None, None, 'Settings', self._styleprefix[:-1]),
                        'middlepadding': ('middlepadding', None, None, 0, self._middlepadding),
                        'buttons': ('buttons', None, None, (), self._buttons),
                        'buttonanchor': ('buttonanchor', None, None, CENTER, self._buttonanchor),
                        'hidecommand': ('hidecommand', None, None, None, self._hidecommand),
                        'showcommand': ('showcommand', None, None, None, self._showcommand),
                        'width': ('width', 'width', 'Width', 650, super().cget('width')),
                        'height': ('height', 'height', 'Height', 700, super().cget('height'))})
            return cnf

    configure = config

    def cget(self, key):
        '''Return the resource value for a KEY given as string.'''
        if key == 'styleprefix': return self._styleprefix[:-1]
        elif key in self._EXTRAS: return getattr(self, '_' + key)
        elif key in self._PASS: return super().cget(key)
        else: raise TclError(f'unknown option "-{key}"')

    @classmethod
    def keys(cls):
        '''Return a list of all resource names of this widget.'''
        return cls._PASS + cls._EXTRAS

    # __MAGIC__
    def __getitem__(self, key):
        if isinstance(key, slice):
            if key.start and key.stop and key.step:
                return self._contents[key.start][2][key.stop][2][key.step][0]
            elif key.start and key.stop:
                if not key.stop.startswith('<Separator>'): return tuple(self._contents[key.start][2][key.stop][2].keys())
            elif key.start:
                return tuple(self._contents[key.start][2].keys())
            elif not (key.start or key.stop or key.step):
                return tuple(self._contents)
            else:
                raise TclError(f'Can\'t resolve slice {key}.')
        else:
            return self.cget(key)

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            if key.start and key.stop and key.step:
                self.option_replace(key.start, key.stop, key.step, value)
            elif key.start and key.stop:
                self.label_rename(key.start, key.stop, value)
            elif key.start:
                self.section_rename(key.start, value)
            elif not (key.start or key.stop or key.step): #poissible but what's the use?
                self.layout = value
            else:
                raise TclError(f'Can\'t resolve slice {key}.')
        else:
            return self.config({key: value})

class dtTEntry(ttk.Entry):
    '''Ttk Entry widget displays a one-line text string and allows that
    string to be edited by the user.
    This version conflicts with variables and validation.'''
    def __init__(self, master=None, widget=None, **kw):
        '''Constructs a Ttk Entry widget with the parent master.

        STANDARD OPTIONS

            class, cursor, style, takefocus, xscrollcommand

        WIDGET-SPECIFIC OPTIONS

            exportselection, invalidcommand, justify, show, state,
            textvariable, validate, validatecommand, width, text

        VALIDATION MODES (validation is depreciated to use for this specific widget)

            none, key, focus, focusin, focusout, all'''
        cnf, extracted = filtercnf(kw, None, style='TEntry', text='')
        ttk.Entry.__init__(self, master, widget, **cnf, style='texted.TEntry')
        self.__dict__.update({'_' + key: value for key, value in extracted.items()})

        super().insert(0, self._text)
        self._gotSet = True
        
        self.bind('<FocusIn>', self._focusIn, True)
        self.bind('<FocusOut>', self._focusOut, True)
        self.bind('<Control-BackSpace>', self._del, True)
        self.bind('<Control-Delete>', self._del, True)

    def _del(self, event):
        '''Internal function'''
        pos = startPos = self.index(INSERT)
        text = super().get()
        if text == '': return
        if event.keysym=='BackSpace':
            while pos > 0 and text[pos - 1] == ' ': pos -= 1
            while pos > 0 and text[pos - 1] not in (' ', '\t'): pos -= 1
            super().delete(pos, startPos)
        else:
            endPos = self.index(END) - 1
            while pos < endPos and text[pos + 1] == ' ': pos += 1
            while pos < endPos and text[pos + 1] not in (' ', '\t'): pos += 1
            super().delete(startPos, pos)
    def _focusIn(self, event):
        '''Internal function.'''
        if self._gotSet:
            super().delete(0, END)
            super().config(style=self._style)
            self._gotSet = False
    def _focusOut(self, event):
        '''Internal function.'''
        if not super().get():
            super().insert(0, self._text)
            super().config(style='texted.TEntry')
            self._gotSet = True
        else: self._gotSet = False
    def get(self):
        '''Return the text.'''
        if self._gotSet: return ''
        else: return super().get()
    def insert(self, index, string):
        '''Insert STRING at INDEX.'''
        if self._gotSet and string!='':
            super().delete(0, END)
            super().insert(index, string)
            super().config(style=self._style)
    def delete(self, first, last=None):
        '''Delete text from FIRST to LAST (not included).'''
        super().delete(first, last)
        if not super().get():
            super().insert(0, self._text)
            super().config(style='texted.TEntry')
            self._gotSet = True
    def config(self, cnf=None, **kw):
        '''Configure resources of a widget.

        The values for resources are specified as keyword
        arguments. To get an overview about
        the allowed keyword arguments call the method keys.'''
        cnf, extra = filtercnf(kw, None, 'style', 'text')
        self.__dict__.update({'_' + key: value for key, value in extracted.items()})
        if 'text' in extra and self._gotSet:
            super().delete(0, END)
            super().insert(0, self._text)
        if 'style' in extra and not self._gotSet:
            super().config(style=self._style)
    configure = config
    def cget(key):
        '''Return the resource value for a KEY given as string.'''
        if key == 'text': return self._text
        elif key == 'style': return self._style
        else: return super().cget(key)
    __getitem__ = cget
    def keys(self):
        '''Return a list of all resource names of this widget.'''
        return self.keys() + ['text']

class dTEntry(ttk.Entry):
    '''Ttk Entry widget displays a one-line text string and allows that
    string to be edited by the user.
    This version conflicts with variables and validation.'''
    def __init__(self, master=None, widget=None, **kw):
        '''Constructs a Ttk Entry widget with the parent master.

        STANDARD OPTIONS

            class, cursor, style, takefocus, xscrollcommand

        WIDGET-SPECIFIC OPTIONS

            exportselection, invalidcommand, justify, show, state,
            textvariable, validate, validatecommand, width

        VALIDATION MODES (validation is depreciated to use for this specific widget)

            none, key, focus, focusin, focusout, all'''
        ttk.Entry.__init__(self, master, widget, **kw)

        self.bind('<Control-BackSpace>', self._del, True)
        self.bind('<Control-Delete>', self._del, True)

    def _del(self, event):
        '''Internal function'''
        pos = startPos = self.index(INSERT)
        text = self.get()
        if text == '': return
        if event.keysym=='BackSpace':
            while pos > 0 and text[pos - 1] == ' ': pos -= 1
            while pos > 0 and text[pos - 1] not in (' ', '\t'): pos -= 1
            self.delete(pos, startPos)
        else:
            endPos = self.index(END) - 1
            while pos < endPos and text[pos + 1] == ' ': pos += 1
            while pos < endPos and text[pos + 1] not in (' ', '\t'): pos += 1
            self.delete(startPos, pos)

class PseudoNotebook(Frame):
    _REMOVE = ('class', 'colormap', 'container', 'visual', 'state')
    _PASS = ('bd', 'borderwidth', 'relief', 'background', 'bg','cursor', 'height', 'highlightbackground', 'highlightcolor', 'padx', 'highlightthickness', 'takefocus','width')
    _PASSLABEL = ('foreground', 'anchor', 'compound', 'font', 'justify', 'bitmap', 'image', 'text', 'textvariable', 'underline', 'wraplength', 'disabledforeground')
    _LABEL = ('text', 'textvariable', 'bitmap', 'image', 'state')
    _EXTRA = ('buttoncursor', 'tabbackground', 'pady', 'addcommand', 'selectcommand', 'closecommand')
    def __init__(self, master=None, cnf={}, **kw):
        '''Construct a pseudo Notebook with parent master.

                OPTIONS

                    see PseudoNotebook.keys()

                TAB OPTIONS

                    text, textvariable, bitmap, image, state

                TAB IDENTIFIERS (TagOrID)

                    The tab_id argument found in several methods may take any of
                    the following forms:

                        * An integer between zero and the number of tabs
                        * A tag like "tab#0"
                        * The string "end", which returns the number of tabs (only
                          valid for method index)'''
        cnf, du = filtercnf(cnf, kw, buttoncursor='hand2', tabbackground='white', pady=5, addcommand=None, selectcommand=None, closecommand=None)
        cnf, self._labelcnf = filtercnf(cnf, None, *self._PASSLABEL)
        checkcnf(cnf, self._REMOVE)
        self.__dict__.update({'_'+option: value for option, value in du.items()})
        Frame.__init__(self, master, cnf)
        self._background = super().cget('bg')
        self.pack_propagate(False)

        self._tabcounter = 0
        self._focused = None
        self._prevFocus = None
        self._lastFocus = None
        self._grabbed = None
        self._tabs = {}
        self._window = self._root()
        self._offset = 0
        self._tilewidth = 0
        
        self._ghost = Frame(self)
        self._ghost.pack_propagate(False)
        self._ghost.separator = Frame(self._ghost)
        self._ghost.separator.pack_propagate(False)
        ttk.Separator(self._ghost.separator, orient=VERTICAL).pack(fill=Y, expand=True)
        self._ghost.separator.pack(side=RIGHT, fill=Y, pady=5)

        self._topspacer = Frame(self, bg=self._background, height=self._pady)
        self._topspacer.pack(side=TOP, fill=X)

        self._leftspacer = Frame(self, bg=self._background, width=self._tilewidth)
        self._leftspacer.separator = Store(grid_remove=lambda: self._leftspacer.config(width=1),
                                           grid=lambda: self._leftspacer.config(width=self._tilewidth)) #Imitate tab separator layout/behaviour
        self._leftspacer.pack(fill=Y, side=LEFT)

        self._addframe = Frame(self, bg=self._background)
        self._addframe.pack(fill=Y, side=LEFT)
        self._add = CustomButton(self._addframe, form=CustomButton.PLUS, activecolor='blue', color='gainsboro', irelheight=1/3, command=self._addcommand,
                                disabledcolor='#e6e6e6', background=self._background, bd=0, cursor=self._buttoncursor, activebackground=self._background, width=20)
        self._add.pack(fill=Y)

        self.bind('<Configure>', self._configSides)

        self._clickID = self._window.bind('<ButtonPress-1>', self._press, True)
        self._dragID = self._window.bind('<Button1-Motion>', self._drag, True)
        self._releaseID = self._window.bind('<ButtonRelease-1>', self._release, True)
        self._closeID = self._window.bind('<Button-2>', self._eventDel, True)

        self.update()

    def addTab(self, cnf={}, **kw) -> str: #text, textvar, bitmap, image, state
        '''Adds a tab with the given attributes and focuses it.'''
        overflow, kw = filtercnf(cnf, kw, *self._LABEL)
        if overflow: raise TclError('unknown option "-%s"'%tuple(overflow.keys())[0])
        if 'state' not in kw: kw['state']=NORMAL
        tag = 'tab#%i'%self._tabcounter
        self._tabcounter+=1

        tab = Frame(self, bg=self._tabbackground)
        tab.rowconfigure(0, weight=1)
        tab.columnconfigure((0, 3), uniform='sides')
        tab.columnconfigure(4, weight=1)
        tab.tag = tag

        tab.left = Canvas(tab, bg=self._background, highlightthickness=0, width=10)
        tab.left.grid(row=0, column=0, sticky=NSEW)
        tab.left.grid_remove()
        tab.right = Canvas(tab, bg=self._background, highlightthickness=0, width=10)
        tab.right.grid(row=0, column=3, sticky=NSEW)
        tab.right.grid_remove()

        tab.label = Label(tab, cnf=self._labelcnf, background=self._tabbackground, **kw)
        tab.label.grid(row=0, column=1, sticky=NSEW)

        tab.x = CustomButton(tab, form=CustomButton.CROSS, activecolor='red', color='gainsboro', command=self._del, disabledcolor='#e6e6e6', background=self._tabbackground,
                                 bd=0, cursor=self._buttoncursor, irelheight=1/5, width=20, state=kw['state'], args=(tab,), highlightthickness=0, activebackground=self._tabbackground)
        tab.x.grid(row=0, column=2, sticky=NS)

        tab.separator = Frame(tab, bg=self._background)
        tab.separator.pack_propagate(False)
        ttk.Separator(tab.separator, orient=VERTICAL).pack(fill=Y, expand=True)
        tab.separator.grid(row=0, column=4, sticky=NS, pady=5)
        tab.separator.grid_remove()
        tab.pack(fill=Y, side=LEFT, before=self._addframe)
            
        tab.update()
        height = tab.winfo_height()
        radius = height//4
        self._tilewidth = 2 * radius

        tab.left.config(width=self._tilewidth)
        tab.separator.config(width=self._tilewidth)

        tab.left.create_polygon(radius, radius, 2*radius, radius, 2*radius, height, 0, height, 0, 3*radius, radius, 3*radius, width=0, fill=self._tabbackground, tags=(CENTER, ALL))
        tab.left.create_arc(-radius, 2*radius, radius, height, fill=self._background, outline=self._background, start=270, tag=(TOP, ALL))
        tab.left.create_arc(radius, 0, 3*radius-2, 2*radius, fill=self._tabbackground, outline=self._tabbackground, start=90, tag=(BOTTOM, ALL))
        tab.right.create_polygon(0, radius, radius, radius, radius, 3*radius, 2*radius, 3*radius, 2*radius, height, 0, height, width=0, fill=self._tabbackground, tag=(CENTER, ALL))
        tab.right.create_arc(-radius, 0, radius-1, 2*radius, fill=self._tabbackground, outline=self._tabbackground, tag=(TOP, ALL))
        tab.right.create_arc(radius, 2*radius, 3*radius, height, fill=self._background, outline=self._background, start=180, tag=(BOTTOM, ALL))

        self._tabs[tag] = tab
        self._focus(tab)

        return tag

    def configTab(self, posOrID, cnf=None, **kw) -> dict:
        ''''''
        cnf = cnfmerge((cnf, kw))
        if cnf:
            overflow, kw = filtercnf(cnf, None, *self._LABEL)
            if overflow: raise TclError('unknown option "-%s"'%tuple(overflow.keys())[0])

            tab = self._getTab(posOrID)
            tab.label.config(kw)
            if 'state' in kw:
                tab.x.config(state=kw['state'])
                tab.label.config(state=kw['state'])
        else:
            return {key: value for key, value in self._getTab(posOrID).label.config() if key in self._LABEL}

    def cgetTab(self, posOrID, key):
        if key not in self._LABEL: raise TclError('unknown option "-%s"'%key)

        return self._getTab(posOrID).label.cget(key)

    @classmethod
    def tabKeys(cls):
        return self._LABEL

    def getPos(self, ID):
        return self.pack_slaves().index(self._getTab(ID))

    def getID(self, pos):
        return self.pack_slaves()[pos if pos != END else -2].tag

    def _configSides(self, event):
        if self._focused: self._focused.update()
        else: return 'break'

        height = self._focused.winfo_height()
        radius = height//4
        self._tilewidth = 2 * radius

        for widget in self.pack_slaves()[2: -1]:
            widget.left.config(width=self._tilewidth)
            widget.separator.config(width=self._tilewidth)

            widget.left.coords(CENTER, radius, radius, 2*radius, radius, 2*radius, height, 0, height, 0, 3*radius, radius, 3*radius)
            widget.left.coords(TOP, -radius, 2*radius, radius, height)
            widget.left.coords(BOTTOM, radius, 0, 3*radius-2, 2*radius)
            widget.right.coords(CENTER, 0, radius, radius, radius, radius, 3*radius, 2*radius, 3*radius, 2*radius, height, 0, height)
            widget.right.coords(TOP, -radius, 0, radius-1, 2*radius)
            widget.right.coords(BOTTOM, radius, 2*radius, 3*radius, height)
            
            widget.update()

    def moveTab(self, tab, posOrID=END, focus=True):
        if type(posOrID) == int: before = self.pack_slaves()[posOrID + 2]
        elif posOrID == END: before = self._addframe
        else: before = self._tabs[posOrID]

        self._move(self._getTab(tab), before)

    def _move(self, tab: Widget, before: Widget, _focus=True):
        if self._prevFocus and tab == self._focused: self._prevFocus.separator.grid()
        tab.pack(before=before, side=LEFT, fill=Y)

        if _focus: self._focus(self._focused)

    def delTab(self, posOrID):
        self._del(self._getTab(posOrID))

    def _eventDel(self, event):
        if type(event.widget) in (ttk.Separator): return 'break'
        for tab in self.pack_slaves()[2:-1]:
            if event.widget in tab:
               if tab.label.cget('state') == NORMAL: break
               return 'break'
        else: return 'break'

        self._del(tab)

    def _del(self, tab):
        if self._closecommand and not self._closecommand(tab.tag): return

        slaves = self.pack_slaves()
        pos = slaves.index(tab)

        if self._focused == tab:
            if self._prevFocus: self._prevFocus.separator.grid()
            self._findNewFocus()
        elif slaves[pos + 1] == self._focused: slaves[pos - 1].separator.grid_remove()

        if self._lastFocus == tab: self._lastFocus = None

        tab.destroy()
        del self._tabs[tab.tag]

    def focusTab(self, posOrID):
        self._focus(self._getTab(posOrID))
    
    def _focus(self, tab):
        if self._selectcommand and not self._selectcommand(tab.tag): return

        if self._focused != tab: self._lastFocus, self._focused = self._focused, tab

        slaves = self.pack_slaves()

        #remove old
        if self._lastFocus:
            if self._prevFocus: self._prevFocus.separator.grid()
            self._lastFocus.left.grid_remove()
            self._lastFocus.right.grid_remove()
            self._lastFocus.separator.grid()
            self._lastFocus['bg'] = self._lastFocus.label['bg'] = self._lastFocus.x['bg'] = self._lastFocus.x['activebackground'] = self._background

        #add new
        self._prevFocus = slaves[slaves.index(self._focused) - 1]
        if self._prevFocus == self._topspacer: self._prevFocus = None
        else:
            self._prevFocus.separator.grid_remove()
            print(self._prevFocus.winfo_width())
        self._focused.left.grid()
        self._focused.right.grid()
        self._focused.separator.grid_remove()
        self._focused['bg'] = self._focused.label['bg'] = self._focused.x['bg'] = self._focused.x['activebackground'] = self._tabbackground
        self._focused.lift()
        self._focused.update()
    
    def _findNewFocus(self):
        slaves = self.pack_slaves()
        pos = slaves.index(self._focused)
        self._focused = None

        if self._lastFocus: self._focus(self._lastFocus)
        elif slaves[pos + 1] != self._addframe: self._focus(slaves[pos + 1])
        elif self._prevFocus and self._prevFocus != self._leftspacer: self._focus(self._prevFocus)

    def _press(self, event):
        if type(event.widget) in (CustomButton, ttk.Separator): return 'break'
        for tab in self.pack_slaves()[2:-1]:
            if event.widget in tab:
               if tab.label.cget('state') == NORMAL: break
               return 'break'
        else: return 'break'

        tab.update()
        self._focus(tab)
        if self._prevFocus: self._prevFocus.separator.grid()

        self._grabbed = tab

        self._offset = event.x_root - tab.winfo_rootx()
        width, tilewidth = tab.winfo_width(), tab.right.winfo_width()

        self._ghost.config(bg=self._background, width=width - tilewidth)
        self._ghost.separator.config(width=tilewidth)
        self._ghost.pack(side=LEFT, fill=Y, before=tab)

        tab.place(height=tab.winfo_height(), width=width, x=event.x_root-(self._offset+self.winfo_rootx()), anchor=SW, rely=1)

        self._add.pack_forget()

        return 'break'

    def _drag(self, event):
        widget = event.widget
        if self._grabbed and widget in self._grabbed:
            if type(widget) != Frame: widget = widget.master
            if widget != self._focused: return
            rootx = self.winfo_rootx()

            x = event.x_root - (self._offset + rootx)
            if x < 0: x = 0
            widget.place(x=x)

            x = event.x_root - rootx
            if x < self._tilewidth: self._ghost.pack(after=self._leftspacer)
            else: 
                for tab in self.pack_slaves()[2:-1]:
                    tabx, tabwidth = tab.winfo_x(), tab.winfo_width()
                    if tabx <= x <= tabx + tabwidth: break
                if tab == self._ghost: return 'break'
                if x >= tabx + tabwidth//2: self._ghost.pack(after=tab)
                else: self._ghost.pack(before=tab)

            return 'break'

    def _release(self, event):
        widget = event.widget
        if self._grabbed and widget in self._grabbed:
            if type(widget) != Frame: widget = widget.master
            if widget != self._focused: return

            widget.pack(side=LEFT, fill=Y, before=self._ghost)
            self._ghost.pack_forget()
            self._focus(widget)
            self._add.pack(fill=Y)

            return 'break'

    def _getTab(self, posOrID) -> Widget:
        if type(posOrID) == int: return self.pack_slaves()[posOrID + 2]
        elif posOrID == END: return self.pack_slaves()[-2]
        else: return self._tabs[posOrID]

    def config(self, cnf={}, **kw):
        cnf = cnfmerge((cnf, kw))
        if cnf:
            cnf, du = filtercnf(cnf, None, *self._PASS)
            cnf, self._labelcnf = filtercnf(cnf, None, *self._PASSLABEL)
            checkcnf(cnf, self._REMOVE)

            if 'tabbackground' in du or 'bg' in cnf or 'buttoncursor' in du:
                if 'tabbackground' in du: tabbg = du['tabbackground']
                else: tabbg = self._tabbackground

                if 'bg' in cnf:
                    bg = cnf['bg']
                    self['bg'] = self._ghost['bg'] = self._topspacer['bg'] = self._leftspacer['bg'] = self._addframe['bg'] = self._add['bg'] = bg
                else: bg = self._background

                if 'buttoncursor' in du:
                    btncursor = du['buttoncursor']
                    self._add.config(cursor=btncursor)
                else: btncursor = self._buttoncursor

                for tab in self._tabs.values():
                    tab.left.config(bg=bg)
                    tab.right.config(bg=bg)
                    tab.separator.config(bg=bg)
                    tab.left.itemconfig(ALL, fill=bg, outline=bg)
                    tab.right.itemconfig(ALL, fill=bg, outline=bg)
                    tab.config(bg=tabbg)
                    tab.label.config(bg=tabbg)
                    tab.x.config(bg=tabbg, cursor=btncursor)

            if 'addcommand' in du: self._add.config(command=du['addcommand'])
            if 'pady' in du: self._topspacer.config(height=du['pady'])
            self.__dict__.update({'_'+option: value for option, value in du.items()})

        else:
            cnf = {'buttoncursor': ('buttoncursor', '', '', 'hand2', self._buttoncursor),
                   'tabbackground': ('tabbackground', '', '', 'white', self._tabbackground),
                   'pady': ('pady', '', '', 5, self._pady),
                   'addcommand': ('addcommand', '', '', None, self._addcommand),
                   'closecommand': ('closecommand', '', '', None, self._closecommand),
                   'selectcommand': ('selectcommand', '', '', None, self._selectcommand)}

            cnf.update({key: value for key, value in super().config() if key in self._PASS})
            if self._tabs: cnf.update({key: value for key, value in tuple(self._tabs.values())[0].config() if key in self._LABELPASS})

            return cnf

    def cget(self, key):
        if key in self._PASS: return super().cget(key)
        elif key in self._PASSLABEL:
            if self._tabs: return tuple(self._tabs.values())[0].cget(key)
            else: raise TclError("No tab created")
        elif key in self._EXTRA: return self.__dict__['_' + key]
        else: raise TclError('no option "-%s"'%key)
    __getitem__ = cget
    @classmethod
    def keys(cls):
        return cls._PASS + cls._PASSLABEL + cls._EXTRA
