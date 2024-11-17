import json
import csv

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

def export_choices_to_csv(file_path, choices):
    # Export choices into a csv format
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["choices"]) # Header
        for choice in choices:
            writer.writerow([choice])

def import_choices_from_csv(file_path):
    # Import choices from an existing csv file
    choices = []

    try:
        with open(file_path, mode="r") as file:
            reader = csv.reader(file)
            next(reader, None) # Skip header
            choices = [row[0] for row in reader if row]
    except FileNotFoundError:
        print(f"File {file_path} not found!")
    return choices
