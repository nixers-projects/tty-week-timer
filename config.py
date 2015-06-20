import os

"""
config
"""
RUN_EVERY = 10
TIME_LEFT = 60*60*24*7  # one week
API_LOCATION = "http://178.62.236.80/tty_week/api"
LOCATION_OF_TIMER = "api"
SAVE_LOCATION = os.environ["HOME"]+"/.tty_week_timer"
