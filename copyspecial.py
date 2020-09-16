#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Wesley Salesberry"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    # your code here
    results = []
    filenames = os.listdir(dirname)
    for filename in filenames:
        if re.search(r'__\w*__', filename):
            results.append(os.path.abspath(os.path.join(dirname, filename)))

    return results


def copy_to(path_list, dest_dir):
    """Given a dirname, returns a list of all its special files."""

    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)

    for _ in path_list:
        shutil.copy(_, os.path.join(dest_dir, os.path.basename(_)))


def zip_to(path_list, dest_zip):
    """Main driver code for copyspecial."""
    cmd = ["zip", "-j", dest_zip]
    cmd.extend(path_list)
    print("Command I'm going to do:", cmd)
    subprocess.run(cmd)


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    parser.add_argument('fromdir', help='dest to grab special files')

    ns = parser.parse_args(args)

    paths = get_special_paths(ns.fromdir)

    # if not ns.todir and not ns.tozip:
    #     parser.print_help()

    if ns.todir:
        copy_to(paths, ns.todir)

    if ns.tozip:
        zip_to(paths, ns.tozip)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    for path in paths:
        print(path)

    # Your code here: Invoke (call) your functions


if __name__ == "__main__":
    main(sys.argv[1:])
