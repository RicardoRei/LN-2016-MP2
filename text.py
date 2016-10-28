# -*- coding: utf-8 -*-
import re

#--------------------------------------------------------------------------------------------------
#                   module that stores the text normalizations used
#--------------------------------------------------------------------------------------------------

#@brief:
#	this funtion processes all the text.
def processText(file):
	text = processPunctuation(file)
	return text

#@brief:
#	Function that receives a file and reads every line adding a space at right and left of every 
#	punctuation.
def processPunctuation(file):
	text = ""
	for line in file:
		result = re.sub(r'((\.\.\.)|[:,!?;.])', r' \1 ', line)
		text = text + result
	return text