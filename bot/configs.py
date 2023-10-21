# This file is placed in the Public Domain.
#
# pylint: disable=E0402,C0115,R0903,W0201


"configuration"


from .objects import Default


def __dir__():
    return (
            'Config',
            'Cfg'
           )


class Config(Default):

    pass


Cfg = Config()
Cfg.commands = True
