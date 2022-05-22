import numpy as np
import cv2

filtered = np.loadtxt('filtered_data.txt')
filtered = filtered.astype('uint8')
cv2.imwrite('cpp_filtered.jpg', filtered)

filtered = np.loadtxt('OpenCL_filtered_data.txt')
filtered = filtered.astype('uint8')
cv2.imwrite('CL_filtered.jpg', filtered)