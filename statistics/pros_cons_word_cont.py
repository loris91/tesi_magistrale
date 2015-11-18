#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

'''
La classe pros_cons_word_cout analizza i file generati dalla classe pros_cons_extractor.
Per ogni file si dividono i commenti in base al numero di parole di cui il commento è formato, si conta 
di quante parole sono composti i commenti e se ne calcola la media. Tutte le informazioni vengono salvate in un file
json statistiche.json

'''
import os
import re
import json
import nltk
from pprint import pprint

category_name = "TVS"

review_folder = "/home/alakay/Scrivania/cache/"+category_name+"/"

def pros_work():
	with open(review_folder+"pros.json") as json_file:
		json_data = json.load(json_file)
		json_file.close()

	json_stat = {}
	json_stat['Tipo'] = "Commenti PROS"


	numero_commenti = len(json_data['opinion'])
	somma =0

	for opinion  in json_data['opinion']:
		tokens = nltk.word_tokenize(opinion)
		somma = somma + len(tokens)
		key = str(len(tokens))
		if json_stat.has_key(key):
			json_stat[key]=json_stat[key]+1
		else:
			json_stat[key]=1

	media = float(somma)/float(numero_commenti)
	media = str(media)
	media = re.sub(r"\.",",",media)

	json_stat['Numero_Commenti'] = str(numero_commenti)
	json_stat['Media'] = str(media)
	with open ("/home/alakay/Scrivania/cache/"+category_name+"/statistiche.json","a") as myfile:
			json.dump(json_stat, myfile)


def cons_work():
	with open(review_folder+"cons.json") as json_file:
		json_data = json.load(json_file)
		json_file.close()

	numero_commenti = len(json_data['opinion'])
	somma =0

	json_stat = {}
	json_stat['Tipo'] = "Commenti CONS"

	for opinion  in json_data['opinion']:
		tokens = nltk.word_tokenize(opinion)
		somma = somma + len(tokens)
		key = str(len(tokens))
		if json_stat.has_key(key):
			json_stat[key]=json_stat[key]+1
		else:
			json_stat[key]=1

	media = float(somma)/float(numero_commenti)
	media = str(media)
	media = re.sub(r"\.",",",media)

	json_stat['Numero_Commenti'] = str(numero_commenti)
	json_stat['Media'] = str(media)
	with open ("/home/alakay/Scrivania/cache/"+category_name+"/statistiche.json","a") as myfile:
			json.dump(json_stat, myfile)


if __name__ == "__main__":
	pros_work()
	cons_work()