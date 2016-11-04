# -*- coding: utf-8 -*-
import sys
import os
from ngram import *
from text import processText

training_dir = "Corpora/treino/"
test_dir = "Corpora/teste/"

samples_dir = "500Palavras"
authors = ["AlmadaNegreiros", "CamiloCasteloBranco", "EcaDeQueiros", \
		   "JoseRodriguesSantos", "JoseSaramago", "LuisaMarquesSilva"]

def getVocabulary():

	words = set()
	for author in authors:
		print 'starting author: ' + author 
		author_directory = training_dir + author
		author_corpora = ""
		for filename in os.listdir(author_directory):
			print filename
			if "grams" not in filename and filename.endswith(".txt"):
				f = open(author_directory + '/' + filename, 'r')
				author_corpora += processText(file=f).decode('utf-8')
				f.close()

		print 'done ' + author 
		words.update(author_corpora.split())

	return words

def openNgrams(author):
		try:
			f1 = open(training_dir + author + "/unigrams" + author + ".txt", "r")
			f2 = open(training_dir + author + "/bigrams" + author + ".txt", "r")
			return (f1, f2)
		except Exception:
			print "Error opening " + author + " Bigrams or Unigrams"


def getValue(ngram, dictionary):
		try:
			return int(dictionary[ngram]) + 1
		except KeyError:
			return 1

def laplaceCounting(unigrams, bigrams, words, vocabulary):
	v = len(vocabulary)

	SUM = 0
	for i in range(1, 10):
		key = (words[i-1], words[i])
		value1 = getValue(key, bigrams)
		value2 = getValue(words[i-1], unigrams)

		SUM += value1 / float(value2)

	return SUM/float(bigrams["Ngram_Info"][0])

def main():
	vocabulary = getVocabulary()

	for file in os.listdir(test_dir + samples_dir):
		if file and file.endswith(".txt"):
			textFile = open(test_dir + samples_dir + "/" + file, "r")
			words = processText(textFile).decode('utf-8').split()
			closest_author = ("Unkown", float("-inf"))

			for author in authors:
				f1, f2 = openNgrams(author)
				author_unigrams = countedNgramFileToDictionary(file=f1)
				author_bigrams = countedNgramFileToDictionary(file=f2)
				value = laplaceCounting(author_unigrams, author_bigrams, words, vocabulary)

				print 'LAPLACE value: ' + str(value) + ' for author '+ author
				if value > closest_author[1]:
					closest_author = (author, value)
			print closest_author
main()