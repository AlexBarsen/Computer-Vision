import json
import os
import glob
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd


IMAGE_PATHS = ['./COVID-19 Radiography Database/COVID-19/*.png',
               './COVID-19 Radiography Database/NORMAL/*.png',
               './COVID-19 Radiography Database/Viral Pneumonia/*.png']
json_file_paths = ['similar-covid-images.json','similar-normal-images.json','similar-pneumonia-images.json']
N = len(IMAGE_PATHS)

before = np.zeros(N)
after = np.zeros(N)

for i,file_path in enumerate(IMAGE_PATHS):
    before[i] = len(glob.glob(file_path))


for i,json_file_path in enumerate(json_file_paths):
    duplicates = set()
    with open(json_file_path) as f:
        similarities = json.load(f) 
        for k,v in similarities.items():
            for duplicate in v:
                duplicates.add(duplicate)
    after[i] = before[i] - len(duplicates)

print(before)
print(after) 
ind = np.arange(0,len(IMAGE_PATHS))
p1 = plt.bar(ind,after)
p2 = plt.bar(ind,before-after,bottom=after)


plt.xticks(ticks=ind,labels=['COVID','NORMAL','PNEUMONIA'])
plt.legend((p1[0],p2[0]),('Unique','Duplicates'),loc='upper right')
plt.show()