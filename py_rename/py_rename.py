#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__    = "nagracks"
__date__      = "02-07-2016"
__license__   = "GPL3"
__copyright__ = "Copyright © 2016 nagracks"

import os
from cmd_args import parse_args

class RenameIt:

    """RenameIt has various methods for rename files
    eg:

    * prefix_it
    * postfix_it
    * lower_it
    
    """

    def __init__(self, filename, dryrun):
        self.full_name = filename
        # Get filename and fileextention #
        self.filename, self.extension = os.path.splitext(filename)

        # Are we actually doing anything or just preforming a dryrun?
        self.do_dryrun = dryrun
        if self.do_dryrun:
            print "PERFORMING A DRY RUN (NO ACTIONS WILL BE TAKEN)"

    def prefix_it(self, prefix_str):
        """Prefix filename with prefix string

        :prefix_str: string, string to use as prefix in filename
        :returns: None

        """
        old_name = self.full_name
        new_name = prefix_str + old_name
        try:
            if self.do_dryrun == False:
                os.rename(old_name, new_name)
            print "renaming: {old} --> {new}".format(old=old_name,
                                                     new=new_name)
        except OSError as e:
            print e

    def postfix_it(self, postfix_str):
        """Postfix filename with postfix string

        :postfix_str: string, string to use as postfix in filename
        :returns: None

        """
        old_name = self.full_name
        new_name = self.filename + postfix_str
        try:
            if self.do_dryrun == False:
                os.rename(old_name, new_name)
            print "renaming: {old} --> {new}".format(old=old_name,
                                                     new=new_name)
        except OSError as e:
            print e

    def lower_it(self):
        """Lowercase the filename
        :returns: None

        """
        old_name = self.full_name
        new_name = old_name.lower()
        try:
            if self.do_dryrun == False:
                os.rename(old_name, new_name)
            print "renaming: {old} --> {new}".format(old=old_name,
                                                     new=new_name)
        except OSError as e:
            print e

def main():
    """Main function
    :returns: None

    """

    # Commandline args #
    args = parse_args()

    # Assign value #
    prefix_str = args.prefix
    postfix_str = args.postfix
    filename = args.filename
    lower = args.lower
    dryrun = args.dryrun

    # Initialise RenameIt object #
    rename_it = RenameIt(filename, dryrun)

    # Applying args conditions #
    if prefix_str:
        rename_it.prefix_it(prefix_str)
    elif postfix_str:
        rename_it.postfix_it(postfix_str)
    elif lower:
        rename_it.lower_it()

if __name__ == "__main__":
    main()
