from functools import wraps, WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES
from inspect import signature
import typing

def f_event(func: typing.Callable) -> typing.Callable:
    """
    Adds ignored event options to functioncall.
    
    This differs in no way from adding it manually.
    The whole purpose is to silently make it possible
    to use its methods as callbacks too.
    """

    @wraps(func)
    def event_wrapper(*_: typing.Tuple[typing.Any, ...]):
        return func();

    return event_wrapper;

def m_event(func: typing.Callable) -> typing.Callable:
    """
    Adds ignored event options to methodcall.
    
    This differs in no way from adding it manually.
    The whole purpose is to silently make it possible
    to use its methods as callbacks too.
    """

    #methods require class reference 'self'
    @wraps(func)
    def event_wrapper(self, *_: typing.Tuple[typing.Any, ...]):
        return func(self);

    return event_wrapper;

def exclude(*args: typing.Tuple[str, ...]) -> typing.Callable:
    """
    Exclude given arguments (as strings) from functions signature.
    """

    def decorator(function):
        sig = signature(function);
        function.__signature__ = sig.replace(parameters=(parameter for key, parameter in sig.parameters.items() if key not in args));

        return function;
    
    return decorator;

def wrapsAndExpand(original: typing.Callable, expansion: str,
                  assigned: typing.Tuple[str, ...] = WRAPPER_ASSIGNMENTS, updated: typing.Tuple[str, ...] = WRAPPER_UPDATES) -> typing.Callable:
    def wrapper(func: typing.Callable) -> typing.Callable: #mostly copies @wraps behavior
        try:
            doc = getattr(original, "__doc__");
        except AttributeError:
            setattr(func, "__doc__", expansion);
        else:
            setattr(func, "__doc__", doc + expansion);

        for attr in assigned:
            if attr == "__doc__": continue;

            try:
                value = getattr(original, attr);
            except AttributeError:
                pass
            else:
                setattr(func, attr, value);

        for attr in updated:
            getattr(func, attr).update(getattr(original, attr, {}));

        func.__wrapped__ = original;

        return func;
    
    return wrapper;

class Debugger:
    """
    Small custom Debugger to show function call stack.
    """
    def __init__(self, indent: int = 4, verbose: bool = True):
        """
        @param indent: Stack indent offset to be added/subtracted for each method.
        @param verbose: Wether or not to show in- and outputs too.
        """
        self.offset = indent;
        self.indent = 0;

        if verbose:
            self.addToDebug = self._addToDebug_verbose;
        else:
            self.addToDebug = self._addToDebug;
    
    @wraps(print)
    def print(self, *args, **kwargs):
        """
        Standard print with indent.
        """
        print(' ' * (self.indent + self.offset), *args, **kwargs);

    def _addToDebug_verbose(self, func: typing.Callable) -> typing.Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            self.indent += self.offset;
            print(' ' * self.indent, "START", func.__name__);

            return_value = func(*args, **kwargs);

            print(' ' * self.indent, "STOP", func.__name__);
            self.indent -= self.offset;

            return return_value;
        
        return wrapper;

    def _addToDebug_verbose(self, func: typing.Callable) -> typing.Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            self.indent += self.offset;
            print(' ' * self.indent, "START", func.__name__, "WITH", args, kwargs);

            return_value = func(*args, **kwargs);

            print(' ' * self.indent, "STOP", func.__name__, "WITH", return_value);
            self.indent -= self.offset;

            return return_value;
        
        return wrapper;