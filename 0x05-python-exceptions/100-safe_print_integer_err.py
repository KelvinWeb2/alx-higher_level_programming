#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    intgr = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        intgr = False
    return (intgr)
