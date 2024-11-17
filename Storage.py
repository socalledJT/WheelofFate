import json

def load_choces(file_path):
    # Loads custom choices from a JSON file
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    
def save_choices(file_path, choices):
    # Save written choices
    with open(file_path, 'w') as file:
        json.dump(choices, file, indent=4)
