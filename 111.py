#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from itertools import *
# for i in combinations_with_replacement(123, 3):
#     print i
import time
import sys
def main():
    for i in range(65, 91):
        s = "{name:s}".format(name=chr(i))
        time.sleep(0.5)
        sys.stdout.write(s)


main()