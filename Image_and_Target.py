import numpy as np 
import cv2
from os import listdir
from os.path import isfile, join
from numpy import asarray
from numpy import save
import cv2

myPath = '/home/hariharan/Desktop/Spider/FYP/Dataset/Positive_Slope/Positive_Slope_Depth_Dataset/' # Sample - Path to positive slope color images

onlyfiles = [f for f in listdir(myPath) if isfile(join(myPath, f))] # List of file names present in myPath 

images = [] # Empty list for Images
target = [] # Empty list for Target Values
names=[]# Empty list for names

folder_size = len(onlyfiles) # Number of Images in the folder specified by myPath variable
print(folder_size)


for i in onlyfiles:

	img = cv2.imread(myPath + i)
	target_value_string = i.split('_')[4].split('.')[0]  # Isolate the target value as string
	img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	img=cv2.resize(img,(200,200))
	#print (img.shape)

	images.append(img) # Append the 2D image array
	target.append(float(target_value_string)) # Append the target value as float
	names.append(i)


#print(len(images)) # Total Number of Images 
#print(len(target)) # Total Number of Target Values


#print(images) # Image List
#print(target) # Target Value List

images_array = asarray(images) # Convert Images List to Array
target_array = asarray(target) # Convert Target List to Array
names_array=asarray(names)
print(names_array[100])
#cv2.imshow('image_3',images_array[3])
cv2.imshow('image_100',images_array[100])
print(target_array[100])
cv2.waitKey(0)
cv2.destroyAllWindows()
#print(images_array) # Image Array
#print(target_array) # Target Array


#save('images_depth_positive.npy', images_array)
#save('target_depth_positive.npy', target_array)

