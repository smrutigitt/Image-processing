import cv2
img="flower.png"
src=cv2.imread(img)
tmp=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
_,alpha= cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
b,g,r=cv2.split(src)
rgba=[b,g,r,alpha]
dst=cv2.merge(rgba, 4)
cv2.imwrite("gfg.png",dst)