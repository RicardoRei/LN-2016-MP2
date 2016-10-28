
def identifyAuthor(args):
	f1 = open(args[1],'r')
	processed_text = processPunctuation(f1)
	f1.close()
	
	tokens = nltk.word_tokenize(processed_text)
	ngrams = createNgram(args[2], tokens)
	ngramOfUnknownAuthor = countNgramFrequency(list(ngrams))
	
	dictionary=dict()
	for author in ["Tolkien"]:
		dictionary[author] = likelihood(ngramOfUnknownAuthor, author)
		
	print dictionary