from cv2 import *
import numpy as np
import os, copy

# Reads image into an array
img = imread('DIP/einstein.tif', 0)

# Get Dimensions of image (row, col)
dim = img.shape    

# Initialize Everything For Use Below
hist = [0] * 256
cumulative = [0] * 256
equ = copy.copy(img)

# Builds Histogram
for i in range(dim[0]):
    for j in range(dim[1]):
        hist[(img[i][j])] = hist[(img[i][j])] + 1

# Builds Cumulative Histogram
for i in range(1, 255):
    cumulative[i] = cumulative[i-1] + hist[i]

# Normalize Cumulative Histogram
c = (255/(dim[0]*dim[1])) # (L-1)/(M*N)
for i in range(255):
    cumulative[i] = round(c * cumulative[i])

# Transforms Image By Assigning New Grey Value
for i in range(dim[0]):
    for j in range(dim[1]):
        equ[i][j] = cumulative[img[i][j]-1]

# Stacks the input and output images together
result = np.hstack((img, equ))

# Writes the stacked images to a file
imwrite('histequ_result.png', equ)

# Displays the result
imshow('Side By Side', result)
waitKey(0)
destroyAllWindows()
imshow('By Itself', equ)
waitKey(0)
destroyAllWindows()
