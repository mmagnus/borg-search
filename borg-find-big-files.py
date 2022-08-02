#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
439043371 this is more like byte 439043371B -> 419M

(base) ➜  hd-malibu git:(main) ✗ python ../../borg-find-big-files.py hd-2022-05-17T13:01:57.txt | grep Movie
size 439043371 -rw-r--r-- magnus staff  439043371 Fri, 2021-05-28 19:53:44 docs/Movies/Miro Video Converter/sc 2021-05-28 at 14.02.50.appleuniversal.mp4
-rw-r--r--  1 magnus  staff   419M May 28  2021 sc 2021-05-28 at 14.02.50.appleuniversal.mp4

size 754455073 -rw-r--r-- magnus staff  754455073 Sat, 2020-12-05 14:00:14 docs/Movies/emacs git vm/git/Screen Recording 2020-12-05 at 1.39.15 PM.mov
size 547079395 -rw-r--r-- magnus staff  547079395 Sat, 2020-12-05 14:18:13 docs/Movies/emacs git vm/git/Screen Recording 2020-12-05 at 2.01.27 PM.mov
size 422908997 -rw-r--r-- magnus staff  422908997 Sat, 2020-12-05 15:31:51 docs/Movies/emacs git vm/git/Screen Recording 2020-12-05 at 3.20.55 PM.mov


(base) ➜  hd-malibu git:(main) ✗ python ../../borg-find-big-files.py hd-2022-05-17T13:01:57.txt | sort -r
   3902.94 MB -rwxr----- magnus staff  4092526592 Thu, 2021-05-13 10:32:22 fenix maps/gmapprom.img
   3422.62 MB -rwxr----- magnus staff  3588882432 Thu, 2021-05-13 10:51:24 fenix maps/D6185100A.img

"""
from __future__ import print_function
import argparse
from icecream import ic
import sys
ic.configureOutput(outputFunction=lambda *a: print(*a, file=sys.stderr))
ic.configureOutput(prefix='> ')


def get_parser():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)

    #parser.add_argument('-', "--", help="", default="")

    parser.add_argument("-v", "--verbose",
                        action="store_true", help="be verbose")
    parser.add_argument("file", help="", default="", nargs='+')
    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    if list != type(args.file):
        args.file = [args.file]

    for f in args.file:
        #print(f, '---------------------------------')
        for l in open(f):
            
            try:
                l.split()[3]
            except IndexError:
                continue
            
            size = round(int(l.split()[3]) / (1024 * 1024), 2) # to get MB
            if size > 100: # 
                print(str(size).rjust(10), 'MB @', f + '|' + l.strip())
            
