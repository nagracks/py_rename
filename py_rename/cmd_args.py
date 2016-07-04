#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__    = "nagracks"
__date__      = "02-07-2016"
__license__   = "GPL3"
__copyright__ = "Copyright © 2016 nagracks"

from argparse import ArgumentParser

def parse_args():
    """parse args with argparse
    :returns: args

    """
    parser = ArgumentParser(description="Python Rename")
    parser.add_argument('-v',
                        '--version',
                        action='version',
                        version='%(prog)s version 0.1')
    parser.add_argument('-A',
                        '--prefix',
                        dest = 'prefix',
                        metavar='string',
                        action='store',
                        help="Prefix filename with prefix string")
    parser.add_argument('-B',
                        '--postfix',
                        dest = 'postfix',
                        metavar='string',
                        action='store',
                        help="Postfix filename with postfix string")
    # Boolean args #
    parser.add_argument('-n',
                        '--dryrun',
                        dest = 'dryrun',
                        action='store_true',
                        help="Perform a dry run (will no run any actions)")
    parser.add_argument('-l',
                        '--lower',
                        dest='lower',
                        action='store_true',
                        help="Lowercase the filename")
    
    # Positional args #
    parser.add_argument('filename',
                        help="Filename")

    args = parser.parse_args()
    return args
