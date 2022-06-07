#!/usr/bin/python3
for d1 in range(0, 8):
    for d2 in range(d1 + 1, 10):
        print("{:d}{:d}".format(d1, d2), end=", ")
print("{:d}{:d}".format(d1 + 1, d2))
