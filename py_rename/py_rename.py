#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
from cmd_args import parse_args


__author__          = "nagracks"
__date__            = "02-07-2016"
__license__         = "GPL3"
__copyright__       = "Copyright © 2016 nagracks"
__contributors__    = ["kretusmaximus", "astonge", "prabhath6", "Luki138"]


class RenameIt(object):

    """Class RenameIt

    Constructor args:
    filename
    dryrun
    silent

    methods
    * prefix_it
    * postfix_it
    * lower_it
    * replace_space
    * camel_case
    """

    def __init__(self, filename, dryrun, silent):
        self.full_name = filename
        # Get filename and file extension #
        self.filename, self.extension = os.path.splitext(filename)
        # Suppress output?
        self.silent = silent
        # Are we actually doing anything or just preforming a dryrun?
        self.do_dryrun = dryrun

        if self.do_dryrun:
            print("PERFORMING A DRY RUN (NO ACTIONS WILL BE TAKEN)")

    def _print(self, *msg):
        """Print msg if not silent

        :msg: str, What to print
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
                os.rename(self.full_name, new_name + self.extension)
            self._print("renaming: {old} --> {new}".format(old=self.full_name,
                                                new=new_name + self.extension))
            # Set after every rename, 
            # Makes it possible to run multiple arguments
            self.filename = new_name
            self.full_name = self.filename + self.extension
        except OSError as e:
            self._print(
                "Failed to rename {old} --> {new}: {err}".
                format(old=self.full_name, new=new_name, err=e))

    def prefix_it(self, prefix_str):
        """Prefix filename with prefix string

        :prefix_str: str, string to use as prefix in filename
        :returns: None
        """
        old_name = self.filename
        new_name = prefix_str + old_name
        self._rename(new_name)

    def postfix_it(self, postfix_str):
        """Postfix filename with postfix string

        :postfix_str: str, string to use as postfix in filename
        :returns: None
        """
        old_name = self.filename
        new_name = old_name + postfix_str
        self._rename(new_name)

    def lower_it(self):
        """Lowercase the filename
        :returns: None
        """
        old_name = self.filename
        new_name = old_name.lower()
        self._rename(new_name)

    def replace_space(self, fill_char='_'):
        """Replace spaces with fill_char

        :fill_char: default to '_'
        :returns: None
        """
        old_name = self.filename
        new_name = old_name.replace(' ', fill_char)
        self._rename(new_name)

    def camel_case(self):
        """Convert to camel case
        :returns: None
        """
        old_name = self.filename.replace('_', ' ')
        modified_name = re.findall('[\w]+', old_name.lower())
        new_name = ''.join([word.title() for word in modified_name])
        self._rename(new_name)


def main():
    """Main function
    :returns: None
    """

    # Commandline args #
    args = parse_args()

    # Initialise RenameIt object #
    rename_it = RenameIt(args.filename, args.dryrun, args.silent)

    # Applying args conditions #
    if args.prefix:
        rename_it.prefix_it(args.prefix)
    if args.postfix:
        rename_it.postfix_it(args.postfix)
    if args.lower:
        rename_it.lower_it()
    if args.remove_space:
        rename_it.replace_space()
    if args.camel_case:
        rename_it.camel_case()


if __name__ == "__main__":
    main()
