import json

def load_json(file, mode='r'):
    with open(file, mode) as f:
        return json.load(f)
    
def save_json(data, file, mode='w'):
    with open(file, mode) as f:
        json.dump(data, f, indent=4)