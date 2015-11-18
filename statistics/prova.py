#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import re
import nltk

if __name__ == "__main__":
	'''
	phrase = "Terrible lead channel . No effects loop . No footswitchable channels !! !"	
	print phrase
	print "\n____________________\n"

	tokens = nltk.word_tokenize(phrase)
	print tokens
	print "\n____________________\n"

	tagged = nltk.pos_tag(tokens)
	print tagged
	print "\n____________________\n"

	entities = nltk.chunk.ne_chunk(tagged)
	print entities
	print "\n____________________\n"
	'''

	phrase = "Hard drive (HD) is amazing and the pen drive [128MB of memory] is usefull {price (and not only)is very hight}, but is cool!"

	phrase = re.sub(r"\{[^}]*\}","",phrase) #Elimino le parentesi {} e il loro contenuto
	phrase = re.sub(r"\[[^\]]*\]","",phrase) #Elimino le parentesi [] e il loro contenuto
	phrase = re.sub(r"\([^)]*\)","",phrase) #Elimino le parentesi () e il loro contenuto
	phrase = re.sub(r" +"," ",phrase)

	print phrase