#! /usr/local/bin/python3

import sys
import ws2016 as ws

ws.myfunc('do a')

if len(sys.argv) > 1:  # 0 is prog name

    cmd_name = sys.argv[0]
    first_arg = sys.argv[1]

