#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
'''
La classe characteristics_extractor.py ha lo scopo di estrarre le il "nome" delle caratteristiche e non loro valore.
'''

import os
import re
import json
import nltk
from pprint import pprint

category_folder = "/home/alakay/Scrivania/Ciao.co.uk/Category/"
characteristics_folder = "/home/alakay/Scrivania/Ciao.co.uk/Characteristics/"

def estrai(product_folder,file_name):
	with open(product_folder+file_name) as json_file:
		product_json = json.load(json_file)
		json_file.close()

	category = str(product_json['Category'])
	section = str(product_json['Section'])

	try:
		with open(characteristics_folder+category+".json") as json_file:
			data = json.load(json_file)
			json_file.close()

			if section not in data[category].keys():
				data[category][section] = []

	except Exception, e:
		data={}
		data[category] = {}
		data[category][section] = []

	new_list =  []
	for key in product_json['Product_Information'].keys():
		characteristics = product_json['Product_Information'][key]
		for characteristic in characteristics:
			new_list.append(str(characteristic))

	data[category][section] = list(set(data[category][section]+new_list))

	with open (characteristics_folder+category+".json","w") as myfile:
			json.dump(data, myfile)

if __name__ == "__main__":
	list_folder = os.listdir(category_folder)

	for category in list_folder:
		product_folder = category_folder+category+"/product/"
		list_files = os.listdir(product_folder)
		#for i in range(0,11):
		#	print i
		#	file_name = list_files[i]
		for file_name in list_files:
			estrai(product_folder,file_name);
