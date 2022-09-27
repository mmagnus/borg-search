#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Search for phrase in all of your repos or in --only::

    $ borg-index.py --only m1.
    > args: Namespace(only='m1.', verbose=False)
    > repo: 'm1.local-2022-01-26-143942'

files will be created so you can grep them::

    $ grep 'Miro' m1*
    m1.local-2022-01-26-143942.txt:drwxr-xr-x magnus staff         0 Mon, 2021-07-26 17:02:21 Volumes/HD/docs/Movies/Miro Video Converter

and then to extract::

    $ borg extract ::m1.local-2022-01-26-143942 'Volumes/HD/docs/Movies

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
    parser.add_argument("--only", help="only this repo, like 'snapshot' or 'snapshot-2022-04' (dont use here *, just write part of repo names; of '*' then take all (by default)",
                        default="*") # nargs='+')
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
    ic(args)
    out, err = exe("borg list ::")
    if not out.strip():
        print('Empty borg list')
        sys.exit(1)
    nl = []
    for l in out.split('\n'):
        repo = l.split()[0]
        if args.only == '*':
            nl.append(repo)
            continue
        if args.only in l:
            nl.append(repo)

    print('found ', len(nl))
    for l in nl:
        print(l)

    from tqdm import tqdm
    pbar = tqdm(nl)
    for repo in pbar:
        cmd = 'borg list ::%s > %s.txt' % (repo, repo)
        if args.verbose: print(cmd)
        pbar.set_description("Processing %s" % repo)
        os.system(cmd)

        cmd = 'zip %s.zip %s.txt && trash %s.txt ' % (repo, repo, repo)
        if args.verbose: print(cmd)
        os.system(cmd)
