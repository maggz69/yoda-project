import os
import numpy as np
import cv2

def getAllFileNames(path, filter):
    files =  [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    # filter only filenames with MedianFiltered
    files = [f for f in files if filter in f]
    return files



def old():
    filtered = np.loadtxt('filtered_data.txt')
    filtered = filtered.astype('uint8')
    cv2.imwrite('cpp_filtered.jpg', filtered)

    filtered = np.loadtxt('OpenCL_filtered_data.txt')
    filtered = filtered.astype('uint8')
    cv2.imwrite('CL_filtered.jpg', filtered)

def saveFileAsImage(fileName, imageName):
    img = np.loadtxt(os.path.join(os.getcwd()+"/data/imageData",fileName))
    img = img.astype('uint8')
    cv2.imwrite(imageName, img)

if __name__ == '__main__':
    name = getAllFileNames('data/imageData', 'MedianFiltered')
    for f in name:
        newPathName = os.path.abspath(os.path.join(os.getcwd()+"/data/image", f.split(".")[0]+".png"))
        print(newPathName)
        saveFileAsImage(f,newPathName )

    name = getAllFileNames('data/imageData', 'CL_Filtered')
    for f in name:
        newPathName = os.path.abspath(os.path.join(os.getcwd()+"/data/image", f.split(".")[0]+"CL.png"))
        print(newPathName)
        saveFileAsImage(f,newPathName )