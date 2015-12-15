#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

'''
La classe offre delle analisi statistiche su i dati memorizzati nel DB
'''

import pymongo
import os
import json
from bson.objectid import ObjectId
from pprint import pprint
import collections

categories_folder = "/home/alakay/Scrivania/Ciao.co.uk/Category/"
list_folder = os.listdir(categories_folder)

connection = pymongo.Connection()

db = connection["ciao_co_uk"]
products = db["products"]


def calcola_totale():
	elements = db.products.find({})
	print elements.count()
	print ""

def calcola_totale_pros():
	elements = db.products.find({"polarity":"pros"})
	#print elements.count()

	for cat in list_folder:
		elem = db.products.find({"category":cat,"polarity":"pros"})
		print cat + "\t" +str(elem.count())
	print ""

def calcola_totale_cons():
	elements = db.products.find({"polarity":"cons"})
	#print elements.count()

	for cat in list_folder:
		elem = db.products.find({"category":cat,"polarity":"cons"})
		print cat + "\t" +str(elem.count())
	print ""

def visualizza_dati_categoria(category_name):
	elements = db.products.find({"category":category_name})
	for ele in elements:
		print (ele["section"],ele["polarity"],ele["feature"],ele["value"])

def calcola_termini_feature_pros():
	for cat in list_folder:
		dic = {}
		elements = db.products.find({"category":cat,"polarity":"pros"})
		for el in elements:
			feature = el["feature"]
			size = len(feature.split())
			if size in dic.keys():
				dic[size] = dic[size] +1
			else:
				dic[size] = 1
		print "Pros, Categoria: " + cat + "\t" + str(dic)

def calcola_termini_feature_cons():
	for cat in list_folder:
		dic = {}
		elements = db.products.find({"category":cat,"polarity":"cons"})
		for el in elements:
			feature = el["feature"]
			size = len(feature.split())
			if size in dic.keys():
				dic[size] = dic[size] +1
			else:
				dic[size] = 1
		print "Cons, Categoria: " + cat + "\t" + str(dic)


def calcola_termini_indicator_pros():
	for cat in list_folder:
		dic = {}
		elements = db.products.find({"category":cat,"polarity":"pros"})
		for el in elements:
			feature_indicator = el["value"]
			for a in feature_indicator:
				size = len(a.split())
				if size in dic.keys():
					dic[size] = dic[size] +1
				else:
					dic[size] = 1
		print "Pros, Categoria: " + cat + "\t" + str(dic)

def calcola_termini_indicator_cons():
	for cat in list_folder:
		dic = {}
		elements = db.products.find({"category":cat,"polarity":"cons"})
		for el in elements:
			feature_indicator = el["value"]
			for a in feature_indicator:
				size = len(a.split())
				if size in dic.keys():
					dic[size] = dic[size] +1
				else:
					dic[size] = 1
		print "Cons, Categoria: " + cat + "\t" + str(dic)

def inverti(data):
	ret = {}

	for key in data.keys():
		k = data[key]

		if k in ret.keys():
			ret[k].append(key)
		else:
			ret[k]=[key]
	return ret

def trova_maggiore(data):
	print max(data.keys())


def trova_feature_indicator_frequenti_pros():
	for category_name in list_folder:
		dic = {}
		elements = db.products.find({"category":category_name,"polarity":"pros"})
		for el in elements:
			feature_indicator = el["value"]
			for a in feature_indicator:
				if a in dic.keys():
					dic[a] = dic[a]+1
				else:
					dic[a]=1
		dic = inverti(dic)

		a =   collections.OrderedDict(sorted(dic.items(), key=lambda t: t[0], reverse=True))
		keys = a.keys()
		l_keys = len(keys)
		first = (keys[0], a[keys[0]])
		second = (keys[1], a[keys[1]])
		third = (keys[2], a[keys[2]])
		print category_name + "\t" + str(first) + "\t" + str(second) + "\t" + str(third)
		print ""

def trova_feature_indicator_frequenti_cons():
	for category_name in list_folder:
		dic = {}
		elements = db.products.find({"category":category_name,"polarity":"cons"})
		for el in elements:
			feature_indicator = el["value"]
			for a in feature_indicator:
				if a in dic.keys():
					dic[a] = dic[a]+1
				else:
					dic[a]=1
		dic = inverti(dic)

		a =   collections.OrderedDict(sorted(dic.items(), key=lambda t: t[0], reverse=True))
		keys = a.keys()
		l_keys = len(keys)
		first = (keys[0], a[keys[0]])
		second = (keys[1], a[keys[1]])
		third = (keys[2], a[keys[2]])
		print category_name + "\t" + str(first) + "\t" + str(second) + "\t" + str(third)
		print ""


if __name__ == "__main__":
	#calcola_totale()
	#calcola_totale_pros()
	#calcola_totale_cons()
	#visualizza_dati_categoria("Cameras")

	#calcola_termini_feature_pros()
	#calcola_termini_feature_cons()

	#calcola_termini_indicator_pros()
	#calcola_termini_indicator_cons()

	#trova_feature_indicator_frequenti_pros()
	trova_feature_indicator_frequenti_cons()

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

