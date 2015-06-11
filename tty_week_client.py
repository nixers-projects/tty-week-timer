#!/usr/bin/env python

import datetime


def fetch_time_left():
    """
    fetch_time_left :: Int
    get the time from the daemon
    maybe nudge it so it fetches it directly
    """
    pass


def get_end_as_local_time(time_left):
    """
    get_end_as_local_time :: String
    Returns the date (as local time) when the challenge will end
    """
    return str(
        datetime.datetime.now() + datetime.timedelta(seconds=int(time_left)))
