#! /usr/bin/env python
# -*- coding: utf8 -*-

import glob
import os
import errno
import random
from os.path import abspath
import csv


filename = abspath('../../neugebax/MTB/meta_clinical_sample.txt')
filename1 = abspath('../../neugebax/MTB/meta_study.txt')
filename2 = abspath('../../neugebax/MTB/meta_clinical_patient.txt')
filename3 = abspath('../../neugebax/MTB/meta_mutations_extended.txt')
filename4 = abspath('../../neugebax/MTB/data_clinical_sample.txt')
filename5 = abspath('../../neugebax/MTB/data_clinical_patient.txt')


do_it_random = True


#SAMPLE_ID herauskriegen
os.chdir("/home/neugebax/MAF_Dateien/")

Result_for_data_clinical_sample = ""
Result_for_data_clinical_patient = ""

file_name = "Codierung_Testdaten_Erlangen.csv"
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

if do_it_random == False:
    for line in csv_reader:
        first_column = (line[1])
        second_column = (line[2]) #index 1 for second column
        third_column = (line[3])
        forth_column = (line[4])
        fifth_column = (line[5])
        six_column  = (line[6])
        seventh_column = (line[7])
        eigth_column = (line[8])
        Result_for_data_clinical_sample += first_column + '\t' + second_column + '\t' + eigth_column +'\n' 
        Result_for_data_clinical_patient += first_column + '\t' + third_column + '\t' + forth_column + '\t' + fifth_column +  '\t' + six_column +  '\t' + seventh_column + '\n'
        Result_for_data_clinical_sample_without_header = Result_for_data_clinical_sample[23:]
        Result_for_data_clinical_patient_without_header = Result_for_data_clinical_patient[54:]
else:
    for line in csv_reader:
        for index in range(0,1):
            first_column = random.randint(1000000000,9999999999)
        second_column = (line[2]) #index 1 for second column
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

if not os.path.exists(os.path.dirname(filename)):
    try:
       os.makedirs(os.path.dirname(filename))
    except OSError as exc:  # Guard against race condition
        if exc.errno != errno.EEXIST:
           raise

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
