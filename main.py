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
foldercount=5
while count<int(quantity):
    print("test")
    storeImages=list()
    #iterate through "Layers" dir
    for files in os.scandir(imagepathLoad["imagePaths"]["files"]):
        strFiles=str(files).replace("<DirEntry","").replace("'","").replace(">","").strip()
        print(strFiles)

        random_image=random.choice([
            image for image in os.listdir(imagepathLoad["imagePaths"]["files"]+"\\"+strFiles)
            if os.path.isfile(os.path.join(imagepathLoad["imagePaths"]["files"]+"\\"+strFiles)) and image.endswith(".jpg")
            or image.endswith(".png")
        ])

        #random img
        im=Image.open(imagepathLoad["imagePaths"]["files"]+strFiles+"\\"+random_image)
        nft_image=Image.new("RGBA",(32,32),(0,0,0,0))
        nft_image.save(imagepathLoad["imagePaths"]["nfts"]+"\\"+"image.png","PNG")
        #nft_image.show()

    count+=1
count=0

print(foldercount,count)
#end



