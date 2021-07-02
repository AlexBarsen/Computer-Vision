from PIL import Image
import imagehash
import os
from tqdm import tqdm
import json


"""
This will create a .json file for all images that are similar.
The folder that contains the images are stored in directory. 
The output paths are stored in json_paths.

Lets say image1, image5 and image6 are similar, this will create an output as follows:
{image1: [image5,image6]}


"""

directory = ['COVID-19 Radiography Database\\NORMAL\\',
            'COVID-19 Radiography Database\\Viral Pneumonia\\']
json_paths = ['similar-normal-images.json',
        'similar-pneumonia-images.json']

for k in range(len(directory)):
    images = []
    similar_images = {} 
    for filename in os.listdir(directory[k]):
        if  filename.endswith(".png"): 
            images.append(os.path.join(directory[k], filename))
    for i in tqdm(range(len(images)),position=0, leave=True):
        for j in tqdm(range(i+1,len(images)),position=0, leave=True):
            hash1 = imagehash.average_hash(Image.open(images[i]))
            hash2 = imagehash.average_hash(Image.open(images[j]))
            if (hash1 - hash2) < 1.0:
                similar_images.setdefault(images[i],[]).append(images[j])

    with open(json_paths[k], 'w') as file:
        json.dump(similar_images, file)