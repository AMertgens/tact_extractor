import json
import csv

# Load the JSON file
with open('data_result.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Open the CSV file for writing
with open('output_file.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)

    # Write the header row
    csvwriter.writerow(["Name", "Extra Info", "Text", "Key"])

    # Process each entry in the JSON file
    for key, value in data.items():
        name = ""
        extra_info = ""
        title = ""
        
        if isinstance(value, list):
            title = value[0]  # The text (e.g., "Constantinus Episcopus")
            
            if len(value) > 1 and isinstance(value[1], list):
                # Extract name and extra info if they exist
                sublist = value[1]
                if len(sublist) > 0:
                    name = sublist[0]  # First element of the sublist
                if len(sublist) > 1:
                    extra_info = sublist[1]  # Second element of the sublist

        # Write a row to the CSV
        csvwriter.writerow([name, extra_info, title, key])

print("CSV file created successfully.")
