import json

compiled = open("../imgs/compiled_galaxies_imgs.json", "w")
compiled_json = []

for i in range(0, 142):
		img_file = open("../imgs/galaxies/object_" + str(i) + "_img.json")
		img_json = json.load(img_file)
		img_dict = {"pid":i+1, "url":str(img_json["url"])}
		compiled_json.append(img_dict)

json.dump(compiled_json, compiled)
compiled.close()