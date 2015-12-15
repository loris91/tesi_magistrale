#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

'''
La classe offre una prova nel cercare le feature all'interno delle review
'''

import os
import re
import json
import nltk
import nltk.data
from pprint import pprint

import pymongo
from bson.objectid import ObjectId


categories_folder = "/home/alakay/Scrivania/Ciao.co.uk/Category/"

connection = pymongo.Connection()

db = connection["ciao_co_uk"]
products = db["products"]


if __name__ == "__main__":
	path = "/home/alakay/Scrivania/Ciao.co.uk/Category/Cameras/review/"
	file_name = "Boots.json"
	category = "Cameras"
	section = "Photo Developing"

	with open(path+file_name) as json_file:
		data = json.load(json_file)
		json_file.close()

	review = data["reviews"][0]["Review"]
	#print review + "\n"

	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

	for phase in  tokenizer.tokenize(review):
		words = phase.split()
		for word in words:
			el = db.products.find({"category":category,"section":"Photo Developing","feature":"word"})
			if el is not None:
				print "Parola trovata: " + word
				print "Frase partenza: " + phase
				print "Elemento DB: " + str(el)
				print ""
