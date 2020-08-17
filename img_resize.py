#!/usr/bin/env python3


from PIL import Image

import glob

images = []

imagesList = {}
imagesList = glob.glob('*.jpeg')

counter=0
for item in imagesList:
    img = Image.open(item)
    newsize = (224, 224)
    img = img.resize(newsize)
    images.append(img)
    img = img.save("image_"+str(counter) +".jpeg")
    counter+=1
   

        
        

        


