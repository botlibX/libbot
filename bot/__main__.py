# This file is placed in the Public Domain.
#
# pylint: disable=C0412,C0115,C0116,W0212,R0903,C0207,C0413,W0611
# pylint: disable=C0411,E0402,E0611,C2801


"runtime"


import getpass
import importlib
import os
import pwd
import readline
import shutil
import sys
import termios
import time
import threading
import traceback


from bot.spec import Broker, Censor, Cfg, Client, Errors, Event
from bot.spec import CLI, Handler, Storage
from bot.spec import command, cprint, daemon, debug, parse, scan, forever
from bot.spec import launch, mods, name, privileges, shutdown, spl


from bot import modules


Censor.output = print
Storage.workdir = Cfg.workdir


class Console(CLI):

    def dispatch(self, evt):
        parse(evt)
        command(evt)
        evt.wait()

    def poll(self) -> Event:
        return self.event(input("> "))


def wrap(func) -> None:
    old = None
    try:
        old = termios.tcgetattr(sys.stdin.fileno())
    except termios.error:
        pass
    try:
        func()
    except (EOFError, KeyboardInterrupt):
        print("")
        sys.stdout.flush()
    finally:
        if old:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old)


def main():
    parse(Cfg, " ".join(sys.argv[1:]))
    Cfg.mod = ",".join(modules.__dir__())
    if "n" in Cfg.opts:
        Cfg.commands = False
    if "d" in Cfg.opts:
        daemon(Cfg.pidfile)
    if "d" in Cfg.opts or "s" in Cfg.opts:
        privileges(Cfg.user)
        scan(modules, Cfg.mod, True)
        forever()
    elif "c" in Cfg.opts:
        dtime = time.ctime(time.time()).replace("  ", " ")
        if "v" in Cfg.opts:
            cprint(f"{Cfg.name.upper()} started at {dtime} {Cfg.opts.upper()} {Cfg.mod.upper()}")
        thrs = scan(modules, Cfg.mod, "x" not in Cfg.opts)
        if "w" in Cfg.opts:
            for thr in thrs:
                thr.join()
                cprint(f"ready {thr.name}")
        csl = Console()
        csl.start()
        csl.forever()
    else:
        cli = Console()
        scan(modules, Cfg.mod)
        evt = cli.event(Cfg.otxt)
        parse(evt)
        command(evt)
        evt.wait()


if __name__ == "__main__":
    wrap(main)
    shutdown()
