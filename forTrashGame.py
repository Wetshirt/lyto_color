import pyautogui

import numpy as np
import cv2

from PIL import Image, ImageEnhance
from operator import itemgetter, attrgetter



#img = pyautogui.screenshot( 'foo.png', region = [750, 450, 450, 500])


image = cv2.imread('foo.png')  # 加載圖片


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



#使用Canny方法尋找圓形輪廓
circles= cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,10,param1=150,param2= 50,minRadius=5,maxRadius=200)



#輸出返回值，方便查看類型//左上到右下

#circles2 =sorted(circles[0], key = itemgetter(1, 2) )



print(circles[0])

#輸出檢測到圓的個數
print(len(circles[0]))

print("-------------我是條分割線-----------------")

for circle  in circles[0]:

    
    x=int(circle[0])
    y=int(circle[1])


    cv2.circle(image, (x, y), 2, (0, 255, 0), 0)
        
 
    
   
    print(gray[x + 20][y])
    


cv2.imshow('image', image)



    

