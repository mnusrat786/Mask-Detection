#these are libraries
import os
#open cv library
import cv2

arr = os.listdir("images/")

for aa in arr:
    aaa = aa.split('.')[0]
    img = cv2.imread(f"images/{aa}")
    ress = cv2.resize(img,(640,640))
    cv2.imwrite(f"folder2/{aaa}.png",ress) 
