#  Author: Anton Nedilko
#   Email: arcs3567@gmail.com
#  Source: https://github.com/techeditorsrc
#    Info: functions for conversion integer and r, g, b values into a hex string format
# License: GPL v3

def int_to_hex(p,align=-1):
    r=hex(p)[2:]
    if align!=-1:
        l=len(r)
        if l<align:
            r='0'*(align-l)+r
    return r

def rgb_to_hex(r,g,b):
    return int_to_hex(r,align=2)+int_to_hex(g,align=2)+int_to_hex(b,align=2)
