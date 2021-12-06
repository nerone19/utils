import sys
from os import listdir
from os.path import isfile, join
from os import walk,path,mkdir
from PIL import Image

assert(sys.argv[1] is not None), "please add the path for the original images"
assert(sys.argv[2] is not None), "please add the path for the labeled images"
assert(sys.argv[3] is not None), "please add the desired path for puttinh the blended images"
original_images_path = sys.argv[1]
labeled_images_path = sys.argv[2]
blended_images_path = sys.argv[3]

print( sys.argv[1])
print(original_images_path)
if( path.exists(blended_images_path) is not True): #check wheter directory already existing
    mkdir(blended_images_path)  #create blended folder

for (dirpath, dirnames, filenames) in walk(original_images_path):
    print(sys.argv[1])
    for filename in filenames:
        print("e")
        if(filename.split(".")[1] == "png"):
            original_img = Image.open(original_images_path + "/" + filename).convert("RGB")

            if(path.exists(labeled_images_path + filename)):
                labeled_image = Image.open(labeled_images_path + "/" + filename).convert("RGB")
            
                i = Image.blend(original_img, labeled_image, 0.6)
                i.save(blended_images_path + "/" + filename, "PNG")
