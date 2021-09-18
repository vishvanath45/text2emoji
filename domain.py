import json
import random
import string

file = open('source1.json')

data = json.load(file)

def emojify(text):
    words = text.split()
    emojified_text = ""

    for word in words:
        # word = word.lower()
        emoji_list = data.get(word)
        if(emoji_list == None ):
            emojified_text += word + " "
        else:
            emojified_text += word + random.choice(emoji_list) + " "
    return emojified_text