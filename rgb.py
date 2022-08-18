import numpy as np
from PIL import Image
arr=np.zeros((2,2,3))
#arr=np.array()
print(arr)
img=Image.fromarray(arr,"RGB")
img.show()
img.save('img.png')
