import json

def parse_json():
    json_data = '{"name": "John", "age": 30, "city": "New York"}'
    data = json.loads(json_data)
    print(data)

parse_json()
