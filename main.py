import json
import random
import os
from PIL import Image

with open('C:\\Users\\kevin\\OneDrive\\Desktop\\nftimagegen\\pathimages.json','r')as imagePaths:
    data=imagePaths.read()
imagepathLoad=json.loads(data) #loads json file

quantity=input('how many to generate?: ')

#random pick
count=0
filecount=0
while count<int(quantity):
    print("test")
    #iterate through "Layers" dir
    for files in os.scandir(imagepathLoad["imagePaths"]["files"]):
        strFiles=str(files).replace("<DirEntry","").replace("'","").replace(">","").strip()
        print(strFiles)

        random_image=random.choice([
            image for image in os.listdir(imagepathLoad["imagePaths"]["files"]+"\\"+strFiles)
            if os.path.isfile(os.path.join(imagepathLoad["imagePaths"]["files"]+"\\"+strFiles)) and image.endswith(".jpg")
            or image.endswith(".png",33)
        ])
        filecount+=1
    count+=1
count=0

print(filecount,count)
#end



