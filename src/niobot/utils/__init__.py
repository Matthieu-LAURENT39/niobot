from .checks import *
from .federation import *
from .help_command import *
from .parsers import *
from .string_view import *
from .typing import *
from .unblocking import *


def deprecated(use_instead: str = None):
    """Marks a function as deprecated and will warn users on call."""
    import functools
    import warnings

    def wrapper(func):
        @functools.wraps(func)
        def caller(*args, **kwargs):
            value = "{} is deprecated.{}".format(
                func.__qualname__, "" if not use_instead else " Please use %r instead." % use_instead
            )
            warn = DeprecationWarning(value)
            warnings.warn(warn)
            return func(*args, **kwargs)

        caller.__doc__ = func.__doc__
        return caller

    return wrapper
