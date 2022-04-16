#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Search for phrase in all of your repos or in --only::

     $ python borg-index.py --only snapshot-2022-04-16

files will be created so you can grep them::

    $ head snapshot-2022-04-13T00:01:05.txt
    drwxr-xr-x magnus staff         0 Tue, 2022-04-12 23:07:02 Users/magnus/Desktop

"""
from __future__ import print_function
import argparse
from icecream import ic
import sys
import os
ic.configureOutput(outputFunction=lambda *a: print(*a, file=sys.stderr))
ic.configureOutput(prefix='> ')


def get_parser():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-v", "--verbose",
                        action="store_true", help="be verbose")
    parser.add_argument("--only", help="only this repo, like 'snapshot' or 'snapshot-2022-04'", default="") # nargs='+')
    return parser


import subprocess
def exe(cmd):
    o = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = o.stdout.read().strip().decode()
    err = o.stderr.read().strip().decode()
    return out, err

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    search = args.search
    ic(args)
    out, err = exe("borg list ::")
    for l in out.split('\n'):
        repo = l.split()[0]
        if args.only in l:
            ic(repo)
            os.system('borg list ::%s > %s.txt' % (repo, repo))
