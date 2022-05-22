import numpy as np
import cv2

img = cv2.imread('salt-and-pepper-strangle_1.jpg', cv2.IMREAD_GRAYSCALE)
#img = cv2.resize(img, (1200,1200))
height = np.shape(img)[0]
width = np.shape(img)[1]
shape = np.array([height, width])
# img_data = np.zeros((height, width))
# for i in range(height):
#       for j in range(width):
#          img_data[i][j] = img[i][j][0]
np.savetxt("shape_data.txt", shape, fmt="%0.0f")
np.savetxt("image1_data.txt", img, fmt="%0.0f")
cv2.imwrite('input.jpg', img)