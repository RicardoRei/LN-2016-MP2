# -*- coding: utf-8 -*-
import nltk
import nltk.tokenize
from nltk import bigrams
from nltk import trigrams
from text import processText

#--------------------------------------------------------------------------------------------------
#     module that Creates, Stores (in files) and Retrieves  (from files) the counted Ngrams
#--------------------------------------------------------------------------------------------------

import sys
import os

#@brief:
#	Function that receives a list of ngram_token and returns a list of pairs (count, (word1, word2))
#
#	ex: input = [('volta', 'ter'), ('porque', 'era'), ('volta', 'ter')]
#		output = [(2, ('volta', 'ter')), (1, ('porque', 'era'))]
def countNgramFrequency(ngram_tokens):

	def getKey(item):
		return item[1][0]

	from collections import defaultdict
	total = 0

	counts = defaultdict(int)
	for ngram in ngram_tokens:
		counts[ngram] += 1
		total += 1

	result = list()
	for ngram, count in counts.iteritems():
		#in case ngram is a unigram the element is a string (not a tuple) and the writeNgramToFile
		# function in the loop at line 99 will break the string in elements.
		if not isinstance(ngram, tuple):
			ngram = (ngram, )
		result.append((count, ngram))

	return sorted(result, key=getKey) + [(str(total),)]

#@brief: 
#	used to create different ngrams with the tokens from the nltk.
#
def createNgrams(ngramsType, tokens):
	if ngramsType == "unigrams":
		return tokens
	if ngramsType == "bigrams":
		return nltk.bigrams(tokens)
	if ngramsType == "trigrams":
		return nltk.trigrams(tokens)

#@brief: 
#	This funtion will create a big ngram of the type specified on argument ngramsType with all the 
# 	words presented in the texts inside the authors folder.
def createAuthorCountedNgrams(author_directory, ngramsType):
	authorText = ""
	for file in os.listdir(author_directory):
		if "grams" not in file and file.endswith(".txt"):
			f = open(author_directory+"/" + file, 'r')
			authorText += processText(f).decode('utf-8')
			f.close()

	tokens = nltk.word_tokenize(authorText)
	ngrams = createNgrams(ngramsType, tokens)
	return countNgramFrequency(list(ngrams))
	

#@brief:
#	This funtion creates a Ngram for a Specific Text.
#	Note that the last funtion creates a Ngram with all the texts of an author! 
#	This one only considers one text and its mainly used for the test part
def createTextCountedNgrams(textPath, textFilename, ngramsType):
	f1 = open(textPath + textFilename, 'r')
	processed_text = processText(f1).decode('utf-8')
	f1.close()

	tokens = nltk.word_tokenize(processed_text)
	ngrams = createNgrams(ngramsType, tokens)
	return countNgramFrequency(list(ngrams))

#@brief:
#	this funtion will write to a file a counted ngram. 
#	The directortFolder argument is the folder where the new file is going to be saved.
#	The name argument is the name of the file.
def writeNgramsTofile(directoryName, name, counted_ngrams):
	cwd = os.getcwd()
	os.chdir(directoryName)

	if os.path.isfile(name):
		os.remove(name)
		
	outputFile = open(name, "a+")

	for element in counted_ngrams[:-1]:
		new = ""
		for i in element[1]:
			new = new + i + " "
		outputFile.write(new.encode('utf-8') + " " + str(element[0])+"\n")
	
	new = ""
	for i in counted_ngrams[-1]:
		new = new + str(i) + " "
	outputFile.write("Ngrams_Info: " + new.encode('utf-8')+ "\n")

	outputFile.close()
	os.chdir(cwd)

#@brief:
#	In order to compare the Ngrams its easier if they have the same format.
#	This function receives a counted ngram and creates an dictionary.
# ex: Input = [(2, ('volta', 'ter')), (1, ('porque', 'era'))]
#	  Output = { ('volta', 'ter'): 2, ('porque', 'era'): 1 }
def countedNgramsToDictionary(ngrams):
	result = dict()
	for e in ngrams[:-1]:
		key = tuple()
		for word in e[1]:
			key = key + (word.encode('utf-8'),)
		result[key] = e[0]
	result["Ngrams_Info"] = ngrams[-1]
	return result

#@brief:
#	receives a FilePointer that stores a counted ngram and return a dictionary for that ngram.
def countedNgramsFileToDictionary(file):
	result = dict()
	for line in file:
		if line.startswith("Ngrams_Info"):
			result["Ngrams_Info"] = tuple(line.split()[1:])
		else:
			count = line.split()[-1]
			ngram = tuple(line.split()[:-1])
			result[ngram] = count
	return result

#---------------------------------------------------------------------------------------------------
#								Format examples
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
#For the text:
'''
All that is gold does not glitter,
Not all those who wander are lost;
The old that is strong does not wither,
Deep roots are not reached by the frost.

From the ashes a fire shall be woken,
A light from the shadows shall spring;
Renewed shall be blade that was broken,
The crownless again shall be king.
'''

