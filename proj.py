
import sys
import os
from ngram import *

#--------------------------------------------------------------------------------------------------
#       							Main module
#--------------------------------------------------------------------------------------------------

training_dir = "Corpora/treino/"
samples_dir = ["500Palavras", "1000Palavras"]
#samples_dir = ["10Palavras"]
#samples_dir = ["developmentCorpus"]

test_dir = "Corpora/teste/"
authors = ["AlmadaNegreiros", "CamiloCasteloBranco", "EcaDeQueiros", \
			"JoseRodriguesSantos", "JoseSaramago", "LuisaMarquesSilva"]
#authors = ["Tolkien"]

def identifyAuthor(dir, ngramType):
	sample_dir = test_dir + dir
	authorText=""
	for file in os.listdir(sample_dir):
		if file and file.endswith(".txt"):
			counted_ngram = createTextCountedNgram(textPath=sample_dir + "/", 
												   textFilename=file, 
												   ngramType=ngramType)
			result = compareWithAuthorsNgrams(ngram=countedNgramToDictionary(counted_ngram), 
											  ngramType=ngramType)
			print 'result for file: ' + file + ' ' + str(result)


def compareWithAuthorsNgrams(ngram, ngramType):
	closest_author = ("Unkown", float("-inf"))
	for author in authors:
		author_file = open(training_dir + author + "/" + ngramType + author + ".txt", "r")
		author_ngram = countedNgramFileToDictionary(file=author_file)
		value = distanceBetweenProfiles(author_ngram, ngram, ngramType)
		author_file.close()
		print 'value: ' + str(value) + ' for author '+ author
		if value > closest_author[1]:
			closest_author = (author, value)

	return closest_author

def distanceBetweenProfiles(knownProfileFile, unknownProfileFile, ngramType):
	def F(ngram, dictionary):
		try:
			return dictionary[ngram]
		except KeyError:
			return 0

	SUM = 0
	for key in unknownProfileFile:
		if key != "Ngram_Info":
			SUM = SUM + int(F(key, knownProfileFile))

	return SUM / float(knownProfileFile["Ngram_Info"][0])

def main():
	cmdargs = sys.argv
	cmd = cmdargs[1]
	ngramType = cmdargs[2]
	
	if cmd == "train":
		for author in authors:
			counted_ngram = createAuthorCountedNgram(author_directory= training_dir + author, 
													 ngramType=ngramType) 
			writeNgramTofile(directoryName=training_dir + author, 
							  name = ngramType + author + ".txt", 
							  counted_ngram=counted_ngram)

	if cmd == "test":
		for dir in samples_dir:
			identifyAuthor(dir=dir, ngramType=ngramType)

main()

 


