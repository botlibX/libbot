# This file is placed in the Public Domain.
#
# pylint: disable=C0115,C0116,E0402,W0718,W0212,W0613


"handler"


import inspect
import queue
import threading
import _thread


from .broker import Broker
from .error  import Errors
from .event  import Event
from .object import Object
from .thread import launch


def __dir__():
    return (
            'Client',
            'Handler',
            'command'
           )


class Handler(Object):

    cmds = {}

    def __init__(self):
        Object.__init__(self)
        self.cbs     = Object()
        self.queue   = queue.Queue()
        self.stopped = threading.Event()
        self.end     = threading.Event()

    @staticmethod
    def add(func) -> None:
        Handler.cmds[func.__name__] = func

    def event(self, txt) -> Event:
        evt = Event()
        evt.txt = txt
        evt.orig = object.__repr__(self)
        return evt

    def forever(self) -> None:
        self.stopped.wait()

    def dispatch(self, evt) -> None:
        func = getattr(self.cbs, evt.type, None)
        if not func:
            evt.ready()
            return
        evt._thr = launch(func, evt)

    def loop(self) -> None:
        while not self.stopped.is_set():
            try:
                self.dispatch(self.poll())
            except (KeyboardInterrupt, EOFError):
                _thread.interrupt_main()

    def poll(self) -> Event:
        return self.queue.get()

    def put(self, evt) -> None:
        self.queue.put_nowait(evt)

    @staticmethod
    def scan(mod) -> None:
        for key, cmd in inspect.getmembers(mod, inspect.isfunction):
            if key.startswith("cb"):
                continue
            if 'event' in cmd.__code__.co_varnames:
                Handler.add(cmd)

    def register(self, typ, cbs) -> None:
        self.cbs[typ] = cbs

    def start(self) -> None:
        launch(self.loop)

    def stop(self) -> None:
        self.stopped.set()


class Client(Handler):

    def __init__(self):
        Handler.__init__(self)
        self.register("command", command)
        Broker.add(self)

    def announce(self, txt) -> None:
        self.raw(txt)

    def dosay(self, channel, txt) -> None:
        self.raw(txt)

    def raw(self, txt) -> None:
        pass


def command(evt) -> None:
    func = Handler.cmds.get(evt.cmd, None)
    if not func:
        evt.ready()
        return
    try:
        func(evt)
        evt.show()
    except Exception as ex:
        Errors.add(ex)
    evt.ready()