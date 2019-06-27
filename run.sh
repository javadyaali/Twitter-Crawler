#!/usr/bin/env bash

for item in `seq 1 37` ; do
    python3 crawler_python3.py $item
    sleep 360
done

