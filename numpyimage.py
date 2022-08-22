import cv2
import numpy as np
from PIL import Image

#image=Image.open('flower.png')
image=cv2.imread("flower.png")
arr=np.array(image)
#arr[:,:]=[,,0]
print(arr[10,10,:])
print(arr.shape)
print(arr.dtype)
print(arr.size)
print(arr.ndim)
#print(arr)
r =image[:,:,0]
g =image[:,:,1]
b =image[:,:,2]
print(r,g,b)

'''replace_arr = np.array([[[255, 255, 255]]]).repeat(558, 0).repeat(800, 1)
mask = np.repeat(np.all(arr == 0, axis = -1)[:, :, np.newaxis], 3, axis = -1)
arra = np.where(mask, 0, replace_arr)'''

'''Rmask= np.all(image==b,axis=-1)
image[Rmask]=[255,255,255]'''

if r  < [(75)] and g  < [(75)] and  b > [(128)] :
       r=(255, 255, 255) 
       g=(255, 255, 255)
       b=(255, 255, 255)

image.show()

# assign blue channel to zeros
#arr[:,:,2] = np.zeros([arr.shape[0], arr.shape[1]])


#img=Image.fromarray(arr)
#img.save('flowerr.png')
#img.show()





