import json
import time
from difflib import get_close_matches

data = json.load(open("data.json"))
def dictonary(word):
    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word.title()]

    elif word.lower() in data:
        return data[word.lower()]

    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("did you mean %s insted" %get_close_matches(word, data.keys())[0])
        decide = input("press y for YES an n for NO")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]

        elif decide == "n":
            return("word not found in dicitionary check your spelling")    
        else:
            return("you have enter the something else plz enter y or n")

    

    else:
        print("word not found in dictonary check again with right spelling") 




word=input("enter the word you want to search")
time.sleep(1.5)
output= dictonary(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)            
