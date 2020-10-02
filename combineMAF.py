#! /usr/bin/env python
# -*- coding: utf8 -*-

import glob
import os
import errno
from os.path import abspath


read_files = glob.glob('/home/neugebax/MAF_Dateien/*.tabular')
filename = abspath('../../neugebax/MTB/data_mutations_extended.txt')

if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exc:  # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

with open(filename, "w") as outfile:
    for f, value in enumerate(read_files):
        with open(value, "r") as infile:
            if f == 0:
                outfile.write(infile.read())
            elif f != 0:
                outfile.write(infile.read()[601:])
