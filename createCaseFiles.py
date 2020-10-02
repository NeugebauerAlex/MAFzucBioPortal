#! /usr/bin/env python
# -*- coding: utf8 -*-

import csv
import glob
import errno
import os
from os.path import abspath

# Lese die csv Datei ein und Zähle die Zeilen für case_list_description

input_file = open('/home/neugebax/MAF_Dateien/Codierung_Testdaten_Erlangen.csv')
reader_file = csv.reader(input_file)
value_with_header = len(list(reader_file))
value = value_with_header - 1


# Hole den Dateinamen für cancer_study_identifier
#base = os.path.basename('/home/unberapp/import_test/Codierung_Testdaten_Erlangen.csv')

# Das Argument und den Pfad angeben für die beiden case-Dateien
filename1 = abspath('../../neugebax/MTB/case_lists/cases_all.txt')
filename2 = abspath('../../neugebax/MTB/case_lists/cases_sequenced.txt')

#SAMPLE_ID herauskriegen
os.chdir("/home/neugebax/MAF_Dateien/")

Result_for_data_clinical_sample = ""
Result_for_data_clinical_patient = ""
case_list_id = ""

file_name = "Codierung_Testdaten_Erlangen.csv"
csv_file = open(file_name)
csv_reader = csv.reader(csv_file, delimiter=';')
second_column = []

for line in csv_reader:
        second_column = (line[2])
        case_list_id += second_column + '\t'
        case_list_id_without_header = case_list_id[12:]

# Output Ordner nicht da, dann erstelle einen
if not os.path.exists(os.path.dirname(filename1)):
    try:
        os.makedirs(os.path.dirname(filename1))
    except OSError as exc:  # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

# Schreibe eine Datei
with open(filename1, "w") as file:
    file.write("cancer_study_identifier:MTB")
    file.write("\n")
    file.write("stable_id:MTB_all")
    file.write("\n")
    file.write("case_list_name: All Tumors")
    file.write("\n")
    file.write("case_list_description: All tumor samples:" + str(value))
    file.write("\n")
    file.write("case_list_ids:" + case_list_id_without_header)
    file.write("\n")
    file.write("case_list_category: all_cases_in_study")
    file.close()  # close file

if not os.path.exists(os.path.dirname(filename2)):
    try:
        os.makedirs(os.path.dirname(filename2))
    except OSError as exc:  # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

with open(filename2, "w") as file:
    file.write("cancer_study_identifier:MTB")
    file.write("\n")
    file.write("stable_id:MTB_sequenced")
    file.write("\n")
    file.write("case_list_name: All Tumors")
    file.write("\n")
    file.write("case_list_description: All tumor samples:" + str(value))
    file.write("\n")
    file.write("case_list_ids:" + case_list_id_without_header)
    file.close()  # close file
