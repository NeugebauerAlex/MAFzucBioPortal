#! /usr/bin/env python
# -*- coding: utf8 -*-

import glob
import os
import errno
from os.path import abspath


# Definiere read_files - Wo findet das Skript die MAF Dateien die kombiniert werden sollen
read_files = glob.glob('/home/neugebax/MAF_Dateien/*.tabular')

# Wo soll die kombinierte MAF Datei gespeichert werden
filename = abspath('../../neugebax/MTB/data_mutations_extended.txt')

# Wenn der angegebene Ordner nicht existiert, kreiere einen
if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exc:  # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

# Kombiniere alle Daten und lösche erste Zeile
with open(filename, "w") as outfile:
    for f, value in enumerate(read_files):
        with open(value, "r") as infile:
            if f == 0:
                outfile.write(infile.read())
            elif f != 0:
                # Wenn Python3 installiert ist, hier nur next()
                outfile.write(infile.read()[601:])
