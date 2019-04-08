import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? If yes please type Y or if not please type N: " % get_close_matches(word, data.keys())[0])
        if yn == "Y": 
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "Sorry this does not match, Please check it."
        else:
            return "Sorry I don't understand."
    else:
        return "Sorry this word does not exist, please try again."

word = input("Enter Word: ")

print(translate(word.lower()))