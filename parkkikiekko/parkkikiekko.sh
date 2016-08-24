#!/bin/bash

SERVICE="parkkikiekko/main.py"

while true; do
    if ps ax | grep -v grep | grep $SERVICE > /dev/null; then
	#echo "running"
	sleep 10
    else
        /usr/bin/python /home/pi/work/ZeroSeg/parkkikiekko/main.py 2>&1 > /home/pi/work/ZeroSeg/parkkikiekko/output.log
    fi
done

