# -*- coding: utf-8 -*-
import sys
import re
import os
import nltk
import nltk.tokenize
from nltk import bigrams
from nltk import trigrams


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
#	Function that receives a list of ngram_token and returns a list of pairs (count, (word1, word2))
#
#	ex: input = [('volta', 'ter'), ('porque', 'era'), ('volta', 'ter')]
#		output = [(2, ('volta', 'ter')), (1, ('porque', 'era'))]
def countNgramFrequency(ngram_tokens):
	from collections import defaultdict

	counts = defaultdict(int)
	for bigram in ngram_tokens:
		counts[bigram] += 1

	result = list()
	for bigram, count in counts.iteritems():
		result.append((count, bigram))

	result.sort(reverse=True)
	return result


#writes .txt according to professors' specification	
def writeToFile(countedNgram,authorName,ngramas):
	directoryName = "Corpora/treino/"+authorName+"/"
	newFilename = ngramas+authorName+".txt"
	
	os.chdir(directoryName)
	if os.path.isfile(newFilename):
		os.remove(newFilename)
		
	os.mknod(newFilename)
	outputFile=open(newFilename,"w")
	for element in countedNgram:
		new=""
		for i in element[1]:
			new=new+i+" "
		outputFile.write(new +" "+str(element[0])+"\n")
		
#ngram is the number corresponding to n-gram, EX: if we want to calculate probabilities over bigrams, ngram should be bi		
def probabilities(filename,ngram):
	fileIn=open(filename,'r')
	for line in f:
		print "bla"



			
	
#so far, we have all texts from a specific author in variable authorText
#ex: python proj.py Corpora/treino/Einstein bigramas
def main():
	cmdargs=sys.argv
	authorText=""
	for file in os.listdir(cmdargs[1]):
		if "gramas" not in str(file):
			f=open(cmdargs[1]+"/"+file,'r')
			processed_text = processPunctuation(f)
			authorText+=processed_text+"\n"
			f.close()
			print "read from :"+str(file)
	
	authorPath=cmdargs[1].split("/")
	authorName=authorPath[2]
	
	tokens = nltk.word_tokenize(authorText)
	
	ngramas=cmdargs[2]
	
	if ngramas=="bigramas":
		tokens = nltk.bigrams(tokens)
	if ngramas=="trigramas":
		tokens = nltk.trigrams(tokens)
		
	counted_ngram = countNgramFrequency(list(tokens))
	
	
	writeToFile(counted_ngram,authorName,ngramas)
	
	
	#tokens = [token.lower() for token in tokens if (len(token) > 1)] #same as unigrams
	
	
	
	
	
	
main()
