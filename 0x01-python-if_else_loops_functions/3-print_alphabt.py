#!/usr/bin/python3
for j in range(ord('a'), ord('z')+1):
    if j != ord('e') and j != ord('q'):
        print("{}".format(chr(j)), end='')
