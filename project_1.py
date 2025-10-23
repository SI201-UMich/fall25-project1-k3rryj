#Name - Kerrington Jackson
#UMID - 75922020
#Collaborators - 
#AI Use - used ChatGPT for these fixes - 1. helped explain errors with 
# loading my csv file and recommended adding function to handle errors when 
# converting to float 2. used it to help generate test cases

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


"""class TestAllMethod(unittest.TestCase):
    def setUp(self):
        self.penguin_info = load_csv_file('penguins.csv')

    def test_body_mass_gen1(self):
        input_data = [
            {'species': 'Adelie', 'body_mass_g': 3750.0, 'year': 2007},
            {'species': 'Adelie', 'body_mass_g': 3800.0, 'year': 2007},
            {'species': 'Adelie', 'body_mass_g': 3250.0, 'year': 2007},
        ]
        expected = {('Adelie', 2007): 3600.0}
        result = avg_body_mass_species_year(input_data)
        self.assertEqual(result, expected)


    def test_body_mass_gen2(self):
        input_data = [
            {'species': 'Adelie', 'body_mass_g': 3600.0, 'year': 2007},
            {'species': 'Gentoo', 'body_mass_g': 5000.0, 'year': 2009},
        ]
        expected = {('Adelie', 2007): 3600.0, ('Gentoo', 2009): 5000.0}
        result = avg_body_mass_species_year(input_data)
        self.assertEqual(result, expected)

    def test_body_mass_edge1(self):
        input_data = [
            {'species': 'Adelie', 'body_mass_g': None, 'year': 2007},
            {'species': 'Adelie', 'body_mass_g': 3700.0, 'year': 2007},
        ]
        expected = {('Adelie', 2007): 3700.0}
        result = avg_body_mass_species_year(input_data)
        self.assertEqual(result, expected)
    
    def test_body_mass_edge2(self):
        input_data = [
            {'species': 'Chinstrap', 'body_mass_g': 3750.0, 'year': 2008},
        ]
        expected = {('Chinstrap', 2008): 3750.0}
        result = avg_body_mass_species_year(input_data)
        self.assertEqual(result, expected)
    
    def test_flipper_length_gen1(self):
        nput_data = [
            {'species': 'Adelie', 'sex': 'male', 'flipper_length_mm': 181.0},
            {'species': 'Adelie', 'sex': 'female', 'flipper_length_mm': 186.0},
            {'species': 'Adelie', 'sex': 'female', 'flipper_length_mm': 195.0},
        ]
        expected = {
            'Adelie': {'male_avg': 181.0, 'female_avg': 190.5, 'difference': -9.5}
        }
        result = compare_flipper_length_by_sex(input_data)
        self.assertEqual(result, expected)

    def test_flipper_length_gen2(self):
        input_data = [
            {'species': 'Adelie', 'sex': 'male', 'flipper_length_mm': 181.0},
            {'species': 'Gentoo', 'sex': 'female', 'flipper_length_mm': 210.0},
            {'species': 'Gentoo', 'sex': 'male', 'flipper_length_mm': 220.0},
        ]
        expected = {
            'Adelie': {'male_avg': 181.0, 'female_avg': None, 'difference': None},
            'Gentoo': {'male_avg': 220.0, 'female_avg': 210.0, 'difference': 10.0},
        }
        result = compare_flipper_length_by_sex(input_data)
        self.assertEqual(result, expected)

    def test_flipper_length_edge1(self):
        input_data = [
            {'species': 'Chinstrap', 'sex': None, 'flipper_length_mm': 200.0},
            {'species': 'Chinstrap', 'sex': 'male', 'flipper_length_mm': 205.0},
        ]
        expected = {
            'Chinstrap': {'male_avg': 205.0, 'female_avg': None, 'difference': None}
        }
        result = compare_flipper_length_by_sex(input_data)
        self.assertEqual(result, expected)

    def test_flipper_length_edge1(self):
        input_data = [
            {'species': 'Gentoo', 'sex': 'female', 'flipper_length_mm': 215.0},
        ]
        expected = {
            'Gentoo': {'male_avg': None, 'female_avg': 215.0, 'difference': None}
        }
        result = compare_flipper_length_by_sex(input_data)
        self.assertEqual(result, expected)

#come back and double check code when fiinished with functions
#edit/replace function names
"""""

load_csv_file('penguins.csv')




#def main():
 #   unittest.main(verbosity=2)

#if __name__ == '__main__':
  #  main()

