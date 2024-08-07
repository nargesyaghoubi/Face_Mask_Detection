from tensorflow.keras.utils import to_categorical
from keras.utils import to_categorical
import cv2,os
import numpy as np

data_path='datasets'
categories=os.listdir(data_path)
labels=[i for i in range(len(categories))]

label_dict=dict(zip(categories,labels)) #empty dictionary

print(label_dict)
print(categories)
print(labels)

img_size = 100
data = []
target = []