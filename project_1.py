#Name - Kerrington Jackson
#UMID - 75922020
#Collaborators - 
#AI Use - used ChatGPT for these fixes - 1. helped explain errors with 
# loading my csv file and recommended adding function to handle errors when 
# converting to float 2.

import csv
import unittest
import os

def load_csv_file(f):
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)

    with open(full_path) as fh:
        csv_file = csv.reader(fh)
        headers = next(csv_file)
        info = []
        #create function to deal with csv numbers
        def try_float(value):
            try:
                value = float(value)
            except:
                return 'NA'
        for row in csv_file:
            new_dict = {}
            new_row = row[1:] #get rid of row number
        #row format - Species, island, bill length, 
        # bill depth, flipper length, body mass, sex, year
            new_dict['Species'] = new_row[0]
            new_dict['Island'] = new_row[1]
            new_dict['Bill Length'] = try_float(new_row[2])
            new_dict['Bill Depth'] = try_float(new_row[3])
            new_dict['Flipper Length'] = try_float(new_row[4])
            new_dict['Body Mass'] = try_float(new_row[5])
            new_dict['Sex'] = new_row[6]
            new_dict['Year'] = new_row[7]
            info.append(new_dict)
        print(info)
        return info

load_csv_file('penguins.csv')


