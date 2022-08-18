import numpy as np
from PIL import Image

image=Image.open('flower.jpg')
array=np.array(image)
print(array[10,10,:])
image.show()

image.save('flower.png')
