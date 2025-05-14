import json

def write_json_to_file():
    data = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    with open('data.json', 'w') as file:
        json.dump(data, file)

write_json_to_file()
