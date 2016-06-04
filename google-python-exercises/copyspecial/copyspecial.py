#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""


# +++your code here+++
# Write functions and modify main() to call them
def get_special_filepaths(dirname):
    result = []

    filenames = os.listdir(dirname);
    for filename in filenames:
        match = re.search(r'__\w+__', filename)
        if match:
            result.append(os.path.abspath(os.path.join(dirname, filename)))

    return result


def copy_to(special_filepaths, todir):
    """Copy multiple files to a directory"""
    if not os.path.exists(todir):
        os.mkdir(todir)
    for filepath in special_filepaths:
        shutil.copy(filepath, todir)


def zip_to(paths, zipfile):
    """Zip multiple files with the given name"""
    cmd = 'zip -j ' + zipfile + ' ' + ' '.join(paths)
    print 'Execute command', cmd

    # If the command has a problem, the status is not 0, print the error message to stderr
    (status, output) = commands.getstatusoutput(cmd)
    if status:
        sys.stderr.write(output)
        sys.exit(1)


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print "error: must specify one or more dirs"
        sys.exit(1)

    # +++your code here+++
    # Call your functions
    special_filepaths = []
    for dir in args:
        special_filepaths.extend(get_special_filepaths(dir))

    if todir:
        copy_to(special_filepaths, todir)
    elif tozip:
        zip_to(special_filepaths, tozip)
    else:
        print '\n'.join(special_filepaths)


if __name__ == "__main__":
    main()
