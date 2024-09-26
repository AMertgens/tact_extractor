import re

def parse_line(line):
    # Split the line at the first comma to get the name and the rest of the line
    parts = line.split(",", 1)
    
    if len(parts) < 2:
        return None  # Skip invalid lines
    
    name = parts[0].strip()  # Everything before the first comma is the name
    rest = parts[1].strip()  # Everything after the first comma
    
    # Handle the case where the name is "--"
    if name == '- -':
        name = '--'
    
    # Find the position of the colon, which separates the ID from the reference
    colon_index = rest.find(":")
    
    if colon_index == -1:
        return None  # Skip invalid lines without a colon
    
    id_field = rest[:colon_index + 1].strip()  # Everything up to and including the colon is the ID
    rest_after_id = rest[colon_index + 1:].strip()  # Everything after the colon
    
    # Split the rest into reference and text parts
    rest_parts = rest_after_id.split(" ", 1)

    if len(rest_parts) < 2:
        return None  # Skip invalid lines
    
    reference_field = rest_parts[0].strip()  # The first part after the colon is the reference

    # Check if the reference ends with "ff" or single letter (e.g., "a", "b") and handle it
    if reference_field.endswith(('ff', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')):
        # Reference is correct, no further change needed
        text_field = rest_parts[1].strip()
    else:
        # If there's an additional suffix, treat it as part of the reference
        next_word = rest_parts[1].split(" ", 1)[0].strip()
        reference_field += " " + next_word
        text_field = rest_parts[1][len(next_word):].strip()
    
    # Strip non-alphabetic characters from the text field and convert to lowercase
    text_field = re.sub(r'[^a-zA-Z\s]', '', text_field).lower()
    
    return [name, id_field, reference_field, text_field]

def process_file(filename):
    parsed_lines = []
    
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # Parse each line
            parsed_line = parse_line(line.strip())
            if parsed_line:
                parsed_lines.append(parsed_line)
    
    return parsed_lines

def save_to_csv(data, output_file):
    import csv
    
    # Save the parsed data to a CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'ID', 'Reference', 'Text'])  # Write header
        writer.writerows(data)

# Main logic to process the file and save the output
input_file = 'Lists/SICUT.TXT'  # Path to your input text file
output_file = 'outputsicut.csv'  # Path to save the output CSV

parsed_data = process_file(input_file)
save_to_csv(parsed_data, output_file)

print(f"Processing completed. Output saved to {output_file}")
