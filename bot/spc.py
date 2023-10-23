# This file is placed in the Public Domain.
#
# pylint: disable=W0611,W0614,W0401,E0402,E0611


"the python3 bot namespace"


from .all import *
from .brk import *
from .cfg import *
from .clt import *
from .err import *
from .fnd import *
from .hdl import *
from .evt import *
from .fnc import *
from .obj import *
from .prs import *
from .scn import *
from .dsk import *
from .thr import *
from .tme import *
from .utl import *


def __dir__():
    return (
            'Broker',
            'Censor',
            'Cfg',
            'Client',
            'CLI',
            'Console',
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
