# This file is placed in the Public Domain.
#
# pylint: disable=W0611,W0614,W0401,E0402,E0611


"the python3 bot namespace"


from . import brokers, censors, clients, handler, message, methods, objects
from . import repeats, storage, threads, timings, utility


from .brokers import *
from .censors import *
from .clients import *
from .errored import *
from .finding import *
from .handler import *
from .message import *
from .methods import *
from .objects import *
from .repeats import *
from .scanner import *
from .storage import *
from .threads import *
from .timings import *
from .utility import *


def __dir__():
    return (
            'Broker',
            'Cfg',
            'Client',
            'Default',
            'Errors',
            'Handler',
            'Message',
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
