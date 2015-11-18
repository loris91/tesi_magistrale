#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
'''
La classe pros_cons_analyser prende il file supp.json (tale file è formato dai pos_tag delle review) e effettua una
analisi statistica su i pos_tag.
CLASSE DEPRECATA
'''

import os
import re
import json
import nltk
from pprint import pprint

review_folder = "/home/alakay/Scrivania/cache/"

def crea_dizionario():
	dizionario = {}
	dizionario["CC"] = "CC"
	dizionario["CD"] = "CD"
	dizionario["DT"] = "DT"
	dizionario["EX"] = "EX"
	dizionario["FW"] = "FW"
	dizionario["IN"] = "IN"
	dizionario["JJ"] = "JJ"
	dizionario["JJR"] = "JJ"
	dizionario["JJS"] = "JJ"
	dizionario["LS"] = "LS"
	dizionario["MD"] = "MD"
	dizionario["NN"] = "NN"
	dizionario["NNS"] = "NN"
	dizionario["NNP"] = "NNP"
	dizionario["NNPS"] = "NNP"
	dizionario["PDT"] = "PDT"
	dizionario["POS"] = "POS"
	dizionario["PRP"] = "PRP"
	dizionario["PRP$"] = "PRP"
	dizionario["RB"] = "RB"
	dizionario["RBR"] = "RB"
	dizionario["RBS"] = "RB"
	dizionario["RP"] = "RP"
	dizionario["SYM"] = "SYM"
	dizionario["TO"] = "TO"
	dizionario["UH"] = "UH"
	dizionario["VB"] = "VB"
	dizionario["VBD"] = "VB"
	dizionario["VBG"] = "VB"
	dizionario["VBN"] = "VB"
	dizionario["VBP"] = "VB"
	dizionario["VBZ"] = "VB"
	dizionario["WDT"] = "WD"
	dizionario["WP"] = "WD"
	dizionario["WP$"] = "WD"
	dizionario["WRB"] = "WD"
	dizionario[":"] = ":"
	return dizionario

def pros():
	with open(review_folder+"pros.json") as json_file:
		json_data = json.load(json_file)
		json_file.close()

	print len(json_data['opinion'])

	dizionario = crea_dizionario()

	json_lista = {}
	json_lista['bho'] = []

	for opinion in json_data['opinion']:
		lista =[]
		tokens = nltk.word_tokenize(opinion)
		tagged = nltk.pos_tag(tokens)
		for el in tagged:
			print str(el[1])
			element = dizionario[str(el[1])]
			lista.append(element)
		json_lista['bho'].append(lista)

	with open ("/home/alakay/Scrivania/cache/supp.json","w") as myfile:
			json.dump(json_lista, myfile)

def step_2():
	with open(review_folder+"supp.json") as json_file:
		json_data = json.load(json_file)
		json_file.close()

	print len(json_data['bho'])

	maps = {}
	for el in json_data['bho']:
		key = str(el)
		if maps.has_key(key):
			maps[key]=maps[key]+1
		else:
			maps[key]=1
	pprint(maps)

		

if __name__ == "__main__":
	pros()
	step_2()