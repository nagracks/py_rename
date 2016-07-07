#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__    = "nagracks"
__date__      = "02-07-2016"
__license__   = "GPL3"
__copyright__ = "Copyright © 2016 nagracks"
__contributors__ = ["kretusmaximus"]

import os
from cmd_args import parse_args


class RenameIt(object):

    """RenameIt has various methods for rename files
    eg:

    * prefix_it
    * postfix_it
    * lower_it
    * remove_space
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

        :param msg: What to print
        :type msg: str
        """
        if not self.silent:
            print(msg)

    def _rename(self, old_name, new_name):
        """Generic rename method with error handling

        :param old_name: File to rename
        :type old_name: str
        :param new_name: Filename to rename to
        :type new_name: str
        :return:
        """
        try:
            if not self.do_dryrun:
                os.rename(old_name, new_name)
            self._print("renaming: {old} --> {new}".format(old=old_name,
                                                           new=new_name))
        except OSError as e:
            self._print(
                "Failed to rename {old} --> {new}: {err}".format(old=old_name,
                                                                 new=new_name,
                                                                 err=e))

    def prefix_it(self, prefix_str):
        """Prefix filename with prefix string

        :prefix_str: string, string to use as prefix in filename
        :returns: None

        """
        old_name = self.full_name
        new_name = prefix_str + old_name
        self._rename(old_name, new_name)

    def postfix_it(self, postfix_str):
        """Postfix filename with postfix string

        :postfix_str: string, string to use as postfix in filename
        :returns: None

        """
        old_name = self.full_name
        new_name = self.filename + postfix_str
        self._rename(old_name, new_name)

    def lower_it(self):
        """Lowercase the filename
        :returns: None

        """
        old_name = self.full_name
        new_name = old_name.lower()
        self._rename(old_name, new_name)

    def replace_space(self, fill_char='_'):
        """Replace spaces with fill_char

        :fill_char: default to '_'
        :returns: None

        """
        old_name = self.full_name
        new_name = old_name.replace(' ', fill_char)
        self._rename(old_name, new_name)

    def camel_case(self):
        """Convert to camel case
        :returns: None

        """
        old_name = self.full_name
        new_name = ''.join(word.title() for word in
                           old_name.lower().split(' ', '_'))
        self._rename(old_name, new_name)


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
    elif args.postfix:
        rename_it.postfix_it(args.postfix)
    elif args.lower:
        rename_it.lower_it()
    elif args.remove_space:
        rename_it.replace_space()
    elif args.camel_case:
        rename_it.camel_case()


if __name__ == "__main__":
    main()
