#!/bin/bash
# renames.sh
# basic file renamer

for i in ${tests[*]}; 
do
	python proj.py $i bigrams
done
