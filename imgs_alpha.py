#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from PIL import Image
import math
import time
import datetime
import os
import random


def imgCut(img,box):
    
    newW = box[2]-box[0]
    newH = box[3]-box[1]
    tmpImg = img.crop(box)
    return tmpImg

def file_extension(path):
    ext = ''
    pos = path.rfind('.')
    if(pos!=-1):
        ext = path[pos+1:]
    return ext

def resizeImg(img,width,newPath=None,isSque=False):
    mSize = img.size
    filname = img.filename
    if(mSize[0]):
       
        if isSque:
            if mSize[0]>mSize[1]:#宽大于高
                newH = width
                newW = int(mSize[0]*width/mSize[1])
                img = img.resize((newW,newH))
                x0 = int((newW-width)/2)
                y0 = 0
                x1 = x0+width
                y1 = width
                
            else:
                newW = width
                newH = int(mSize[1]*width/mSize[0])
                img = img.resize((newW,newH))
                y0 = int((newH-width)/2)
                x0 = 0
                y1 = y0+width
                x1 = width
                
            img = img.crop((x0,y0,x1,y1))
        else:
            newW = width
            newH = int(mSize[1]*width/mSize[0])
            img = img.resize((newW,newH))
    
       
        if newPath==None:
            path = filname
        else:
            path = newPath
        #res = img.save(path)
    return img


def staticAvRgb(img):
    size = img.size
    x,y = size
    if y==0:
        y=1
    if x==0:
        x=1    
    r = 0
    g = 0
    b = 0
    for tx in range(x):
        for ty in range(y):
            rgb = img.getpixel((tx,ty))
            r += rgb[0]
            g += rgb[1]
            b += rgb[2]

    r = int(r/(x*y))
    g = int(g/(x*y))
    b = int(b/(x*y))
    return (r,g,b)

def getMinRgbSqrt(list1,var):
    vS = 10000000
    index = 0
   
    for x in range(len(list1)):
    
    
        tv = math.sqrt((var[0] - list1[x][0])**2 + (var[1] - list1[x][1])**2 + (var[2] - list1[x][2])**2)
       
        if  tv<vS :
            vS = tv
            index = x
    return index
            
            
'''        
image = Image.open('img/main.jpg')
simage1 = Image.open('img/s1.jpg')
simage2 = Image.open('img/s2.jpg')
mSize = image.size
simage1 = simage1.resize(((200,200)));
simage2 = simage2.resize(((200,200)));
image = image.convert("RGBA")
simage1 =simage1.convert("RGBA")
simage2 =simage2.convert("RGBA")

newimg = Image.new('RGBA', mSize,(255,255,255) )

image.putalpha(60)

print(mSize)
print(newimg.size)
newimg.paste(simage1,(0,0,200,200))
newimg.putalpha(50)

image.alpha_composite(newimg)
image.show()

#image.putalpha((x,y), alpha)


exit();        
'''



mainImagPath = "m6.jpg"
subImagePath = "img/"
subIw = 100
mainIw = 3000
subImgArr = {}
subImgRgbArr = {}
files= os.listdir(subImagePath)
subImgCount = 0
for imgPath  in files:
    ext = file_extension(imgPath)
    ext = ext.lower()
    if(ext!='jpg'and ext!='jpeg' and ext!='png'):
        continue
    i = subImgCount
    subImgArr[i] = Image.open(subImagePath+'/'+imgPath)
    subImgArr[i] = resizeImg(subImgArr[i],subIw,None,True)
    subImgRgbArr[i] =  subImgArr[i].convert("RGBA")
    subImgCount += 1

#img.putpixel((1,4),(0,0,0))
#img.getpixel((1,4))

mainImg = Image.open(mainImagPath)
mainImg = resizeImg(mainImg,mainIw)
mSize = mainImg.size
if(mSize[1]%subIw!=0):
    #裁剪
    mainImg = imgCut(mainImg,(0,0,mSize[0],mSize[1]-mSize[1]%subIw))

mainImg = mainImg.convert("RGBA")
mSize = mainImg.size

mxLen = int(mSize[0]/subIw)
myLen = int(mSize[1]/subIw)

newimg = Image.new('RGBA', mSize,(255,255,255) )

#循环新图
for my in range(myLen):
    for mx in range(mxLen):
        #print("正在计算 第 "+str(mx+1)+" 行 第"+str(my+1)+"列\n")
        x0 = mx*subIw
        y0 = my*subIw
        x1 = (mx+1)*subIw
        y1 = (my+1)*subIw
        box = (x0,y0,x1,y1)
        #index  = (my*myLen+mx)%subImgCount
        index = random.randint(0,subImgCount-1)
        newimg.paste(subImgArr[index],box)


newimg.putalpha(50)
mainImg.putalpha(200)
mainImg.alpha_composite(newimg)
bg = Image.new("RGB", mainImg.size, (255,255,255))
bg.paste(mainImg,mainImg)

bg.show()  
#now_time = datetime.datetime.now()
#mainImg.save('img/t/'+now_time.strftime('%Y%m%d%-H%M%S')+'.jpg');


