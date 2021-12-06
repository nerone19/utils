from PIL import Image  
import os
from os import walk
import matplotlib.pyplot
cwd = os.getcwd()

ind = 0
base = 'Image-'

for file in sorted(os.listdir(cwd)):
    if (os.path.isdir(file) == False):
        if(file.split(".")[1] == "png" or file.split(".")[1] == "jpg"):
            print(file)
            new_name = 'Image-' + str(ind)
            os.rename(file, new_name + ".png")
            ind = ind + 1

