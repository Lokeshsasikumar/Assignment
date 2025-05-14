#Exercise 3: Reading JSON from a File

import json

def read_json_from_file():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            print(data)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print("Error reading JSON:", e)

read_json_from_file()
