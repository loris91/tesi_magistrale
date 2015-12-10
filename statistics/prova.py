#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os
import re
import json
import nltk
from pprint import pprint

variabile_globale = ""

def func1():
	global variabile_globale 
	print variabile_globale
	variabile_globale = "Primo Cambiamento"

def func2():
	global variabile_globale 
	variabile_globale = "Secondo Cambiamento"

def func3():
	stringa = variabile_globale
	print stringa

def get_bigram(parole):
	bigram =[]
	for i in range(1,len(parole)):
		tmp = str(parole[i-1]) +" " + str(parole[i])
		bigram.append(tmp)
	return bigram

def verifica_1gram(stringa,char):
	parole = stringa.split(" ")
	for p in parole:
		if p in char:
			return p

def verifica_2gram(stringa,char):
	parole = stringa.split(" ")
	parole = get_bigram(parole)
	for p in parole:
		if p in char:
			return p

if __name__ == "__main__":
	
	
	phrase = "EASY TO USE"
	phrase = phrase.lower()
	print phrase
	tokens = nltk.word_tokenize(phrase)
	tagged = nltk.pos_tag(tokens)
	print tagged
	print "\n____________________\n"

	


	'''
	char = ["Long Name", "EAN", "MPN", "Genre", "Subgenre", "Type", "Manufacturer"]

	for e in char[0:2]:
		print e

	stringa = "Puprle"
	find = verifica_1gram(stringa,char)
	if find is None:
		find = verifica_2gram(stringa,char)
	if find is None:
		print "Caratteristica non presente"
	else:
		print "Caratteristica trovata: " + find



	a = (b == true ? "123" : "456" )
	a = '123' if b else '456'

	'''
	'''
	a = 1
	b = a if (a<8) else '>7'

	print ('a',a)
	print ('b',b)

	a = 8
	b = a if (a<8) else '>7'

	print ('a',a)
	print ('b',b)

	a = 10
	b = a if (a<8) else '>7'

	print ('a',a)
	print ('b',b)
	'''