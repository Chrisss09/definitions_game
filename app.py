import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        return "Did you mean %s instead?" % get_close_matches(word, data.keys())[0]
    else:
        return "Sorry this word does not exist, please try again."

word = input("Enter Word: ")

print(translate(word.lower()))