#!/usr/bin/env python3
# This file is placed in the Public Domain.
#
# pylint: disable=C0412,C0115,C0116,W0212,R0903,C0207,C0413,W0611
# pylint: disable=C0411,E0402,E0611,C2801


"clientside"


from .brk import Broker
from .err import Errors, cprint
from .hdl import Handler
from .prs import parse


def __dir__():
    return (
            'CLI',
            'Console'
           )


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


class CLI(Client):

    def announce(self, txt):
        pass

    def raw(self, txt):
        cprint(txt)


class Console(CLI):

    def dispatch(self, evt):
        parse(evt)
        command(evt)
        evt.wait()


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
