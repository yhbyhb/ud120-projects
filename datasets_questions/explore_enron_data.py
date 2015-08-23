# -*- coding: utf-8 -*-
#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import sys
from time import time
sys.path.append("../final_project/")
from poi_email_addresses import poiEmails
sys.path.append("../tools/")
from feature_format import *
from pprint import pprint
import pandas as pd

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

mod_data = []
for k, v in enron_data.iteritems():
	row = v
	row['name'] = k
	mod_data.append(row)
df = pd.DataFrame(mod_data)

print "Data points :", len(enron_data)

print "Featrues :", len(enron_data["SKILLING JEFFREY K"])

print 'number of poi :', len(df[df.poi == True])

# print len(poiEmails())

# What is the total value of the stock belonging to James Prentices
print "James Prentice's Stock :", enron_data['PRENTICE JAMES']['total_stock_value']

# How many email messages do we have from Wesley Colwell to persons of interest?
print "Wesley Colwell's Emails :", enron_data['COLWELL WESLEY']['from_this_person_to_poi']

# What’s the value of stock options exercised by Jeffrey Skilling?
print "Jeff Skilling's Stock Options :", enron_data['SKILLING JEFFREY K']['exercised_stock_options']

# Of these three individuals (Lay, Skilling and Fastow), who took home the most money (largest value of “total_payments” feature)? 
# How much money did that person get?
people = ['LAY KENNETH L', 'SKILLING JEFFREY K', 'FASTOW ANDREW S']
people_df = df.loc[df['name'].isin(people)]
top_payment = people_df['total_payments'].max()
top_payment_name = people_df[people_df.total_payments == top_payment]['name'].values[0]
print "SO MUCH MONEY, name : {}, total_payments : {}".format(top_payment_name, top_payment)

# How many folks in this dataset have a quantified salary? What about a known email address?
print "salary : {}, email address : {}".format(len(df[df.salary != 'NaN']), len(df[df.email_address != 'NaN']))

# Dict-to-array conversion
# data_dictionary = enron_data
# feature_list = ["poi", "salary", "bonus"]
# data_array = featureFormat( data_dictionary, feature_list )
# label, features = targetFeatureSplit(data_array)

# How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments? What percentage of people in the dataset as a whole is this?
nan_payment = len(df[df.total_payments == 'NaN'])
print "{} of {} are NaN. {} %".format(nan_payment, len(df), nan_payment / float(len(df)) * 100.)

# How many POIs in the E+F dataset have “NaN” for their total payments? What percentage of POI’s as a whole is this?
poi_df = df[df.poi == True]
poi_nan_payment = len(poi_df[poi_df.total_payments == 'NaN'])
print "{} of {} are NaN. {} %".format(poi_nan_payment, len(poi_df), poi_nan_payment / float(len(poi_df)) * 100.)
