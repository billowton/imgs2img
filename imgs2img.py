#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from PIL import Image
import math
import time
import datetime

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
    size = img.size;
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
            
            
        
print('success');
exit();        




mainImagPath = "wtt/m.jpg"
subImagePath = "img4/"
subimgCount = 26
subIw = 50
mainIw = 3000
subImgArr = {}
subImgRgbArr = {}
for x in range(subimgCount):
    subImgArr[x] = Image.open(subImagePath+str(x+1)+".jpeg")
    subImgArr[x] = resizeImg(subImgArr[x],subIw,None,True)
    subImgRgbArr[x] = staticAvRgb(subImgArr[x])

#img.putpixel((1,4),(0,0,0))
#img.getpixel((1,4))


mainImg=Image.open(mainImagPath)
mainImg = resizeImg(mainImg,mainIw)
mSize = mainImg.size
#循环主图
mxLen = int(mSize[0]/subIw)
myLen = int(mSize[1]/subIw)


for my in range(myLen):
    for mx in range(mxLen):
        #print("正在计算 第 "+str(mx+1)+" 行 第"+str(my+1)+"列\n")
        x0 = mx*subIw
        y0 = my*subIw
        x1 = (mx+1)*subIw
        y1 = (my+1)*subIw
        box = (x0,y0,x1,y1)
        tmpImg = mainImg.crop(box)
        tmpRgb = staticAvRgb(tmpImg)
        tIndex = getMinRgbSqrt(subImgRgbArr,tmpRgb)
    
        mainImg.paste(subImgArr[tIndex],box)
       
mainImg.show()  
now_time = datetime.datetime.now()
mainImg.save('img/t/'+now_time.strftime('%Y%m%d%-H%M%S')+'.jpg');


