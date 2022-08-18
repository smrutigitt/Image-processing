from PIL import Image
img=Image.open('flower.png')

matrix = (1,0,0,0,  0,1,0,0,  0,0,0,0)
        
img=img.convert("RGB",matrix)
img.show()