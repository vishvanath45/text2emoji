import json

wordlist = open('1000_most_popular_english_words.txt', 'r')


emoji_data1 = open('source1.json')
emoji_map1 = json.load(emoji_data1)

emoji_data2 = open('source2.json')
emoji_map2 = json.load(emoji_data2)


emoji_data3 = open('merged_source.json')
emoji_map3 = json.load(emoji_data3)


def check_emoji_mapping_quality(emoji_map):
    count = 0
    rank = 0
    for word in wordlist:
        # print(word.strip())
        # print(len(word))
        rank = rank +1
        if(emoji_map.get(word.strip()) == None):
            count = count+1
            print(word.strip() , rank)

    print(count)


def merge_source_and_generate_merged_dict():
#10352
    count = 0
    merged_dict = dict()
    merged_dict = emoji_map1 
    for word in emoji_map2:
        if(merged_dict.get(word) != None):
            list1 = merged_dict.get(word)
            list2 = emoji_map2.get(word)
            merged_dict[word] = list1 + list2
            count = count + 1
        else:
            merged_dict[word] = emoji_map2[word]


    print(merged_dict)   
    # print(len(emoji_map1.keys()))
    # print(len(emoji_map2.keys()))
    # print(len(merged_dict.keys()))
    # print(count)



check_emoji_mapping_quality(emoji_map3)
# merge_source_and_generate_merged_dict()