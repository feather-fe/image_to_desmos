from PIL import Image
from numpy import asarray 
import numpy as np
#loading the image 
original = Image.open('badappleframeuno.jpg')
# using the asarray() function
# converting PIL images into NumPy arrays
array = asarray(original) 
np.set_printoptions(threshold=np.inf)
list_tuples = [tuple(map(int, row)) for row in array.reshape(-1, array.shape[-1])]
print(array)