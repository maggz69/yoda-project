from math import sqrt
import sys
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2

# Read Image as Numpy Array


def readImgAsArray(imgPath):
    return cv2.imread(imgPath)


def writeImage(img, imgPath):
    mpimg.imsave(imgPath, img)


def convertImageToBlackAndWhite(imgArray):
    gray = cv2.cvtColor(imgArray, cv2.COLOR_BGR2GRAY)
    return gray


def performSobelEdgeDetection(imgArray):

    # pad the image with zeros
    imgArray = np.pad(imgArray, pad_width= ([1, ], [1, ]), mode= 'constant', constant_values= (0, 0))
    
    # defone sobel filters
    vertical_grad_filter = np.array([[1, 0, -1],[2, 0, -2],[1, 0, -1]])
    horizontal_grad_filter = np.array([[1, 2, 1],[0, 0, 0],[-1, -2, -1]])

    # define the kernel width
    # this is the pixel group size
    kernel_width = vertical_grad_filter.shape[0]//2
    
    # create gradient array that will store the returned edges
    grad_ = np.zeros(imgArray.shape)

    print("\n")

    for i in range(kernel_width, imgArray.shape[0] - kernel_width):
        for j in range(kernel_width, imgArray.shape[1] - kernel_width):
            x = imgArray[i - kernel_width: i + kernel_width + 1, j - kernel_width: j + kernel_width + 1]
            x = x.flatten() * vertical_grad_filter.flatten()
            sum_x = x.sum()

            y = imgArray[i - kernel_width: i + kernel_width + 1, j - kernel_width: j + kernel_width + 1]
            y = y.flatten() * horizontal_grad_filter.flatten()
            sum_y = y.sum()

            grad_[i - kernel_width][j - kernel_width] = sqrt(sum_x**2 + sum_y**2)
    
    # print progress
    j = (i + 1) / range(kernel_width, imgArray.shape[0] - kernel_width)
    sys.stdout.write('\r')
    # the exact output you're looking for:
    sys.stdout.write("[%-20s] %d%%" % ('='*int(20*j), 100*j))
    sys.stdout.flush()
    return grad_




if __name__ == "__main__":
    imgPath = "./yoda.jpg"

    img_array = readImgAsArray(imgPath)

    gray_img = convertImageToBlackAndWhite(img_array)

    # show image
    plt.imshow(gray_img)
    plt.savefig('./yoda_grayscale.jpg')

    gradient_img = performSobelEdgeDetection(gray_img)

    # # check if gradient_img is numpy array
    if (type(gradient_img) == np.ndarray):
        plt.imshow(gradient_img)
        plt.savefig('./yoda_lines.jpg')
