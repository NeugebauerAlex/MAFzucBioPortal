#! /usr/bin/env python
# -*- coding: utf8 -*-

import glob
import os
import errno
from os.path import abspath
from backports import configparser

config = configparser.ConfigParser()
config.read('config.ini')


# Definiere read_files - Wo findet das Skript die MAF Dateien die kombiniert werden sollen
input_files = config['combineFiles']['Pfad_zu_MAF']
read_files = glob.glob(input_files)

# Wo soll die kombinierte MAF Datei gespeichert werden
path = config['combineFiles']['filename']
filename = abspath(path)

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
                # Delete die erste Zeile der folgenden MAF-Dateien, gebe hier die Zeichenanzahl an der Überschrift bei Python < 3
                # Wenn Python3 installiert ist, hier nur next()
                outfile.write(infile.read()[601:])
