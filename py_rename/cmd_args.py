#!/usr/bin/env python2
# -*- coding: utf-8 -*-


from argparse import ArgumentParser


__author__       = "nagracks"
__date__         = "30-07-2016"
__license__      = "GPL3"
__copyright__    = "Copyright © 2016 nagracks"
__contributors__ = ["kretusmaximus", "astonge", "prabhath6", "Luki138"]


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
                        dest='prefix',
                        metavar='string',
                        action='store',
                        help="prefix filename with prefix string")
    parser.add_argument('-B',
                        '--postfix',
                        dest='postfix',
                        metavar='string',
                        action='store',
                        help="postfix filename with postfix string")

<<<<<<< HEAD
    parser.add_argument('-r',
                        '--rename',
                        dest='rename',
                        metavar='string',
                        action='store',
                        help="replace filename with string")

    # TODO implement regex
    """ parser.add_argument('-R',
=======
    parser.add_argument('-R',
>>>>>>> upstream/master
                        '--regex',
                        dest='regex',
                        metavar='string',
                        action='store',
<<<<<<< HEAD
                        help="regex support, matches get replaced with --rename string")
    """
=======
                        help="replace regex with string")
>>>>>>> upstream/master
    # Boolean args #
    parser.add_argument('-n',
                        '--dryrun',
                        dest='dryrun',
                        action='store_true',
                        help="perform a dry run (will not run any actions)")
    parser.add_argument('--lower',
                        dest='lower',
                        action='store_true',
                        help="lowercase the filename")
    parser.add_argument('--remove-space',
                        action='store_true',
                        help="remove space with underscore")
    parser.add_argument('--camel-case',
                        action='store_true',
                        help="convert to camel case")
    parser.add_argument('-s',
                        '--silent',
                        dest='silent',
                        action='store_true',
                        help="silence output")

    # Positional args #
    parser.add_argument('filename',
                        help="filename")

    args = parser.parse_args()
    return args
