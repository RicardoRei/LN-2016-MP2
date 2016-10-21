# -*- coding: utf-8 -*-
import re
import nltk
from nltk import bigrams
from nltk import trigrams

#@brief:
#	Function that receives a file and reades every line adding a space at right and left of every 
#	punctuation.
def processPunctuation(file):
	text = ""
	for line in file:
		result = re.sub(r'((\.\.\.)|[:,!?;.])', r' \1 ', line)
		text = text + result
	return text

fileIn = open('Corpora/test.txt', 'rU')
processed_text = processPunctuation(fileIn)
fileIn.close()
print (processed_text)

# split the texts into tokens
tokens = nltk.word_tokenize(processed_text)
tokens = [token.lower() for token in tokens if (len(token) > 1)] #same as unigrams
bi_tokens = nltk.bigrams(tokens)

print bi_tokens



