#!/usr/bin/env python

import datetime
import config


def fetch_time_left():
    """
    fetch_time_left :: Int
    get the time from the daemon
    maybe nudge it so it fetches it directly
    """
    time_left = config.TIME_LEFT
    try:
        time_left = open(config.SAVE_LOCATION).read()
    except:
        pass
    return time_left


def get_end_as_local_time(time_left):
    """
    get_end_as_local_time :: String
    Returns the date (as local time) when the challenge will end
    """
    if time_left == "WAITING":
        return "Still waiting for the challenge to start"
    elif time_left == "END!":
        return "The challenge is already over"
    else:
        return str(
            datetime.datetime.now() + datetime.timedelta(seconds=int(time_left)))


def run():
    time_left = fetch_time_left()
    print "The challenge will end at: " + get_end_as_local_time(time_left)
    if time_left == "WAITING":
        time_left = 604800
    elif time_left == "END!":
        time_left = 0
    print "Time left: " + str(time_left) + "s"
    print "You already spent " + str(604800-int(time_left)) + "s in the TTY"


run()
