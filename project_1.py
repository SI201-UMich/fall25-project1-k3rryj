#Project 1 - Penguin Data Analysis
#Name - Kerrington Jackson
#UMID - 75922020
#email - kerryjac@umich.edu
#Collaborators - GenAI
#AI Use - used ChatGPT for these fixes - 1. helped explain errors with 
# loading my csv file and recommended adding function to handle errors when 
# converting to float 2. used it to help generate test cases but edited them
# to make sure they matched my actual sample data 3. used it to 
# help with smaller helper functions specifically the function checkers which 
# handle messy data #had it recommend minor fixes too impove functions - added strip() and upper() to check for na/none to
#cover more cases 4. used it to help fix my mistakes when writing my output function

import csv
import unittest
import os

def load_csv_file(f):
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)

    with open(full_path) as fh:
        csv_file = csv.reader(fh)
        headers = next(csv_file)
        file_info = []
        
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
            file_info.append(new_dict)
        return file_info

#create function to deal with csv numbers    
def try_float(value):
            try:
                return float(value)
            except:
                return "NA"
            
def body_mass_valid_row(row_info):
    check = ['Body Mass', 'Species', 'Year']
    for item in check:
        if str(row_info.get(item)).strip().upper()  in [" ", "NA", None, "NONE", ""]: #or row_info[item]
            return False
    return True
   


def calculate_mass(file_info):
    mass_dict = {}
    for row in file_info:
        if not body_mass_valid_row(row): #skip rows that have issues with data
            continue
        species = row['Species']
        year = row['Year']
        mass = row['Body Mass']

        if species not in mass_dict:
            mass_dict[species] = {}
        if year not in mass_dict[species]:
            mass_dict[species][year] = []

        mass_dict[species][year].append(mass)
    return mass_dict
            
def calculate_avg(nested_dict):
    avg_dict = {}
    for species, years in nested_dict.items():
        sort_years = sorted(years.keys(), key=int)
        avg_dict[species] = {}
        for year in sort_years:
            mass = years[year]
            if len(mass)>0:
                avg = sum(mass)/len(mass)
                avg_dict[species][year] = round(avg,2)
            else:
                avg_dict[species][year] = None
    return avg_dict


def calculate_body_mass_by_species_and_year(file_info):
    body_mass_dict = calculate_mass(file_info)
    mass_avg_dict = calculate_avg(body_mass_dict)
    print(mass_avg_dict)
    return mass_avg_dict                

def bill_length_valid_row(row_info):
    check = ['Bill Length', 'Sex', 'Island']
    for item in check:
        if str(row_info.get(item)).strip().upper()  in [" ", "NA", None, "NONE", ""]:
            return False
    return True

def create_bill_per_dict(file_info, threshold):
    bill_len_dict = {}
    percent_dict = {}
    for row in file_info:
        if not bill_length_valid_row(row):
            continue

        island = row['Island']
        sex = row['Sex']
        bill_len = row['Bill Length']

        if island not in bill_len_dict:
            bill_len_dict[island] = {}
        if sex not in bill_len_dict[island]:
            bill_len_dict[island][sex] = {'valid': 0, 'total': 0}

        bill_len_dict[island][sex]['total'] += 1

        if bill_len>threshold:
            bill_len_dict[island][sex]['valid'] += 1

    for islands, sexes in bill_len_dict.items():
        percent_dict[islands] = {}
        for sex, values in sexes.items():
            if values['total']>0:
                percent = (values['valid']/values['total']) * 100
            else:
                percent = 0
            percent_dict[islands][sex] = f"{percent:.2f}%"
    return percent_dict
        
def save_results(file_info, threshold=40, output='penguin_data_results.csv'):
    body_mass_result = calculate_body_mass_by_species_and_year(file_info)
    bill_per_result = create_bill_per_dict(file_info, threshold)

    with open(output, 'w', newline='') as fh:
        writer = csv.writer(fh)
        writer.writerow(["Average Body Mass by Species and Year"])
        writer.writerow(["Species", "Year", "Average Body Mass (g)"])
        for species, years in body_mass_result.items():
            for year, avg in years.items():
                writer.writerow([species, year, avg])
        
        writer.writerow([])
        writer.writerow([f"Bill Length Percentage (> {threshold} mm) by Sex and Island"])
        writer.writerow(["Island", "Sex", "Percent Above Threshold"])
        for island, sexes in bill_per_result.items():
            for sex, percent in sexes.items():
                writer.writerow([island, sex, percent])

    print(f"Results have been saved to {output}")





