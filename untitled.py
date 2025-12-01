import json

with open("Settings.json") as data_file:
	settings = json.load(data_file)

	story = settings["Story"]

	del settings["Story"]

	storage_new_Keys = {}

	for i in settings.keys():

		storage_new_Keys[i] = input(settings[i])

	for i in settings.keys():
		story.replace(i, storage_new_Keys[i])

	print(story)