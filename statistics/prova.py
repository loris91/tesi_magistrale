#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import re
import nltk
from pprint import pprint

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

	data = {}

	data['TVs'] = {}

	data['TVs']['Color'] = []

	data['TVs']['Color'].append("Schermo")
	data['TVs']['Color'].append("Batteria")
	data['TVs']['Color'].append("Tastiera")

	lista = ["Audio","Schermo","Puppa"]

	data['TVs']['Color'] = list(set(data['TVs']['Color'] + lista))

	'''
	if 'Plasma' in data['TVs'].keys():
		data['TVs']['Plasma'].append("Schermo")
		data['TVs']['Plasma'].append("Batteria")
		data['TVs']['Plasma'].append("Tastiera")
	else :
		data['TVs']['Plasma'] = []
		data['TVs']['Plasma'].append("Schermo")
		data['TVs']['Plasma'].append("Batteria")
		data['TVs']['Plasma'].append("Tastiera")
	'''
	if 'Plasma' not in data['TVs'].keys():		
		data['TVs']['Plasma'] = []
	data['TVs']['Plasma'].append("Schermo")
	data['TVs']['Plasma'].append("Batteria")
	data['TVs']['Plasma'].append("Tastiera")



	pprint(data)