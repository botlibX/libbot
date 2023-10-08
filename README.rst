NAME

::

   LIBBOT - library to program bots


DESCRIPTION


::

    LIBBOT is a python3 library intended to be programmable  in a
    static, only code, no popen, no user imports and no reading
    modules from a directory, way. 

    LIBBOT provides a demo bot, it can connect to IRC, fetch and
    display RSS feeds, take todo notes, keep a shopping list
    and log text.


SYNOPSIS


::

    bot <cmd> [key=val] 
    bot <cmd> [key==val]
    bot [-c] [-d] [-v] [-i]


INSTALL


::

    $ pipx install libbot

USAGE


::

    for easy typing use an alias

    $ alias bot="python3 -m bot"

    list of commands

    $ bot cmd
    cmd,err,flt,sts,thr,upt

    start a console

    $ bot -c
    >

    list of modules

    $ bot mod
    bsc,err,flt,irc,log,mod,rss,shp,
    sts,tdo,thr,udp

    start as daemon

    $ bot -d
    $ 


CONFIGURATION


::

    irc

    $ bot cfg server=<server>
    $ bot cfg channel=<channel>
    $ bot cfg nick=<nick>

    sasl

    $ bot pwd <nsvnick> <nspass>
    $ bot cfg password=<frompwd>

    rss

    $ bot rss <url>
    $ bot dpl <url> <item1,item2>
    $ bot rem <url>
    $ bot nme <url< <name>


COMMANDS


::

    cmd - commands
    cfg - irc configuration
    dlt - remove a user
    dpl - sets display items
    ftc - runs a fetching batch
    fnd - find objects 
    flt - instances registered
    log - log some text
    met - add a user
    mre - displays cached output
    nck - changes nick on irc
    pwd - sasl nickserv name/pass
    rem - removes a rss feed
    rss - add a feed
    slg - slogan
    thr - show the running threads


SYSTEMD

::

    replace <user> with the username giving the pipx command.

    [Unit]
    Description=library to program bots
    Requires=network.target
    After=network.target

    [Service]
    DynamicUser=True
    Type=forking
    User=<user>
    Group=<uer>
    PIDFile=bot.pid
    WorkingDirectory=/home/<user>/.bot
    ExecStart=/home/<user>/.local/pipx/venvs/libbot/bin/bot -d
    RemainAfterExit=yes

    [Install]
    WantedBy=multi-user.target



FILES

::

    ~/.local/bin/bot
    ~/.local/pipx/venvs/libbot/


AUTHOR

::

    botlib <botlib@proton.me>


COPYRIGHT

::

    LIBBOT is placed in the Public Domain.
