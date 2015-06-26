#!/usr/bin/env python
"""
This program is run with the pythondaemon to be started as a daemon.
python2 pythondaemon.py tty_week_daemon.py
"""
import time
import config
import subprocess
import signal
import os
from urllib import URLopener


DEBUG = True

"""
global
"""
WEB_INSTANCE = URLopener()
POSSIBLY_X = [
    "Xorg",
    "X11",
    "xinit"
]


def print_debug(msg):
    if DEBUG:
        print("[*] "+msg)


def get_all_current_processes():
    """
    Returns all the current processes running
    """
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = p.communicate()
    return out


def kill_process_by_name(current_processes, name):
    """
    kill_process_by_name :: String -> String -> Void
    takes the output os ps -A and a process name
    it kills all the process currently running that have that name in it
    """
    for line in current_processes.splitlines():
        if name in line:
            print_debug("Found an X session, killing it")
            pid = int(line.split(None, 1)[0])
            os.kill(pid, signal.SIGKILL)


def initialize_timer():
    """
    fetch the initial time left for the timer online or from a local save
    """
    try:
        print_debug("Initializing the timer by fetching it on the online API")
        response = WEB_INSTANCE.open(config.API_LOCATION).read()
        response = response.rstrip()
        print_debug("Found "+str(response)+" on the online API")
        save_time_left(response)
        return response
    except Exception, e:
        print(e)
        return 'WAITING'


def end_all_X_sessions():
    """
    end_all_X_sessions :: void
    Check if any graphical session is running and kill them
    """
    all_processes = get_all_current_processes()
    for i in POSSIBLY_X:
        kill_process_by_name(all_processes, i)


def kill_itself():
    """
    kill_itself :: void
    Function that will end the daemon process
    """
    print_debug("Killing myself")
    all_processes = get_all_current_processes()
    kill_process_by_name(all_processes, "tty_week_daemon")
    pass


def save_time_left(time_left):
    """
    save_time_left :: bool
    saves the time left so that the client can find it
    """
    time_left = time_left.rstrip()
    print_debug("Saving time: "+str(time_left))
    open(config.SAVE_LOCATION, 'w').write(time_left)


def run():
    """
    Main procedure that is ran every X minutes
    """
    # Idle state, waiting for the challenge to start
    time_left = initialize_timer()
    while time_left == "WAITING":
        print_debug("Found waiting flag, will wait until something else happens")
        time_left = initialize_timer()
        time.sleep(10)
    if time_left == "END!":
        print_debug("Challenge already ended")
        return
    config.TIME_LEFT = time_left
    while config.TIME_LEFT >= 0:
        print_debug("Ending all X sessions")
        end_all_X_sessions()
        print_debug("Saving time in specific location")
        save_time_left(config.TIME_LEFT)
        print_debug("Sleeping: "+str(config.RUN_EVERY*60))
        time.sleep(config.RUN_EVERY*60)
        config.TIME_LEFT =  str(int(config.TIME_LEFT)-config.RUN_EVERY*60)
    print_debug("Challenge ended")
    save_time_left("END!")
    print_debug("Killing myself")
    kill_itself()


"""
Exec the magic
"""
run()
