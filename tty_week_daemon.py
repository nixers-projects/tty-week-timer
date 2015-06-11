#!/usr/bin/env python
"""
This program is run with the pythondaemon to be started as a daemon.
python2 pythondaemon.py tty_week_daemon.py
"""
import time

"""
config
"""
RUN_EVERY = 10
TIME_LEFT = 60*60*24*7  # one week


def end_all_X_sessions():
    """
    end_all_X_sessions :: void
    Check if any graphical session is running and kill them
    """
    pass


def save_time_left(time_left):
    """
    save_time_left :: bool
    saves the time left so that the client can find it
    """
    pass


def run():
    """
    Main procedure that is ran every X minutes
    """
    while 1:
        end_all_X_sessions()
        save_time_left(TIME_LEFT)
        time.sleep(RUN_EVERY*60)
        TIME_LEFT -= RUN_EVERY*60
