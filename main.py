import json
import random
import os
from PIL import Image

with open('C:\\Users\\kevin\\OneDrive\\Desktop\\nftimagegen\\pathimages.json','r')as imagePaths:
    data=imagePaths.read()
imagepathLoad=json.loads(data)

quantity=input('how many to generate?: ')

count,fileCount,saveCount=0,0,0
canExecute=False
canCount=True
folderCount=0

#configs
height,width=32,32 #image size

nft_image=Image.new("RGBA",(height,width),(0,0,0,0))

rarityList=dict()
attributes=list()
#loop random file

for getFiles in os.scandir(imagepathLoad["imagePaths"]["files"]):
    nameFiles=str(getFiles).replace("<DirEntry","").replace("'","").replace(">","").strip()
    for getImages in os.scandir(imagepathLoad["imagePaths"]["files"]+"\\"+nameFiles):
        nameImages=str(getImages).replace("<DirEntry","").replace("'","").replace(">","").replace(".png","").strip()
        rarityList[nameImages]=0
print(rarityList)

while count<int(quantity):
    storeImages=list()

    #iterate through "Layers" dir 5 folders
    for files in os.scandir(imagepathLoad["imagePaths"]["files"]):
        strFiles=str(files).replace("<DirEntry","").replace("'","").replace(">","").strip()

        if canCount==True:
            folderCount+=1
            #store files in rarityList
            for images in os.listdir(imagepathLoad["imagePaths"]["files"]+"\\"+strFiles):
                rarityList[images]=0

        #pick random image
        random_image=random.choice([
            image for image in os.listdir(imagepathLoad["imagePaths"]["files"]+"\\"+strFiles)
            if os.path.isfile(os.path.join(imagepathLoad["imagePaths"]["files"]+"\\"+strFiles)) and image.endswith(".jpg")
            or image.endswith(".png")
        ])
        #opens random image
        randIm=Image.open(imagepathLoad["imagePaths"]["files"]+strFiles+"\\"+random_image)

        fileCount+=1
        attributes.append(random_image)

        if fileCount==1:
            combine_1=Image.alpha_composite(nft_image,randIm)
        elif fileCount==2:
            combine_2=Image.alpha_composite(combine_1,randIm)
        elif fileCount==3:
            combine_3=Image.alpha_composite(combine_2,randIm)
        elif fileCount==4:
            combine_4=Image.alpha_composite(combine_3,randIm)
        elif fileCount==5:
            combine_5=Image.alpha_composite(combine_4,randIm)
        elif fileCount==folderCount:
            combine_6=Image.alpha_composite(combine_5,randIm)
            saveCount+=1
            combine_6.save(imagepathLoad["imagePaths"]["nfts"]+"\\"+f"image_{saveCount}.png","PNG")
            fileCount=0

    canCount=False
    count+=1
    print(f"no.{count} {attributes}")
    attributes.clear()
count=0

print(folderCount,count)
print(rarityList)
print("Finished!"+f"\nGenerated {quantity} images")
#end



