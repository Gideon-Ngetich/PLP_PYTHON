import json
from difflib import get_close_matches

with open('week 4 mini project/data.json', 'r') as file:
    data_dict = json.load(file)

def word_definition(word):
    if word in data_dict:
        return data_dict[word]
    else:
        suggestions = get_close_matches(word, data_dict.keys(), n=1, cutoff=0.8)
        if suggestions:
            suggestion = suggestions[0]
            response = input(f"Did you mean '{suggestion}' instead (y/n): ")
            if response.lower() == 'y':
               return data_dict[suggestion]
            else:
                return 'Word not found. Please try again'
        else:
            return 'Word not found. Please try again'

word = input('Enter a word to get it\'s definition: ')
definition = word_definition(word)
print(definition)