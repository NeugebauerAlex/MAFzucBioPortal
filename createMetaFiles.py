#! /usr/bin/env python
# -*- coding: utf8 -*-

import os
import errno
import random
from os.path import abspath
import csv
from backports import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# Gebe das Argument und den Pfad, sowie den namen der Datei an, die am Ende erstellt werden soll
filename = abspath(config['createMetaFiles']['filename'])
filename1 = abspath(config['createMetaFiles']['filename1'])
filename2 = abspath(config['createMetaFiles']['filename2'])
filename3 = abspath(config['createMetaFiles']['filename3'])
filename4 = abspath(config['createMetaFiles']['filename4'])
filename5 = abspath(config['createMetaFiles']['filename5'])

# Setze dies auf False, wenn du richtigen Patienten-Daten verwendet werden sollen
do_it_random = config['createMetaFiles']['Patienten_ID_zufällig?']


#SAMPLE_ID herauskriegen
os.chdir(config['createMetaFiles']['ord_name'])

Result_for_data_clinical_sample = ""
Result_for_data_clinical_patient = ""

# Aus der angegebenen CSV Datei die gewünschten Spalten des Pathologie selektieren und kopieren
file_name = (config['createMetaFiles']['file_name_csv'])
csv_file = open(file_name)
csv_reader = csv.reader(csv_file, delimiter=';')
first_column = []
second_column = [] #empty list to store second column values
third_column = []
forth_column  = []
fifth_column  = []
six_column  = []
seventh_column = []
eigth_column = []

# Wenn do_it_random = True, benutze den Zufallszahlen generator für die erste Spalte, der CSV Datei
# Wenn do_it_random = False, kopiere alle gewünschten Spalten aus der CSV Datei

if do_it_random == False:
    for line in csv_reader:
        first_column = (line[1]) #index 1 für zweite column
        second_column = (line[2])
        third_column = (line[3])
        forth_column = (line[4])
        fifth_column = (line[5])
        six_column  = (line[6])
        seventh_column = (line[7])
        eigth_column = (line[8])
        # Kopiere die Selektierten Spalten, in die gewünschten Argumente, die jeweils in data_clinical_patient bzw. data_clinical_sample verwendet werden
        # Immer Tabular getrennt, sonst passt die Formatierung nicht, da ganze Spalten kopiert werden
        # Am Ende immer einen Absatz schreiben, da immer ganze Spalten kopiert werden
        Result_for_data_clinical_sample += first_column + '\t' + second_column + '\t' + eigth_column +'\n'
        Result_for_data_clinical_patient += first_column + '\t' + third_column + '\t' + forth_column + '\t' + fifth_column +  '\t' + six_column +  '\t' + seventh_column + '\n'
        # Lösche die Überschriften, sodass nur die puren Daten genommen werden
        Result_for_data_clinical_sample_without_header = Result_for_data_clinical_sample[23:]
        Result_for_data_clinical_patient_without_header = Result_for_data_clinical_patient[54:]
else:
    for line in csv_reader:
        for index in range(0,1):
            first_column = random.randint(1000000000,9999999999)
        second_column = (line[2])
        third_column = (line[3])
        forth_column = (line[4])
        fifth_column = (line[5])
        six_column  = (line[6])
        seventh_column = (line[7])
        eigth_column = (line[8])
        Result_for_data_clinical_sample += str(first_column) + '\t' + str(second_column) + '\t' + str(eigth_column) +'\n'
        Result_for_data_clinical_patient += str(first_column) + '\t' + str(third_column) + '\t' + str(forth_column) + '\t' + str(fifth_column) +  '\t' + str(six_column) +  '\t' + str(seventh_column) + '\n'
        Result_for_data_clinical_sample_without_header = Result_for_data_clinical_sample[28:]
        Result_for_data_clinical_patient_without_header = Result_for_data_clinical_patient[58:]


# Hole den Dateinamen für cancer_study_identifier
#base = os.path.basename('/home/unberapp/import_test/Codierung_Testdaten_Erlangen.csv')

# Wenn Ordner noch nicht existiert, erstelle einen
if not os.path.exists(os.path.dirname(filename)):
    try:
       os.makedirs(os.path.dirname(filename))
    except OSError as exc:  # Guard against race condition
        if exc.errno != errno.EEXIST:
           raise

