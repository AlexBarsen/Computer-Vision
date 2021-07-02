# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 18:14:44 2020

@author: david
"""
import pandas as pd
import matplotlib.pyplot as plt
import os
import pickle

"""
Used to visualize the history of a model
"""

#Change this to the correct file that you want to visualize
HDF_FILE =os.path.join('server/history', 'efficientNetB7.h5') 

def main():
    with open(HDF_FILE, 'rb') as f:
        df = pickle.load(f)

        print(max(df['val_accuracy']))
        #print(df['val_accuracy'].index(0.96875))
        #plt.xlabel("Number of epochs")
        #plt.ylabel("Accuracy")
        #plt.plot(df["accuracy"], label="training accuracy")
        #plt.plot(df["val_accuracy"], label="validation accuracy")
        #plt.axis([0, 100, 0, 1.0])
        #plt.title('With data augmentation and dropout')
        #plt.legend()
        #plt.savefig('efficientNetB7_accuracy_3.png')
        #plt.show()
   

if __name__ == '__main__':
    main()