#ETL Data Pipeline Project

Project Overview
This project demonstrates the extraction, transformation, and loading (ETL) process using Python. The ETL pipeline extracts data from various file formats (CSV, JSON, XML), transforms the data by standardizing units of measurement, and loads the processed data into a structured CSV file for further analysis. The project also incorporates logging to track the progress of each phase of the ETL process.

Problem Statement
In many real-world scenarios, data comes from multiple sources and formats. This project simulates the extraction of data from different file types (CSV, JSON, XML), processes the extracted data to convert measurements into a standardized format, and saves the output to a structured format for analysis.

Tools Used
Python: Programming language used for implementing the ETL pipeline.
Pandas: For data manipulation and analysis.
glob: For handling file formats.
xml.etree.ElementTree: To parse XML data.
datetime: To track the progress of each phase through logging.
logging: To log the ETL process steps for auditing and debugging.

.
Extracted the Data with given link In source.zip 
Then Unzipped It as Source_unzipped.csv
├── ETL.py                # Main Python script for the ETL pipeline
├── log_file.txt          # Logs for the ETL process
└── data/
    ├── source_unzipped/  # Unzipped data files
        ├── data.csv      # Sample CSV file
        ├── data.json     # Sample JSON file
        ├── data.xml      # Sample XML file
    └── transformed_data.csv  # Final transformed data in CSV format

#ETL Process
1. Extraction
The ETL pipeline starts by extracting data from CSV, JSON, and XML files located in the source_unzipped folder. Three separate functions handle the extraction process for each file type. The extracted data is then combined into a single DataFrame.

2. Transformation
The extracted data undergoes a transformation phase, where the following conversions take place:

Height from inches to meters.
Weight from pounds to kilograms.
This ensures the data is in a standardized format for analysis or storage.

3. Loading
After transformation, the processed data is written into a CSV file named transformed_data.csv. This file can then be loaded into a database or used for further analysis.

4. Logging
Each phase (Extraction, Transformation, Loading) is logged with timestamps to monitor the progress and ensure smooth execution. Logs are saved to a log_file.txt file.

#How to Run the Project
Prerequisites
Python: Ensure Python is installed. Download Python
Required Libraries:

Install the required libraries using the following command:
bash
Copy code
pip install pandas

Steps to Execute
Unzip the source files:

Unzip the provided source files into the source_unzipped directory.
Run the ETL Script:

Navigate to the directory containing the ETL script and run the script as follows:
bash
Copy code
python ETL.py
The script will extract, transform, and load the data, saving the final output in transformed_data.csv.
Check Logs:
To verify the process, check the log_file.txt to see the logged information about each phase.

Project Workflow
Extraction Phase: Data is extracted from multiple file formats (CSV, JSON, XML).
Transformation Phase: Data is transformed by standardizing units.
Loading Phase: Transformed data is saved into a CSV file.
Logging: All steps are logged for auditing and debugging.

