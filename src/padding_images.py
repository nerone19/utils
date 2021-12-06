import os
from os import walk
import numpy as np
from PIL import Image, ImageOps 
import matplotlib.pyplot
import cv2
cwd = os.getcwd()


for r, d, f in os.walk(cwd):
    
    for file in f:
        print(file)
        if(file.split(".")[1] == "png"):
            print("ciao",r)
            im = Image.open(file)  
            widht, height = im.size
            print(im.size)
            if(widht - height > 0):
                h_pad = int((widht - height)/2)
                w_pad = 0
            elif(height - widht > 0):
                h_pad = 0
                w_pad = int((height - widht)/2)
            else: 
                h_pad = 0
                w_pad = 0
            
            if(h_pad > 0 or w_pad > 0 ):
                or_img = np.pad(im, ((h_pad, h_pad), (w_pad, w_pad), (0,0)), 'constant', constant_values=0)
                cv2.imwrite('./'+file, or_img)
   