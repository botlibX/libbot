# This file is placed in the Public Domain.
#
# pylint: disable=C0116,E0402


"list of commands"


from bot.reacts import Reactor


def cmd(event):
    event.reply(",".join(sorted(Reactor.cmds)))
