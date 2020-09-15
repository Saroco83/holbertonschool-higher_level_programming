#!/usr/bin/python3
def uppercase(str):
    print("".join(["{}".format(chr(ord(i)-32)) if 96 < ord(i) < 123 else
                   i for i in str]))
