# -*- coding: utf-8 -*-
"""
Created on Tue May 25 17:05:17 2021

@author: heaven
"""
import cv2


class image_edit:
    def __init__(self, path, width, high):
        self.path = path
        self.width = width
        self.high = high
        self.image = cv2.imread(self.path)
        
    def size_fit(self, image): # 오류남 비율 확대로 생각해보자 가로세로 사이즈 지정 말고 
        h, w, _ = image.shape
        ra_h, ra_w, ra_im = h/self.high, w/self.width, h/w
        # small size image case
        if ra_h > ra_w:
            resize_h = self.high
            resize_w = int(self.high*w / h)
        elif ra_h < ra_w:
            resize_w = self.width
            resize_h = int(self.width*h / w)
        else:
            resize_w = self.high
            resize_h = self.high
        return image.resize(image, (resize_w, resize_h))
            
    
    
    
    def im_load(self):
        img = self.image
        img = self.size_fit(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, c = img.shape
        return img.data, h, w, c




'''
# test
img = cv2.imread('ic.png')
#img = cv2.resize(img, (1100, 900))
high, width = 900, 1100
h, w, _ = img.shape
ra_h, ra_w, ra_im = h/high, w/width, h/w
# small size image case
if ra_h > ra_w:
    resize_h = high
    resize_w = int(high*w / h)
elif ra_h < ra_w:
    resize_w = width
    resize_h = int(width*h / w)
else:
    resize_w = high
    resize_h = high
print(resize_w, resize_h)
img.resize(img, (729, 900))

print(img.shape)


cv2.imshow("original", img)
cv2.waitKey()
cv2.destroyAllWindows()

#'''