#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pymongo
import os
import json
from bson.objectid import ObjectId
from pprint import pprint

categories_folder = "/home/alakay/Scrivania/Ciao.co.uk/Category/"

connection = pymongo.Connection()

db = connection["ciao_co_uk"]
products = db["products"]

def calcola(array):
	d = {}
	for text in array:
		key = str(text)

		if key in d.keys():
			d[key] = d[key]+1
		else:
			d[key] = 1

	stat = ""
	for key in d.keys():
		stat = stat + "\t" + str(d[key])
	return d

def inverti(data):
	ret = {}

	for key in data.keys():
		k = data[key]

		if k in ret.keys():
			ret[k].append(key)
		else:
			ret[k]=[key]
	return ret

def calcola_totale():
	elements = db.products.find({})
	print elements.count()

def calcola_totale_pros():
	list_folder = os.listdir(categories_folder)

	elements = db.products.find({"polarity":"pros"})
	#print elements.count()

	for cat in list_folder:
		elem = db.products.find({"category":cat,"polarity":"pros"})
		print cat + "\t" +str(elem.count())

def calcola_totale_cons():
	list_folder = os.listdir(categories_folder)

	elements = db.products.find({"polarity":"cons"})
	#print elements.count()

	for cat in list_folder:
		elem = db.products.find({"category":cat,"polarity":"cons"})
		print cat + "\t" +str(elem.count())

def visualizza_dati():
	elements = db.products.find({"category":"Cameras"})
	for ele in elements:
		print (ele["section"],ele["polarity"],ele["feature"],ele["value"])

if __name__ == "__main__":
	#calcola_totale()
	#calcola_totale_pros()
	#calcola_totale_cons()
	visualizza_dati()

	'''
	list_folder = os.listdir(categories_folder)

	db = connection["ciao_co_uk"]
	products = db["products"]

	for category_name in list_folder:
		a_p = []
		a_c = []

		p_es = db.products.find({"category":category_name,"polarity":"pros"})
		for elem in p_es:
			indicator = elem["value"]
			a_p = a_p + indicator
		p_stat = calcola(a_p)
		p_stat = inverti(p_stat)

		c_es = db.products.find({"category":category_name,"polarity":"cons"})
		for elem in c_es:
			indicator = elem["value"]
			a_c = a_c + indicator
		c_stat = calcola(a_c)
		c_stat = inverti(c_stat)

		print category_name 
		print p_stat
		print c_stat
	'''

