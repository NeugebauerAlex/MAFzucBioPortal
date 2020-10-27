#! /usr/bin/env python
# -*- coding: utf8 -*-

import os
import csv

os.chdir("/Users/alexneugebauer/Desktop/")

original_file = "data_mutations_extended.txt"

dummy_file = "cleaned_file.txt"

Result_for_artifact_selection = ""

# Ziehe Spalte mit Artefakten aus CSV Datei
file_name = "Artefact_List-Tabelle 1.csv"
csv_file = open(file_name)
csv_reader = csv.reader(csv_file, delimiter=';')

second_column = []
second_column = (line[2])

for line in csv_reader:
    second_column = (line[2]) 
    Result_for_artifact_selection += second_column + '\n'
    Result_for_artifact_selection_without_header =  Result_for_artifact_selection[11:]



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


def main():
    delete_line_with_word(original_file, Result_for_artifact_selection_without_header)


def delete_line_with_word(file_name, word):
    """Delete lines from a file that contains a given word / sub-string """
    delete_line_by_condition(file_name, lambda x: word in x)


if __name__ == '__main__':
    main()
