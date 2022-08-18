
import cv2
import numpy as np

src=cv2.imread('flower.png')
print(src.shape)

src[:,:,0] = np.zeros([src.shape[0],src.shape[1]])

cv2.imwrite('blue.png',src)
