import pandas as pd
import glob
import xml.etree.ElementTree as ET
from datetime import datetime
import os

# Set paths
log_file_path = 'log_file.txt'
output_csv_path = 'transformed_data.csv'
input_dir = r'C:\Users\DELL\Downloads\source_unzipped'  # Replace with your unzipped directory path

# Logging function to log progress
def log(message):
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"{datetime.now()}: {message}\n")

# Extraction from CSV files
def extract_from_csv(file_path):
    log(f"Extracting from CSV file: {file_path}")
    return pd.read_csv(file_path)

# Extraction from JSON files
def extract_from_json(file_path):
    log(f"Extracting from JSON file: {file_path}")
    return pd.read_json(file_path, lines=True)


# Extraction from XML files
def extract_from_xml(file_path):
    log(f"Extracting from XML file: {file_path}")
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Assuming XML structure contains records in the 'record' tag
    records = []
    for record in root:
        record_data = {}
        for element in record:
            record_data[element.tag] = element.text
        records.append(record_data)

    return pd.DataFrame(records)

# Master extraction function
def extract_data(files):
    all_data = pd.DataFrame()

    for file in files:
        if file.endswith('.csv'):
            df = extract_from_csv(file)
        elif file.endswith('.json'):
            df = extract_from_json(file)
        elif file.endswith('.xml'):
            df = extract_from_xml(file)
        else:
            log(f"Unsupported file format: {file}")
            continue

        all_data = pd.concat([all_data, df], ignore_index=True)

    return all_data

# Transformation function
def transform_data(df):
    log("Transforming data")

    # Assuming columns 'Height' and 'Weight' exist in the DataFrame
    if 'Height' in df.columns:
        df['Height'] = df['Height'].apply(pd.to_numeric, errors='coerce')
        df['Height'] = df['Height'] * 0.0254  # inches to meters

    if 'Weight' in df.columns:
        df['Weight'] = df['Weight'].apply(pd.to_numeric, errors='coerce')
        df['Weight'] = df['Weight'] * 0.453592  # pounds to kilograms

    return df

# Loading function
def load_data(df, output_file_path):
    log("Loading data into CSV file")
    df.to_csv(output_file_path, index=False)

# Main ETL pipeline function
def etl_pipeline(input_dir):
    log("Starting ETL pipeline")

    # Find all files (CSV, JSON, XML) in the input directory
    input_files = glob.glob(os.path.join(input_dir, '*.*'))

    # Extraction
    extracted_data = extract_data(input_files)

    # Transformation
    transformed_data = transform_data(extracted_data)

    # Loading
    load_data(transformed_data, output_csv_path)

    log("ETL pipeline completed")

# Run the ETL pipeline
if __name__ == "__main__":
    etl_pipeline(input_dir)
    print(f"ETL process completed. Check {output_csv_path} for the result and {log_file_path} for logs.")
