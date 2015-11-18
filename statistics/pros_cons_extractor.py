#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
'''
La classe pros_cons_extractor si occupa di estrarre i commenti PROS e CONS dai file json della cartella review
della categoria scelta. Per ogni review i commenti vengono puliti (eliminati caratteri specili), e le frasi
vengono separate in base ai caratteri [,.!?;] trovati in essa. Infine vengono generati 2 file json contenenti 
i commenti lavorati.

'''

import os
import re
import json
import nltk
from pprint import pprint

category_name = "TVS"


review_folder = "/home/alakay/Scrivania/cache/"+category_name+"/review"

def pulisci(phrase):
	phrase = re.sub(r"&[^;]*;"," ",phrase) #Elimino i caratteri speciali

	phrase = re.sub(r"\{[^}]*\}","",phrase) #Elimino le parentesi {} e il loro contenuto
	phrase = re.sub(r"\[[^\]]*\]","",phrase) #Elimino le parentesi [] e il loro contenuto
	phrase = re.sub(r"\([^)]*\)","",phrase) #Elimino le parentesi () e il loro contenuto

	phrase = re.sub(r" +"," ",phrase) #Elimino gli spazi ripetuti
	return phrase

def split_phrase(phrase,data):
	phrase = re.sub(r"[,.!?;]",".",phrase)
	phrase = phrase.split(".")
	
	for opinion in phrase:
		if nltk.word_tokenize(opinion) != []:
			data['opinion'].append(opinion)

	return data

def analizza_file(file_name,data_pros,data_cons):
	with open(review_folder+"/"+file_name) as json_file:
		json_data = json.load(json_file)
		json_file.close()

	for element in json_data['reviews']:
		pros = pulisci(element["Advantages"])
		split_phrase(pros,data_pros)

		cons = pulisci(element["Disadvantages"])
		split_phrase(cons,data_cons)

	with open ("/home/alakay/Scrivania/cache/"+category_name+"/pros.json","w") as myfile:
			json.dump(data_pros, myfile)

	with open ("/home/alakay/Scrivania/cache/"+category_name+"/cons.json","w") as myfile:
			json.dump(data_cons, myfile)


if __name__ == "__main__":
	list_files = os.listdir(review_folder)

	data_pros = {}
	data_pros['opinion'] = []
	data_cons = {}
	data_cons['opinion'] = []
	
	
	for product in list_files:
		analizza_file(product,data_pros,data_cons)

	print len (data_pros['opinion'])
	print len (data_cons['opinion'])

	with open ("/home/alakay/Scrivania/cache/"+category_name+"/pros.json","w") as myfile:
			json.dump(data_pros, myfile)

	with open ("/home/alakay/Scrivania/cache/"+category_name+"/cons.json","w") as myfile:
			json.dump(data_cons, myfile)