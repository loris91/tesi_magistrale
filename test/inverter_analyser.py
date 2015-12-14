#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

'''
La classe analyser.py prende in input i file temporanei tmp_cat.txt generati dalla classe filter.py e 
ne analizza il contenuto andato ad estrarre feature e feature_indicator da ogni singolo commento.
In questo passo una feature è una sequenza di parole consecutive non vuota di ["NN","NNS","NNP","NNPS"]
cioè nomi e nomi propri, mentre
un feature_indicator è una sequenza di parole consecutive non vuota di ["JJ","JJR","JJS","RB","RBR","RBS"],
cioè aggettivi o avverbi.
Vengono salvati tutti quei commenti in cui è presente almeno il feature_indicator.
Per ogni categoria viene generato un file json in cui si memorizza
	dictionary_json[section][feature][polarity]=list[value]
'''

import os
import re
import json
import nltk
from pprint import pprint
from nltk.stem.snowball import SnowballStemmer

categories_folder = "/home/alakay/Scrivania/Ciao.co.uk/Category/"

characteristics_folder = "/home/alakay/Scrivania/Ciao.co.uk/Characteristics/"

feature_pos_tag = ["NN","NNS","NNP","NNPS"]
value_pos_tag = ["JJ","JJR","JJS","RB","RBR","RBS"]
st = SnowballStemmer("english")


def trova_caratteristica(tagged):
	for i in range(0,len(tagged)):
		element = tagged[i]
		if element[1] in feature_pos_tag:
			if len(tagged)>i+1 :
				if tagged[i+1][1] in feature_pos_tag:
					return str(element[0])+" "+str(tagged[i+1][0])
			return str(element[0])

def trova_valore(tagged):
	for i in range(0,len(tagged)):
		element = tagged[i]
		if element[1] in value_pos_tag:
			if len(tagged)>i+1 :
				if tagged[i+1][1] in value_pos_tag:
					return str(element[0])+" "+str(tagged[i+1][0])
			return str(element[0])

def compatta(array):
	stringa = ""
	for el in array:
		stringa+=el[0]+" "
	return stringa



def analizza_categoria(category_name):
	category_folder = "/home/alakay/Scrivania/Ciao.co.uk/Category/"+category_name+"/"
	
	with open(category_folder+"tmp_file.txt") as tmp_pros_file:
		content = tmp_pros_file.read().splitlines()

	dictionary = {}

	for tupla in content:
		(section,polarity,tagged) = eval(tupla)

		if section not in dictionary.keys():
			dictionary[section]={}

		feature = trova_caratteristica(tagged)



		value = trova_valore(tagged)
		if value is None:
			print compatta(tagged) + "\t|###|\t" + str(tagged)



if __name__ == "__main__":
	list_folder = os.listdir(categories_folder)

	analizza_categoria("Small Kitchen Appliances")