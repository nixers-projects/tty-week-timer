#!/usr/bin/env python

import time

LOCATION_OF_TIMER = "root/of/webserver/api"

while 1:
    time_left = open(LOCATION_OF_TIMER).read()
    try:
        if (int(time_left) <= 0):
            break
        open(LOCATION_OF_TIMER, 'w').write(str(int(time_left)-1))
        time.sleep(1)
    except:
        break
open(LOCATION_OF_TIMER, 'w').write("END!")
