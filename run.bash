#!/bin/bash

python combineFiles.py
wait
python createMetaFiles.py
wait
python createCaseFiles.py
#wait
#python deleteLine.py
