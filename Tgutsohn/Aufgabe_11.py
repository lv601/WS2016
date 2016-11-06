#!/usr/bin/env python3

import sys
import ws2016 as ws

if len(sys.argv) > 1:
    f = open(sys.argv[1], "rb")
    data = ws.parser(f)
    f.close()