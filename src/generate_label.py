import csv
import json
import os
import matplotlib.pyplot
from PIL import Image
import random 
from os import path
import sys
import numpy as np
from skimage.draw import * 
from matplotlib import cm

def create_mask_from_annotation(image,image_data ,filename, label_path,image_path):
    '''
    Method for creating binary images and relativate blended images (label and original images overlapped) for debuggin purpose

    parameters:
    - image: numpy array 
        the original image the mask was extracted from  
    - image_data: json
        the json containing the annotations for image

    - filename: string
        the name of the image (unique name to identify the image and its annotation in the json file)
    
    - label_path: string
        the path where to store binary masks

    - image_path: string
        the path the original images are read from
    '''
    or_img=np.asarray(image)
    width = or_img.shape[1]
    height = or_img.shape[0]
    img = np.zeros((height, width), dtype=np.uint8)

    #for each region labeled in the image 
    for region in range(len(image_data["regions"])):
        #pick only patch regions
        if( image_data["regions"][str(region)]['region_attributes']['label'] == '1'):      
            x = image_data["regions"][str(region)]["shape_attributes"]['all_points_x']
            y = image_data["regions"][str(region)]["shape_attributes"]['all_points_y']
   
            rr, cc = polygon(y, x) 
            problem = False
            for r in rr:
                if(r >=  width): 
                    print("problem", filename)
                    problem = True
                    break
            for c in cc:
                if(c >=  height): 
                    print("problem", filename)
                    problem = True
                    break
            if(problem is not True):
                img[rr,cc] = 255


    im = Image.fromarray(np.uint8(cm.gist_earth(img)*255))
    im.save(label_path +'/' + filename, "PNG")

    #blend image with labels generation
    #original_img = Image.open(image_path + "/" + filename).convert("RGB")
    #label_img = Image.open(path + "/" + filename).convert("RGB")
    #i = Image.blend(label_img, original_img, 0.6)
    #i.save(path + "/" + filename, "PNG")

    return img


image_path = './'
label_path = './labels'


#check wheter directory already exists
if( os.path.isdir(label_path) is not True): 
    os.mkdir(label_path)  

with open('my_labels.json') as json_file:
    data = json.load(json_file)
    for filename in data:
        #open image
        if (path.isfile(image_path + '/' + filename) is True ):
            img = Image.open( image_path + '/' + filename) 
            #get coordinates and generate labeled image
            create_mask_from_annotation(img, data[filename], filename, label_path,image_path)
