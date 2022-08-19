from pickletools import uint8
import numpy as np
from PIL import Image

image=Image.open('flower.jpg')
arr=np.array(image)
#arr[:,:]=[,,0]
print(arr[10,10,:])
print(arr.shape)
print(arr.dtype)
print(arr.size)
print(arr)

# assign blue channel to zeros
arr[:,:,2] = np.zeros([arr.shape[0], arr.shape[1]])


img=Image.fromarray(arr)
#img.save('flowerr.png')
img.show()



