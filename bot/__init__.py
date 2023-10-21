# This file is placed in the Public Domain.
#
# pylint: disable=W0611,W0614,W0401,E0402,E0611


"the python3 bot namespace"


from . import broker, client, error, event, handler, method, object
from . import config, parse, persist, scan, thread, timer, utils


from .broker  import *
from .client  import *
from .config  import *
from .error   import *
from .event   import *
from .locate  import *
from .handler import *
from .method  import *
from .object  import *
from .parse   import *
from .persist import *
from .scan    import *
from .thread  import *
from .timer   import *
from .utils   import *


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
