import json
import os
json_file_path = 'similar-covid-images.json'

new_similarities = {}
with open(json_file_path) as f:
        similarities = json.load(f)
        for key,value in similarities.items():
            new_similarities[os.path.split(key)[1]] = [os.path.split(pathname)[1] for pathname in similarities[key]]

print(new_similarities)