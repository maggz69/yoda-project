from posixpath import normpath
import numpy as np
import cv2
import os
import random


def readImageAsArray(imageName):
    img = cv2.imread(imageName, cv2.IMREAD_GRAYSCALE)
    return img


def getAllFilesInDirectory(path):
    # get all absolute paths of files in directory
    files = []
    for file in os.listdir(path):
        files.append(normpath(os.getcwd() + "/" + path+"/"+file))
    return files


def outputImageData(img,prefix,indx):
    imgShape = np.array([np.shape(img)[0], np.shape(img)[1]])
    # write into shape data file
    shapeFileDir = os.path.abspath(os.path.join(
        os.getcwd(), 'MedianFilter/data/shapeData/'+str(indx)+prefix+'.txt'))
    np.savetxt(shapeFileDir, imgShape, fmt='%d')

    # write into image data file
    imgFileDir = os.path.abspath(os.path.join(
        os.getcwd(), 'MedianFilter/data/imageData/'+str(indx)+prefix+'.txt'))
    np.savetxt(imgFileDir, img, fmt='%d')

    # save image into image directory
    cv2.imwrite(os.path.abspath(os.path.join(
        os.getcwd(), 'MedianFilter/data/image/'+str(indx)+prefix+'.png')), img)


def parseShapeData(fileNames):

    for indx, file in enumerate(fileNames):
        origImage = readImageAsArray(file)
        outputImageData(origImage, "_Original", indx)
        
        noisyImage = add_noise(origImage)
        outputImageData(noisyImage, "_Noisy", indx)


def add_noise(img):

    # Getting the dimensions of the image
    row, col = img.shape

    # Randomly pick some pixels in the
    # image for coloring them white
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):

        # Pick a random y coordinate
        y_coord = random.randint(0, row - 1)

        # Pick a random x coordinate
        x_coord = random.randint(0, col - 1)

        # Color that pixel to white
        img[y_coord][x_coord] = 255

    # Randomly pick some pixels in
    # the image for coloring them black
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):

        # Pick a random y coordinate
        y_coord = random.randint(0, row - 1)

        # Pick a random x coordinate
        x_coord = random.randint(0, col - 1)

        # Color that pixel to black
        img[y_coord][x_coord] = 0

    return img


if __name__ == "__main__":
    originalImagesPath = "MedianFilter/Images/Original"

    # read all files in directory
    files = getAllFilesInDirectory(originalImagesPath)

    parseShapeData(files)
