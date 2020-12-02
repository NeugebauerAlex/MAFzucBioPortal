#! /usr/bin/env python
# -*- coding: utf8 -*-


# Wenn es Artefakte aus der Pipeline gibt, die nicht mit in cBioPortal sollen, bitte in einer CSV Datei sammeln und mit diesem Skript aus der kombinierten MAF Datei löschen
import csv
import os
from backports import configparser

config = configparser.ConfigParser()
config.read('config.ini')

os.chdir(config['deleteLine']['ord_name'])
Result_for_artifact_selection = ""
original_file = config['deleteLine']['original_file']
dummy_file = config['deleteLine']['dummy_file']

# Ziehe Spalte mit Artefakten aus CSV Datei
file_name = config['deleteLine']['file_name_2']
csv_file = open(file_name)
csv_reader = csv.reader(csv_file, delimiter=';')

second_column = []

for line in csv_reader:
    second_column = (line[2])
    Result_for_artifact_selection += second_column + '\n'
    Result_for_artifact_selection_without_header = Result_for_artifact_selection[12:]

# Nehme die aneinandergereihten Strings und Forme sie in eine Liste
stringIntoList = Result_for_artifact_selection_without_header.split('\n')

# Durch die Liste iterieren, um Duplikate zu eleminieren
stringIntoList = list(dict.fromkeys(stringIntoList))


def main():
    length = len(stringIntoList)
    length_real = length - 1
    i = 0
    while i < length_real:
        delete_line_with_word(original_file, stringIntoList[i])
        i += 1


def delete_line_by_condition(original_file, condition):
    """ In a file, delete the lines at line number in given list"""
    dummy_file = original_file + '.bak'
    is_skipped = False
    # Open original file in read only mode and dummy file in write mode
    with open(original_file, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Line by line copy data from original file to dummy file
        for line in read_obj:
            # if current line matches the given condition then skip that line
            if condition(line) == False:
                write_obj.write(line)
            else:
                is_skipped = True
    # If any line is skipped then rename dummy file as original file
    if is_skipped:
        os.remove(original_file)
        os.rename(dummy_file, original_file)
    else:
        os.remove(dummy_file)


def delete_line_with_word(file_name, word):
    """Delete lines from a file that contains a given word / sub-string """
    delete_line_by_condition(file_name, lambda x: word in x)


if __name__ == '__main__':
    main()
