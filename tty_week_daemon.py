#!/usr/bin/env python
"""
This program is run with the pythondaemon to be started as a daemon.
python2 pythondaemon.py tty_week_daemon.py
"""
import time
import config
from urllib import URLopener


"""
global
"""
WEB_INSTANCE = URLopener()


def initialize_timer():
    """
    fetch the initial time left for the timer online or from a local save
    """
    try:
        response = WEB_INSTANCE.open(config.API_LOCATION).read()
        return response
    except, Exception e:
        print(e)
        return 'WAITING'


def end_all_X_sessions():
    """
    end_all_X_sessions :: void
    Check if any graphical session is running and kill them
    """
    pass


def kill_itself():
    """
    kill_itself :: void
    Function that will end the daemon process
    """
    pass


def save_time_left(time_left):
    """
    save_time_left :: bool
    saves the time left so that the client can find it
    """
    open(config.SAVE_LOCATION,'w').write(time_left)


def run():
    """
    Main procedure that is ran every X minutes
    """
    # Idle state, waiting for the challenge to start
    time_left = initialize_timer()
    while time_left == "WAITING":
        time_left = initialize_timer()
    if time_left == "END!":
        return
    config.TIME_LEFT = time_left
    while config.TIME_LEFT >= 0:
        end_all_X_sessions()
        save_time_left(config.TIME_LEFT)
        time.sleep(config.RUN_EVERY*60)
        config.TIME_LEFT -= config.RUN_EVERY*60
    kill_itself()


"""
Exec the magic
"""
run()
