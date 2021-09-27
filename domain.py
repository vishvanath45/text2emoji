import json
import random
import string

file = open('merged_source.json')

data = json.load(file)

def emojify(text):
    words = text.split()
    emojified_text = ""

    for word in words:
        lc_word = word.lower()
        emoji_list = data.get(lc_word)
        if(emoji_list == None ):
            emojified_text += word + " "
        else:
            emojified_text += word + random.choice(emoji_list) + random.choice(emoji_list)*(random.choices([0,1], weights=[3, 2])[0]) + " "
    return emojified_text