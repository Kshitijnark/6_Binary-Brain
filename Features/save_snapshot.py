# Python program to convert
# numpy array to image
  
# import required libraries
from pickletools import optimize
import numpy as np
from PIL import Image as im
import datetime
import cv2
import os
  
# define a main function
def SaveImageFromArray(array , directory):
    array = cv2.cvtColor(array,cv2.COLOR_BGR2RGB)
    data = im.fromarray(array)
    if os.path.exists(directory) == False:
        os.mkdir(directory)
    # saving the final output 
    # as a PNG file
    img_path = f'{directory}\{datetime.datetime.now().strftime("%H.%M.%S")}_{datetime.date.today()}.png'
    data.save(img_path, optimize=True, quality =10)
    return img_path
