# Importing the required modules
from PIL import Image
from numpy import asarray 
import numpy as np
#loading the image 
original = Image.open('image50.jpeg')
# using the asarray() function
# converting PIL images into NumPy arrays
numpydataarr = asarray(original) 
# printing the type of the image after conversion
print("The type after conversion is:",type(numpydataarr))
# displaying the shape of the image
print("dimensions of the array", numpydataarr.shape)
#Printing the pixel information
print("The pixel information is=")
np.set_printoptions(threshold=np.inf)
array = np.array(numpydataarr)
list_tuples = [tuple(map(int, row)) for row in array.reshape(-1, array.shape[-1])]
print(list_tuples)
with open("output.txt", "w") as f:
    print(list_tuples, file=f)