class TestAllMethod(unittest.TestCase):
    def setUp(self):
        self.penguin_info = load_csv_file('penguins.csv')

    def test_body_mass_gen1(self):
        input_data = [
            {'Species': 'Adelie', 'Body Mass': 3750, 'Year': '2007'},
            {'Species': 'Adelie', 'Body Mass': 3800, 'Year': '2008'},
            {'Species': 'Gentoo', 'Body Mass': 5000, 'Year': '2009'},
            {'Species': 'Chinstrap', 'Body Mass': 4050, 'Year': '2009'}
]
        expected = {'Adelie': {'2007': 3750.00, '2008': 3800.00}, 'Gentoo': {'2009': 5000.00},'Chinstrap': {'2009': 4050.00}}
        result = calculate_body_mass_by_species_and_year(input_data)
        self.assertEqual(result, expected)


    def test_body_mass_gen2(self):
        input_data = [
            {'Species': 'Adelie', 'Body Mass': 3750, 'Year': '2007'},
            {'Species': 'Adelie', 'Body Mass': 3800, 'Year': '2007'},
            {'Species': 'Adelie', 'Body Mass': 3250, 'Year': '2007'},
            {'Species': 'Adelie', 'Body Mass': 3450, 'Year': '2007'}
]
        expected = {'Adelie': {'2007': 3562.50}}
        result = calculate_body_mass_by_species_and_year(input_data)
        self.assertEqual(result, expected)
        



    def test_body_mass_edge1(self):
        input_data = [
            {'Species': 'Adelie', 'Body Mass': 'NA', 'Year': '2007'},
            {'Species': 'Gentoo', 'Body Mass': None, 'Year': '2009'}
]
        expected = {}
        result = calculate_body_mass_by_species_and_year(input_data)
        self.assertEqual(result, expected)
    
    def test_body_mass_edge2(self):
        input_data = []
        expected = {}
        result = calculate_body_mass_by_species_and_year(input_data)
        self.assertEqual(result, expected)
    
    def test_bill_length_gen1(self):
        input_data = [
            {'Island': 'Torgersen', 'Sex': 'male', 'Bill Length': 39.1},
            {'Island': 'Torgersen', 'Sex': 'female', 'Bill Length': 39.5},
            {'Island': 'Torgersen', 'Sex': 'male', 'Bill Length': 42.0}
]
        threshold = 40
        expected = {'Torgersen': {'male': '50.00%','female': '0.00%'}}
        result = create_bill_per_dict(input_data, threshold)
        self.assertEqual(result, expected)

    def test_bill_length_gen2(self):
        input_data = [
            {'Island': 'Torgersen', 'Sex': 'male', 'Bill Length': 39.1},
            {'Island': 'Dream', 'Sex': 'female', 'Bill Length': 45.0},
            {'Island': 'Biscoe', 'Sex': 'male', 'Bill Length': 41.0}
]
        expected = {'Torgersen': {'male': '0.00%'},'Dream': {'female': '100.00%'},'Biscoe': {'male': '100.00%'}}
        threshold = 40
        result = create_bill_per_dict(input_data, threshold)
        self.assertEqual(result, expected)

    def test_bill_length_edge1(self):
        input_data = [
            {'Island': 'Torgersen', 'Sex': None, 'Bill Length': 39.1},
            {'Island': 'Dream', 'Sex': 'female', 'Bill Length': 'NA'}
]
        threshold = 40
        expected = {}
        result = create_bill_per_dict(input_data, threshold)
        self.assertEqual(result, expected)

    def test_bill_length_edge2(self):
        input_data = [
            {'Island': 'Torgersen', 'Sex': 'male', 'Bill Length': 40.0}
]
        threshold = 40
        expected = {'Torgersen': {'male': '0.00%'}}
        result = create_bill_per_dict(input_data, threshold)
        self.assertEqual(result, expected)




def main():
    penguin_info = load_csv_file('penguins.csv')
    calculate_body_mass_by_species_and_year(penguin_info)
    create_bill_per_dict(penguin_info, 40)
    save_results(penguin_info, threshold=40, output='penguin_data_results.csv')
    unittest.main(verbosity=2)


if __name__ == '__main__':
    main()

