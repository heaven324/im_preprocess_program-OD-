# -*- coding: utf-8 -*-
"""
Created on Tue May 25 17:05:17 2021

@author: heaven
"""
import cv2


class image_edit:
    def __init__(self, path):
        self.path = path
        self.original_image = cv2.imread(self.path)
        self.fix_image = cv2. imread(self.path)
        
    def im_load(self):
        img = self.fix_image
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, c = img.shape
        return img.data, h, w, c




'''
# test
img = cv2.imread('ic.png')
img = cv2.resize(img, (1100, 900))



cv2.imshow("original", img)
cv2.waitKey()
cv2.destroyAllWindows()

#'''