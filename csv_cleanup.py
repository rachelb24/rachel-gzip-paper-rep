import csv
import re

# Input and output file paths
input_file = 'train_data.csv'
output_file = 'train_output.csv'

# Define a function to clean a string
def clean_string(input_str):
    # Remove newline characters and tabs
    cleaned_str = re.sub(r'\n|\t', ' ', input_str)
    # Remove multiple spaces
    cleaned_str = re.sub(r'\s+', ' ', cleaned_str)
    return cleaned_str.strip()

# Open the input and output CSV files with the specified encoding
with open(input_file, 'r', newline='', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    # Create CSV reader and writer objects
    csv_reader = csv.reader(infile)
    csv_writer = csv.writer(outfile)

    # Iterate through each row in the input CSV file
    for row in csv_reader:
        # Clean each cell in the row
        cleaned_row = [clean_string(cell) for cell in row]
        # Write the cleaned row to the output CSV file
        csv_writer.writerow(cleaned_row)

print(f"Data cleaned and saved to {output_file}")

