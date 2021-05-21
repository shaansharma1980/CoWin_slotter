#!/bin/bash

/usr/local/bin/newman run ./cowin.json > /tmp/output.tmp
# use python3.x+
/usr/bin/python3 cowin_notifier.py

exit 0

