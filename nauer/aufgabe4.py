#!/usr/bin/env python3

# Define constant varibales
flags = dict(FLAG_1=1,
             FLAG_2=2,
             FULLSCREEN=4,
             DEBUG=8,
             LOG_ON=16,
             IGNORE_CASE=32,
             OPTION_1=64,
             OPTION_2=128)

# Set flags
f = flags['FULLSCREEN'] | flags['LOG_ON'] | flags['DEBUG']

print(f)

for key, value in flags.items():
    if value & f:
        # Use ANSI color codes
        # See https://en.wikipedia.org/wiki/ANSI_escape_code
        # and http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
        # for more information
        print('\033[94mFlag {} was set!'.format(key))
    else:
        print('\033[91mFlag {} was not set!'.format(key))