# The counted ngram generated should be:
counted_ngram_example = \
[(1, (u',', u'Deep')), (1, (u',', u'Not')), (1, (u',', u'The')), (1, (u',', u'A')), (1, (u'.', u'From')), 
 (1, (u';', u'The')), (1, (u';', u'Renewed')), (1, (u'A', u'light')), (1, (u'All', u'that')), 
 (1, (u'Deep', u'roots')), (1, (u'From', u'the')), (1, (u'Not', u'all')), (1, (u'Renewed', u'shall')), 
 (1, (u'The', u'crownless')), (1, (u'The', u'old')), (1, (u'a', u'fire')), (1, (u'again', u'shall')), 
 (1, (u'all', u'those')), (1, (u'are', u'not')), (1, (u'are', u'lost')), (1, (u'ashes', u'a')), 
 (1, (u'be', u'king')), (1, (u'be', u'woken')), (1, (u'be', u'blade')), (1, (u'blade', u'that')), 
 (1, (u'broken', u',')), (1, (u'by', u'the')), (1, (u'crownless', u'again')), (2, (u'does', u'not')), 
 (1, (u'fire', u'shall')), (1, (u'from', u'the')), (1, (u'frost', u'.')), (1, (u'glitter', u',')), 
 (1, (u'gold', u'does')), (1, (u'is', u'gold')), (1, (u'is', u'strong')), (1, (u'king', u'.')), 
 (1, (u'light', u'from')), (1, (u'lost', u';')), (1, (u'not', u'glitter')), (1, (u'not', u'reached')), 
 (1, (u'not', u'wither')), (1, (u'old', u'that')), (1, (u'reached', u'by')), (1, (u'roots', u'are')), 
 (1, (u'shadows', u'shall')), (1, (u'shall', u'spring')), (3, (u'shall', u'be')), (1, (u'spring', u';')), 
 (1, (u'strong', u'does')), (1, (u'that', u'was')), (2, (u'that', u'is')), (1, (u'the', u'shadows')), 
 (1, (u'the', u'frost')), (1, (u'the', u'ashes')), (1, (u'those', u'who')), (1, (u'wander', u'are')), 
 (1, (u'was', u'broken')), (1, (u'who', u'wander')), (1, (u'wither', u',')), (1, (u'woken', u',')), 
 ('65',)]

# And the dictionary generated should be:

counted_ngram_dictionary = \
{('All', 'that'): 1, ('blade', 'that'): 1, ('crownless', 'again'): 1, ('light', 'from'): 1, 
 ('not', 'glitter'): 1, ('wither', ','): 1, ('the', 'shadows'): 1, ('is', 'gold'): 1, 
 ('The', 'crownless'): 1, ('king', '.'): 1, ('reached', 'by'): 1, ('From', 'the'): 1, ('The', 'old'): 1, 
 ('frost', '.'): 1, ('glitter', ','): 1, ('by', 'the'): 1, ('be', 'king'): 1, ('shall', 'spring'): 1, 
 ('spring', ';'): 1, ('not', 'reached'): 1, ('not', 'wither'): 1, (';', 'The'): 1, (',', 'Deep'): 1, 
 ('ashes', 'a'): 1, ('woken', ','): 1, ('shadows', 'shall'): 1, ('who', 'wander'): 1, ('does', 'not'): 2, 
 ('be', 'woken'): 1, ('the', 'frost'): 1, ('is', 'strong'): 1, ('are', 'not'): 1, ('gold', 'does'): 1,
 ('old', 'that'): 1, ('was', 'broken'): 1, ('the', 'ashes'): 1, (',', 'Not'): 1, ('shall', 'be'): 3, 
  'Ngrams_Info': ('65',), (';', 'Renewed'): 1, ('wander', 'are'): 1, ('fire', 'shall'): 1, 
 ('again', 'shall'): 1, ('A', 'light'): 1, ('Renewed', 'shall'): 1, ('lost', ';'): 1, (',', 'A'): 1, 
 ('be', 'blade'): 1, ('roots', 'are'): 1, ('Deep', 'roots'): 1, ('all', 'those'): 1, (',', 'The'): 1, 
 ('strong', 'does'): 1, ('those', 'who'): 1, ('from', 'the'): 1, ('.', 'From'): 1, ('Not', 'all'): 1, 
 ('that', 'is'): 2, ('are', 'lost'): 1, ('broken', ','): 1, ('a', 'fire'): 1, ('that', 'was'): 1
 }

# NOTE: As you can see the first value of the tuple in the last position of the list 
#			"counted_ngram_example" is converted in the pair (Ngrams_Info: tuple) in the dictionary.

#		The reason is to encapsulate the extra information about the ngrams in only one key with name
#			Ngrams_Info that will have a tuple (with the aditional info) as a value.


#---------------------------------------------------------------------------------------------------

# File Formats Examples:

# bigrams<Author>.txt  -> <Author> is a variable.
'''
! Excerto  2
! Alguém  1
! Vou  2
( repara  1
( lembrou-se  1
, sebosas  1
, dentro  2
, leite  1
colegas .  2
colegas a  1
colher uns  1
colidiam provocando  1
colisão .  1
potencialmente incompatíveis  1
potentes socos  1
potes ,  1
☺ ,  1
☺ .  1
☺ Para  1
☺ )  1
Ngrams_Info: 92309 
'''

# unigrams<Author>.txt  -> is a variable.
'''
!  310
#  2
Algo  2
Algum  1
Cola  1
Colar  1
Colegas
Espalhe  1
Espanca  8
Espanha  3
JANTAR  2
Jackass  1
Uuuu  1
V-200  1
VEM  1
Vader 1
xixi  1
xixizinho  1
zero  4
zombie  1
zona  3
−  333
Ngram_Info: 92310 
'''
