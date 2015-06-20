#!/bin/sh
LOC=$(pwd)
echo "Running $LOC/tty_week_daemon.py as a daemon"
python2 pythondaemon.py "python2 $LOC/tty_week_daemon.py"
