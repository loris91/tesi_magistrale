#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
'''
import pymongo
from pymongo import MongoClient
from pymongo import Connection


#connection = MongoClient()
#connection.database_names()


connection = Connection()
db = connection['test-database']
collection = db['test-collection']
'''

import pymongo
from bson.objectid import ObjectId


connection = pymongo.Connection()

'''
db = connection["tutorial"]
employees = db["employees"]

# employees.insert({"name": "Lucas Hightower", 'gender':'m', 'phone':'520-555-1212', 'age':8})
# employees.insert({"name": "Loris Marsico", 'gender':'m', 'phone':'327-4698920', 'age':24})
# employees.insert({"name": "Sara Antonelli", 'gender':'s', 'phone':'340-2566980', 'age':24})
# employees.insert({"name": "Luca Marsico", 'gender':'m', 'phone':'390-1267098', 'age':14})

#cursor = db.employees.find()
for employee in db.employees.find():
    print employee
 '''

db = connection["ciao_co_uk"]
products = db["products"]

products.insert({"category":"TVs","section":"plasma","feature":"schermo","polarity":"pros","value":"good"})
products.insert({"category":"TVs","section":"led","feature":"schermo","polarity":"cons","value":"opaco"})
products.insert({"category":"TVs","section":"plasma","feature":"schermo","polarity":"pros","value":"luminoso"})
products.insert({"category":"TVs","section":"plasma","feature":"prezzo","polarity":"pros","value":["basso","accessibbile","buono"]})


for product in db.products.find():
	print product