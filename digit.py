# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 10:07:17 2019

@author: praja
"""

#libraries
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import datasets
import numpy as np
import cv2     # pip install opencv-python    used for image recognition
import matplotlib.pyplot as plt

digit= datasets.load_digits() #load digits from mnist dataset
#train dataset
(train_x, test_x, train_y, test_y) = train_test_split(np.array(digit.data),digit.target, test_size=0.25,random_state=42)

print("training data points: ",len(train_y))
print("testing data points: ",len(test_y))

k=range(1,30,2)
accuracy=[]
#evaluate model for odd k in range 1-10
for i in range(1,30,2):
      model = KNeighborsClassifier(n_neighbors=i)
      model.fit(train_x, train_y)
      score = model.score(test_x, test_y)
      print("k=%d, accuracy=%.2f%%" % (i, score * 100))
      accuracy.append(score)

val=np.argmax(accuracy)   #find k wit max accuracy
print("The accuracy is max for k = %d i.e  %.2f%% "%(k[val],accuracy[val]*100))

#test model again with k that gives max accuracy
model = KNeighborsClassifier(n_neighbors=k[val])
model.fit(train_x, train_y)
predictions = model.predict(test_x)

print("EVALUATION ON TESTING DATA")
print(classification_report(test_y, predictions))
print ("Confusion matrix")
print(confusion_matrix(test_y,predictions))


for i in np.random.randint(0, high=len(test_y), size=(10,)):
    image=test_x[i]
   # prediction = model.predict([image])[0]
    imgdata = np.array(image, dtype='float')
    pixels = imgdata.reshape((8,8))
    plt.imshow(pixels,cmap='gray')
    plt.show()
    print("image",i)  

j=int(input("Enter number of image to be predicted: "))

image==test_x[j]
prediction = model.predict([image])[0]
imgdata = np.array(image, dtype='float')
pixels = imgdata.reshape((8,8))
plt.imshow(pixels,cmap='gray')
plt.show()
#print("image",i+1)  
print("Prediction for image :",prediction)
cv2.waitKey(0)

