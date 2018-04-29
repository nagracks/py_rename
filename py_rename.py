#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__    = "nagracks"
__date__      = "02-07-2016"
__license__   = "MIT"
__copyright__ = "Copyright © 2016 nagracks"

import os
import re
from argparse import ArgumentParser


class RenameIt(object):

    """Class RenameIt

    Constructor args:
     :filename: Name of file
     :dryrun: Just dry run, not perform any action
     :silent:

    Methods:
     * prefix_it
     * postfix_it
     * lower_it
     * replace_space
     * camel_case
     * rename
    """

    def __init__(self, filename, dryrun, silent):
        self.full_name = filename
        # Get filename and file extension #
        self.fname, self.fext = os.path.splitext(filename)
        # Suppress output?
        self.silent = silent
        # Are we actually doing anything or just preforming a dryrun?
        self.do_dryrun = dryrun

        if self.do_dryrun:
            print("PERFORMING A DRY RUN (NO ACTIONS WILL BE TAKEN)")

    def _print(self, *msg):
        """Print msg if not silent

        :msg: *str, What to print
        :return: None
        """
        if not self.silent:
            print(msg)

    def _rename(self, new_name):
        """Generic rename method with error handling

        :new_name: str, Filename to rename to
        :return: None
        """
        try:
            if not self.do_dryrun:
                os.rename(self.full_name, new_name + self.fext)
            self._print("renaming: {old} --> {new}".format(old=self.full_name,
                                                new=new_name + self.fext))
            # Set after every rename, makes it possible to run multiple
            # arguments
            self.fname = new_name
            self.full_name = self.fname + self.fext
        except OSError as e:
            self._print(
                "Failed to rename {old} --> {new}: {err}".
                format(old=self.full_name, new=new_name, err=e))

    def prefix_it(self, prefix_str):
        """Prefix filename with prefix string

        :prefix_str: str, string to use as prefix in filename
        :returns: None
        """
        old_name = self.fname
        new_name = prefix_str + old_name
        self._rename(new_name)

    def postfix_it(self, postfix_str):
        """Postfix filename with postfix string

        :postfix_str: str, string to use as postfix in filename
        :returns: None
        """
        old_name = self.fname
        new_name = old_name + postfix_str
        self._rename(new_name)

    def remove_it(self,n_chars):
        """Remove characters from the start or end of filename

        :n_chars: int, number of characters to remove. +ve from start, -ve from end
        :returns: None
        """
        old_name = self.fname
        length = len(old_name)
        if abs(n_chars) >= length:
            self._print(
                "Failed to rename {old} : {err}".
                format(old=self.full_name, err="Number of characters equals or exceeds length of filename"))
        elif n_chars >= 0:
            new_name = old_name[n_chars::]
            self._rename(new_name)
        else:
            new_name = old_name[0:n_chars]
            self._rename(new_name)

    def lower_it(self):
        """Lowercase the filename
        :returns: None
        """
        old_name = self.fname
        new_name = old_name.lower()
        self._rename(new_name)

    def replace_space(self, fill_char='_'):
        """Replace spaces with fill_char

        :fill_char: default to '_'
        :returns: None
        """
        old_name = self.fname
        new_name = old_name.replace(' ', fill_char)
        self._rename(new_name)

    def camel_case(self):
        """Convert to camel case
        :returns: None
        """
        old_name = self.fname.replace('_', ' ')
        modified_name = re.findall('[\w]+', old_name.lower())
        new_name = ''.join([word.title() for word in modified_name])
        self._rename(new_name)

    def rename(self, rename_string):
        """ renames file to rename_string

        :rename_string: str,  new filename
        :returns: None
        """
        old_name = self.fname
        new_name = rename_string
        self._rename(new_name)


if __name__ == "__main__":
    parser = ArgumentParser(description="Python Rename")
    parser.add_argument(
            '-v',
            '--version',
            action='version',
            version='%(prog)s version 0.1'
            )
    parser.add_argument(
            '-A',
            '--prefix',
            dest='prefix',
            metavar='string',
            action='store',
            help="prefix filename with prefix string"
            )
    parser.add_argument(
            '-B',
            '--postfix',
            dest='postfix',
            metavar='string',
            action='store',
            help="postfix filename with postfix string"
            )
    parser.add_argument(
            '-C',
            '--remove',
            dest='remove',
            type=int,
            metavar='int',
            action='store',
            help="remove characters from start or end of filename (+ve for start, -ve for end)"
            )
    parser.add_argument(
            '-r',
            '--rename',
            dest='rename',
            metavar='string',
            action='store',
            help="replace filename with string"
            )
    parser.add_argument(
            '-n',
            '--dryrun',
            dest='dryrun',
            action='store_true',
            help="perform a dry run (will not run any actions)"
            )
    parser.add_argument(
            '--lower',
            dest='lower',
            action='store_true',
            help="lowercase the filename"
            )
    parser.add_argument(
            '--remove-space',
            action='store_true',
            help="remove space with underscore"
            )
    parser.add_argument(
            '--camel-case',
            action='store_true',
            help="convert to camel case"
            )
    parser.add_argument(
            '-s',
            '--silent',
            dest='silent',
            action='store_true',
            help="silence output"
            )
    parser.add_argument(
            'filename',
            help="filename"
            )

    args = parser.parse_args()

    rename_it = RenameIt(args.filename, args.dryrun, args.silent)

    if args.rename:
        rename_it.rename(args.rename)
    if args.prefix:
        rename_it.prefix_it(args.prefix)
    if args.postfix:
        rename_it.postfix_it(args.postfix)
    if args.remove:
        rename_it.remove_it(args.remove)
    if args.lower:
        rename_it.lower_it()
    if args.remove_space:
        rename_it.replace_space()
    if args.camel_case:
        rename_it.camel_case()
