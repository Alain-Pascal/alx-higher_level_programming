#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    num = 0

    argcount = len(sys.argv) - 1

    if argcount == 1:
        print("1 argument", end="")
    elif argcount != 1:
        print("{} arguments".format(argcount), end="")
    if argcount == 0:
        print(".")
    else:
        print(":")
    if(len(sys.argv) > 1):
        for a in sys.argv:
            if num > 0:
                print("{:d}: {}".format(num, a))
            num += 1
