# This file is placed in the Public Domain.
#
# pylint: disable=W0611,W0614,W0401,E0402,E0611


"the python3 bot namespace"


from . import broker, client, errors, events, handle, method, object
from . import config, parser, repeat, stores, thread, timers, extras


from .broker import *
from .client import *
from .config import *
from .errors import *
from .events import *
from .locate import *
from .handle import *
from .events import *
from .method import *
from .object import *
from .parser import *
from .repeat import *
from .runner import *
from .stores import *
from .thread import *
from .timers import *
from .extras import *


def __dir__():
    return (
            'Broker',
            'Cfg',
            'Client',
            'Default',
            'Errors',
            'Event',
            'Handler',
            'Object',
            'Repeater',
            'Storage',
            'Thread',
            'cdir',
            'command',
            'construct',
            'edit',
            'fetch',
            'find',
            'fntime',
            'fqn',
            'ident',
            'items',
            'keys',
            'laps',
            'last',
            'launch',
            'mods',
            'name',
            'output',
            'parse',
            'read',
            'scan',
            'search', 
            'shutdown',
            'spl',
            'strip',
            'sync',
            'update',
            'values',
            'write'
           )
