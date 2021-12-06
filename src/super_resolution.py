import cv2
from cv2 import dnn_superres
import os

src_path = './to_upsample'
dst_path = './upsampled'

# Create an SR object
sr = dnn_superres.DnnSuperResImpl_create()
model_path = "./models/EDSR_x4.pb"
# Read the desired model
sr.readModel(model_path)
# Set the desired model and scale to get correct pre- and post-processing
sr.setModel("edsr", 3)
for root, dirs, files in os.walk(src_path):
    for filename in files:
        if( os.path.isfile(dst_path + '/' + root.split('\\')[1] + '/' +  filename) is False):
            print('processing..')
            name = os.path.join(root,filename)
            print(filename)
            image = cv2.imread(name)
            # # Upscale the image
            result = sr.upsample(image)
            # # Save the image
            print('done', dst_path + '/' + root.split('\\')[1] + '/' +  filename)
            cv2.imwrite(dst_path + '/' + root.split('\\')[1] + '/' +  filename, result)