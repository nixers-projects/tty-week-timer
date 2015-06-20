#!/usr/bin/env python

import time
import config

LOCATION_OF_TIMER = config.LOCATION_OF_TIMER

while 1:
    time_left = open(LOCATION_OF_TIMER).read()
    try:
        print(time_left)
        if (int(time_left) <= 0):
            break
        open(LOCATION_OF_TIMER, 'w').write(str(int(time_left)-1))
        time.sleep(1)
    except:
        break
if time_left == "END!" or int(time_left) <= 0:
    open(LOCATION_OF_TIMER, 'w').write("END!")
