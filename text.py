# -*- coding: utf-8 -*-
import re

#--------------------------------------------------------------------------------------------------
#                   module that stores the text normalizations used
#--------------------------------------------------------------------------------------------------

#@brief:
#	this funtion processes all the text.
def processText(file):
	text = processPunctuation(file)
	#text = deletePunctuation(text)
	#text = deleteStopWords(text)
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

#@brief:
#	Function that removes the punctuation from the text received has input.
def  deletePunctuation(text):
	return re.sub("[?|\.|!|:|,|;]", '', text)

#@brief:
#	Function that removes the stop word from the text.
def deleteStopWords(text):
	text = re.sub("e", '', text)
	text = re.sub("o", '', text)
	text = re.sub("a", '', text)
	return text

#@brief:
#	Function that removes some accents from the text received has input.
#	NOTE: this function was tested and it didn't look "promissing"
def deleteAccents(text):
	text = re.sub("ã", 'a', text)
	text = re.sub("á", "a", text)
	text = re.sub("à", "a", text)
	text = re.sub("õ", "o", text)
	text = re.sub("ô", "o", text)
	text = re.sub("ó", "o", text)
	text = re.sub("é", "e", text)
	text = re.sub("ê", "e", text)
	text = re.sub("í", "i", text)
	text = re.sub("ú", "u", text)
	text = re.sub("ç", "c", text)
	text = re.sub("Ã", 'A', text)
	text = re.sub("Á", "A", text)
	text = re.sub("À", "A", text)
	text = re.sub("Õ", "O", text)
	text = re.sub("Ô", "O", text)
	text = re.sub("Ô", "O", text)
	text = re.sub("Ó", 'O', text)
	text = re.sub("Í", "I", text)
	text = re.sub("Ú", "U", text)
	text = re.sub("Ç", "C", text)
	text = re.sub("É", "E", text)

	return text