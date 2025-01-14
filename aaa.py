import json

def extract_from_json(file_path):
    log(f"Extracting from JSON file: {file_path}")
    data = []
    
    with open(file_path, 'r') as file:
        for line in file:
            try:
                data.append(json.loads(line))  # Attempt to load each line as a JSON object
            except json.JSONDecodeError as e:
                log(f"JSONDecodeError in {file_path}: {e}")
    
    return pd.DataFrame(data)
