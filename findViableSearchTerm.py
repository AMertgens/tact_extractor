import json
from collections import defaultdict

# Function to clean and tokenize the text
def tokenize(text):
    # Convert to lowercase, remove punctuation, and split into words
    words = text.lower().replace('.', '').replace(',', '').split()
    return {word for word in words if len(word) >= 6}  # Return a set of words with length >= 5

# Function to find the top N words that occur in the most unique snippets, with an upper limit on total occurrences
def top_words_with_limit(json_file, occurrence_limit=4000, top_n=10):
    # Dictionaries to track word snippet count and total occurrence
    word_snippet_count = defaultdict(int)
    word_total_count = defaultdict(int)

    # Open and load the JSON file
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    emptytexts = 0
    # Iterate over all the text snippets
    for key, value in data.items():
        text = value[0]  # Extract the text part from each entry
        second_list = value[1]  # Extract the second list element
        
        # Process the snippet only if the second list element is empty
        if not second_list:
            emptytexts += 1
            words_in_text = tokenize(text)  # Tokenize and get unique words with length >= 5

            # Update word counts for the current snippet
            for word in words_in_text:
                word_snippet_count[word] += 1  # Increment unique snippet count
            # Update total word occurrence count for the text (not unique to snippet)
            for word in text.lower().replace('.', '').replace(',', '').split():
                if len(word) >= 5:  # Only count words with length >= 5
                    word_total_count[word] += 1

    # Filter out words that exceed the occurrence limit
    eligible_words = {word: count for word, count in word_snippet_count.items() if word_total_count[word] < occurrence_limit}

    # Sort the eligible words by their snippet count in descending order and return the top N
    top_words = sorted(eligible_words.items(), key=lambda x: x[1], reverse=True)[:top_n]
    print(f"Number of texts with empty second list: {emptytexts}")
    return top_words  # Return a list of tuples (word, snippet_count)

# Example usage
json_file = 'prolog.json'  # Replace with the actual path to your JSON file
top_words = top_words_with_limit(json_file, occurrence_limit=5000, top_n=10)

print("Top 10 words (min length 5) that occur in the most snippets (with an empty second list) but fewer than 4000 times:")
for word, count in top_words:
    print(f'{word}: {count} unique snippets')