# Schreibe die Meta Datei
with open(filename, "w") as file:
    file.write("cancer_study_identifier:MTB")
    file.write("\n")
    file.write("genetic_alteration_type:CLINICAL")
    file.write("\n")
    file.write("datatype: SAMPLE_ATTRIBUTES")
    file.write("\n")
    file.write("data_filename: data_clinical_sample.txt")
    file.close()  # close file


if not os.path.exists(os.path.dirname(filename1)):
    try:
        os.makedirs(os.path.dirname(filename1))
    except OSError as exc:  # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

# Schreibe die Meta Datei
with open(filename1, "w") as file:
    file.write("type_of_cancer: other")
    file.write("\n")
    file.write("cancer_study_identifier:MTB")
    file.write("\n")
    file.write("name: MTB")
    file.write("\n")
    file.write("description: Galaxy Test")
    file.write("\n")
    file.write("short_name: Galaxy Test")
    file.close()  # close file


if not os.path.exists(os.path.dirname(filename2)):
    try:
        os.makedirs(os.path.dirname(filename2))
    except OSError as exc:  # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

# Schreibe die Meta Datei
with open(filename2, "w") as file:
    file.write("cancer_study_identifier:MTB")
    file.write("\n")
    file.write("genetic_alteration_type: CLINICAL")
    file.write("\n")
    file.write("datatype: PATIENT_ATTRIBUTES")
    file.write("\n")
    file.write("data_filename: data_clinical_patient.txt")
    file.close()  # close file


if not os.path.exists(os.path.dirname(filename3)):
    try:
        os.makedirs(os.path.dirname(filename3))
    except OSError as exc:  # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

# Schreibe die Meta Datei
with open(filename3, "w") as file:
    file.write("cancer_study_identifier:MTB")
    file.write("\n")
    file.write("stable_id: mutations")
    file.write("\n")
    file.write("profile_name: Mutations")
    file.write("\n")
    file.write("profile_description: Extended MAF")
    file.write("\n")
    file.write("genetic_alteration_type: MUTATION_EXTENDED")
    file.write("\n")
    file.write("datatype: MAF")
    file.write("\n")
    file.write("show_profile_in_analysis_tab: true")
    file.write("\n")
    file.write("data_filename: data_mutations_extended.txt")
    file.close()  # close file


if not os.path.exists(os.path.dirname(filename4)):
    try:
        os.makedirs(os.path.dirname(filename4))
    except OSError as exc:  # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

# Schreibe die Klinische Datei, immer Tabular getrennt, sonst erkennt es cBioPortal nicht
with open(filename4, "w") as file:
    file.write("#Patient Identifier\tSample Identifier\tName")
    file.write("\n")
    file.write("#Patient Identifier\tSample Identifier\tName")
    file.write("\n")
    file.write('#NUMBER\tSTRING\tSTRING')
    file.write("\n")
    file.write('#1\t1\t1')
    file.write("\n")
    file.write("PATIENT_ID\tSAMPLE_ID\tNAME")
    file.write("\n")
    file.write(Result_for_data_clinical_sample_without_header)

if not os.path.exists(os.path.dirname(filename5)):
    try:
        os.makedirs(os.path.dirname(filename5))
    except OSError as exc:  # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

# Schreibe die Klinische Datei, immer Tabular getrennt, sonst erkennt es cBioPortal nicht
with open(filename5, "w") as file:
    file.write('#Patient Identifier\tOncoTree_Code\tCancerType\tGeschlecht\tAlter\tEinweiser')
    file.write("\n")
    file.write('#Patient Identifier\tOncoTree_Code\tCancerType\tGeschlecht\tAlter\tEinweiser')
    file.write("\n")
    file.write('#NUMBER\tSTRING\tSTRING\tSTRING\tNUMBER\tSTRING')
    file.write("\n")
    file.write('#1\t1\t1\t1\t1\t1')
    file.write("\n")
    file.write('PATIENT_ID\tONCOTREE_CODE\tCANCER_TYPE_DETAILED\tGESCHLECHT\tALTER\tEINWEISER')
    file.write("\n")
    file.write(Result_for_data_clinical_patient_without_header)
