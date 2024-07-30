import re
import csv

def clean_quotation(quote):
    # Remove " |" and " > " characters and normalize whitespace
    quote = re.sub(r'\s*\|\s*|\s*>\s*', ' ', quote)
    quote = re.sub(r'\s+', ' ', quote)
    return quote.strip()

def split_identifier(identifier):
    # Split the identifier into "J Number" and "Location" at the colon ":"
    parts = identifier.split(':', 1)
    if len(parts) == 2:
        return parts[0].strip(), parts[1].strip()
    else:
        return identifier.strip(), ''

# Read the content of the file
input_file = 'NOSTRI1.txt'
output_file = 'nostri-parsed_data.csv'

with open(input_file, 'r') as file:
    content = file.readlines()

# Regular expression pattern to match the required data
pattern = re.compile(r'(?P<name>[A-Za-z\s-]+),\s*(?P<id>[\w\s.,:]*\d)\s{2,}(?P<quote>.+)')

# Prepare a list to hold the parsed data
data = []

# Parse each line using the regular expression
for line in content:
    match = pattern.search(line)
    if match:
        name = match.group('name').strip()
        identifier = match.group('id').strip()
        j_number, location = split_identifier(identifier)
        quote = clean_quotation(match.group('quote').strip())
        data.append([name, j_number, location, quote])
    else:
        # If the line doesn't match the pattern, consider it part of the previous quote
        if data and line.strip():
            data[-1][3] += ' ' + line.strip()
            data[-1][3] = clean_quotation(data[-1][3])

# Write the parsed data to a CSV file
with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write the header
    csvwriter.writerow(['Name', 'J Number', 'Location', 'Quotation'])
    # Write the data rows
    csvwriter.writerows(data)

print(f"Data parsing complete. The output is saved in '{output_file}'.")
