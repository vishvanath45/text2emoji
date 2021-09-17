import json
import random
import string



def main():
	old_file = open('emoji-mappings.json')
	old_data = json.load(old_file)

	# new_file = open('processed_mapping.json')
	# new_data = json.load(new_file)

	new_dist = dict()
	emojified_text = ""
	for k in old_data:
		value = old_data[k]
		new_dist[k] = list(set(value))


	print(new_dist)

main()
