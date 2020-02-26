from cv2 import *
import numpy as np
import os, copy

# Name: Clark Walcott
# StudentID: 14271159
# Date: 9/17/2019

def hist_eq(img):
    print("Starting Histogram Equalizaton...")
    # MAX Intensity Level
    L = 256

    # Get Dimensions of image (row, col)
    dim = img.shape    

    # Initialize Everything For Use Below
    hist = [0] * L
    cumulative = [0] * L
    equ = copy.copy(img)

    # Builds Histogram
    for i in range(dim[0]):
        for j in range(dim[1]):
            hist[(img[i][j])] = hist[(img[i][j])] + 1

    # Builds Cumulative Histogram
    for i in range(1, L-1):
        cumulative[i] = cumulative[i-1] + hist[i]
    # print(cumulative)
    # Normalize Cumulative Histogram
    c = ((L-1)/(dim[0]*dim[1]))       # (L-1)/(M*N)
    # print(c)
    for i in range(L-1):
        cumulative[i] = round(c * cumulative[i])

    # print(cumulative)
    # Transforms Image By Assigning New Grey Value
    for i in range(dim[0]):
        for j in range(dim[1]):
            equ[i][j] = cumulative[img[i][j]]
    return equ

def main():
    # Reads image into an array
    img = imread('test_images/washedout.tif', IMREAD_GRAYSCALE)
    #img = np.array([[1,8,6,6],[6,3,11,8],[8,8,9,10],[9,10,10,7]], np.int32)
    result = hist_eq(img)
    # Stacks the input and output images together
    result = np.hstack((img, result))

    # Writes the image to a file
    imwrite('histequ_result.png', result)

    # Displays the result
    imshow('Side By Side', result)
    waitKey(0)
    destroyAllWindows()
    #imshow('By Itself', equ)
    #waitKey(0)
    #destroyAllWindows()

if __name__ == "__main__":
    main()