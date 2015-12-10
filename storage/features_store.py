#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

'''
La classe feature_store.py legge i file feature_indicator.json di ogni categoria e ne salva il contenuto nel DB
'''

import pymongo
import os
import json
from bson.objectid import ObjectId
from pprint import pprint

categories_folder = "/home/alakay/Scrivania/Ciao.co.uk/Category/"

connection = pymongo.Connection()
db = connection["ciao_co_uk"]
products = db["products"]

if __name__ == "__main__":
	list_folder = os.listdir(categories_folder)

	for category_name in list_folder:
	#category_name = list_folder[0]
		category_folder = "/home/alakay/Scrivania/Ciao.co.uk/Category/"+category_name+"/"
			
		with open(category_folder+"feature_indicator.json") as json_file:
			json_data = json.load(json_file)
			json_file.close()
		
		for section in json_data.keys():
			for feature in json_data[section].keys():
				for polarity in json_data[section][feature].keys():
					value = json_data[section][feature][polarity]
					print (section,feature,polarity,value)
					element = {}
					element['section']=section
					element['feature']=feature
					element['polarity']=polarity
					element['value']=value
					products.insert(element)