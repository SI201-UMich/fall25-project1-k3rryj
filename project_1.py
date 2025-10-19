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
        def try_float(value):
            try:
                value = float(value)
            except:
                return 'NA'
        for row in csv_file:
            print(row)
            new_dict = {}
        #row format - Species, island, bill length, 
        # bill depth, flipper length, body mass, sex, year
            new_dict['Species'] = row[1]
            new_dict['Island'] = row[2]
            new_dict['Bill Length'] = try_float(row[3])
            new_dict['Bill Depth'] = try_float(row[4])
            new_dict['Flipper Length'] = try_float(row[5])
            new_dict['Body Mass'] = try_float(row[6])
            new_dict['Sex'] = row[7]
            new_dict['Year'] = row[8]
            info.append(new_dict)
        #print(info)
        return info

load_csv_file('penguins.csv')


