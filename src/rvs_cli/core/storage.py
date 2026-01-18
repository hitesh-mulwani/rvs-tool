import os
import json

# This defines where your tracking data will be stored
STORE_DIR = ".rvs"
DATA_FILE = os.path.join(STORE_DIR, "data.json")

def init_db():
    """Creates the .rvs directory and an empty data.json if they don't exist."""
    if not os.path.exists(STORE_DIR):
        os.makedirs(STORE_DIR)
        with open(DATA_FILE, "w") as f:
            json.dump({}, f)
        return True
    return False

def load_data():
    """Reads the current tracking data from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_data(data):
    """Saves the updated dictionary back to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def remove_note(filename):
    """Removes a file from the tracking database."""
    data = load_data()
    if filename in data:
        del data[filename]
        save_data(data)
        return True
    return False