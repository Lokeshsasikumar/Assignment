#Exercise 6: Reading CSV with DictReader

import csv

def read_csv_as_dict():
    with open('data.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(row)

read_csv_as_dict()
