#Exercise 5: Writing CSV

import csv

def write_csv():
    data = [
        {'name': 'John', 'age': 30, 'city': 'New York'},
        {'name': 'Alice', 'age': 25, 'city': 'London'}
    ]
    with open('output.csv', mode='w', newline='') as file:
        fieldnames = ['name', 'age', 'city']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

write_csv()
