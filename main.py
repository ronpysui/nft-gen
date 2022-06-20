import json
import random
import os
from PIL import Image

with open('C:\\Users\\kevin\\OneDrive\\Desktop\\nftimagegen\\pathimages.json','r')as imagePaths:
    data=imagePaths.read()
imagepathLoad=json.loads(data) #loads json file

quantity=input('how many to generate?: ')

count=0
foldercount=5
height,width=32,32
nft_image=Image.new("RGBA",(height,width),(0,0,0,0))

#loop random file
while count<int(quantity):
    print("test")
    storeImages=list()

    #iterate through "Layers" dir
    for files in os.scandir(imagepathLoad["imagePaths"]["files"]):
        strFiles=str(files).replace("<DirEntry","").replace("'","").replace(">","").strip()

        #pick random image
        random_image=random.choice([
            image for image in os.listdir(imagepathLoad["imagePaths"]["files"]+"\\"+strFiles)
            if os.path.isfile(os.path.join(imagepathLoad["imagePaths"]["files"]+"\\"+strFiles)) and image.endswith(".jpg")
            or image.endswith(".png")
        ])
    count+=1

    #save img --> dir
    nft_image.save(imagepathLoad["imagePaths"]["nfts"]+"\\"+f"image_{count}.png","PNG")

    #random img
    randIm=Image.open(imagepathLoad["imagePaths"]["files"]+strFiles+"\\"+random_image)


count=0

print(foldercount,count)
#end



