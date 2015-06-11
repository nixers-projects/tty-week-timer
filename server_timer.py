#!/usr/bin/env python

LOCATION_OF_TIMER = "root/of/webserver/api"

while 1:
    time_left = open(LOCATION_OF_TIMER).read()
    if (int(time_left) <= 0):
        break
    open(LOCATION_OF_TIMER, 'w').write(int(time_left)-1)
    time.sleep(1)
open(LOCATION_OF_TIMER, 'w').write("END!")
