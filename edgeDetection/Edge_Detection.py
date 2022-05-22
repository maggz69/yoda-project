import cv2
import time

# Read the original image
path = 'cctv4.jpg'
img = cv2.imread(path) 
# Display original image
#cv2.imshow('Original', img)
#cv2.waitKey(0)
start = time.time()
# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 


# Sobel Edge Detection
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection


# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
# Display Canny Edge Detection Image
end = time.time()
print("Sequential Edge Detection Execution time (in Milliseconds):", (end-start)*1000)
cv2.imwrite('goldenMeasureED.jpg', edges)


cv2.destroyAllWindows()
