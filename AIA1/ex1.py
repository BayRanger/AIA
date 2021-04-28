#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Simon Matern
"""

# %%
import numpy as np
import cv2
import utils
# %%

def binarizeImage(img, thresh):
    """
    Given a coloured image and a threshold binarizes the image.
    Values below thresh are set to 0. All other values are set to 255
    """
    # TODO
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    max_val = 255
    img_bin = (img_gray > thresh) * max_val
    return img_bin

# %%

 
def smoothImage(img):    
    """
    Given a coloured image apply a blur on the image, e.g. Gaussian blur
    """
    # TODO
    img = cv2.blur(img, (5,5))
    img =  cv2.GaussianBlur(img,(5,5),0)
    return img
# %%
def doSomething(img):
    """
    Given a coloured image apply any image manipulation. Be creative!
    """
    # TODO
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    mask = (img_grey < 87)  
    img_grey[mask]= 255
    img[:,:,0] = img_grey
    img[:,:,1] = img_grey
    img[:,:,2] = img_grey
 
    
    return img

# %%
def processImage(img):
    """
    Given an coloured image applies the implemented smoothing and binarization.
    """
    # TODO
    img = smoothImage(img)
    img = binarizeImage(img, 125)
    return img

# %%
if __name__=="__main__":
    img = cv2.imread("test.jpg")
    utils.show(img)
# %%    
    img1 = smoothImage(img)
    utils.show(img1)
    cv2.imwrite("result1.jpg", img1)
# %%    
    img2 = binarizeImage(img, 125)
    utils.show(img2)
    cv2.imwrite("result2.jpg", img2)
# %%   
    img3 = processImage(img)
    utils.show(img3)
    cv2.imwrite("result3.jpg", img3)
# %%    
    img4 = doSomething(img)
    utils.show(img4)
    cv2.imwrite("result4.jpg", img4)
# %%