import pyautogui
pyautogui.FAILSAFE = True # 啟用失效安全防護

import numpy as np
import cv2

import time

import keyboard  # using module keyboard

from PIL import Image, ImageEnhance
from operator import itemgetter, attrgetter

while(1):

    img = pyautogui.screenshot( 'foo.png', region = [750, 450, 450, 500])


    image = cv2.imread('foo.png')  # 加載圖片


    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



    #使用Canny方法尋找圓形輪廓
    circles= cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,10,param1=150,param2= 50,minRadius=5,maxRadius=200)



    #輸出返回值，方便查看類型//左上到右下

    #circles2 =sorted(circles[0], key = itemgetter(1, 2) )


    #print(circles[0])

    #輸出檢測到圓的個數
    print(len(circles[0]))

    print("-------------我是條分割線-----------------")
    list1 = []

    for circle  in circles[0]:

        
        x=int(circle[0])
        y=int(circle[1])


        #cv2.circle(image, (x, y), 2, (0, 255, 0), 0)

        list1.append( gray[y][x] )
        

    i = 0
    x1 = 0
    y1 = 0

    for li  in list1:
        if( list1.count(li) == 1 ):
            #cv2.circle(image, ( int(circles[0][i][0]), int(circles[0][i][1])), 10, (0, 0, 0), 2)
            print(i, "y")

            x1 = int(circles[0][i][0])
            y1 = int(circles[0][i][1])
            
        i = i +1

    #cv2.imshow('image', image)

    pyautogui.moveTo(x1 + 750, y1 + 450)    #立即到
    pyautogui.click()

    time.sleep(0.5)


