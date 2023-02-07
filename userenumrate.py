#!/usr/bin/env python
import sys
import os.path

def fix_name(name):
    name = name.strip()
    name = ''.join([c for c in name if c.isalpha() or c == "."])
    tokens = name.lower().split(".")
    return tokens

if __name__ == "__main__": 
    if len(sys.argv) != 2:
        print("usage: {} names.txt".format((sys.argv[0])))
        sys.exit(0)

    if not os.path.exists(sys.argv[1]): 
        print("{} not found".format(sys.argv[1]))
        sys.exit(0)

    for line in open(sys.argv[1]):
        name = fix_name(line)

        # skip empty lines
        if len(name) < 1: 
            continue

        fname = name[0]
        lname = name[-1]

        print("{}.{}".format(fname, lname))
        print("{}{}".format(fname, lname))
        print("{}{}".format(lname, fname))
        print("{}.{}".format(lname, fname))
        print("{}{}".format(lname, fname[0]))
        print("{}{}".format(fname[0], lname))
        print("{}.{}".format(fname[0], lname))
        print("{}.{}".format(lname[0], fname))
        print(fname)
        print(lname)
