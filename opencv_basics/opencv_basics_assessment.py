import cv2
import numpy as np

def draw_empty_circle(event,x,y,flag,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,255,0),5)
    
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,0,255),5)
        
cv2.namedWindow(winname='dog_backpack')

cv2.setMouseCallback('dog_backpack', draw_empty_circle)

img = cv2.imread('../Computer-Vision-with-Python/DATA/dog_backpack.jpg')

while True:
    cv2.imshow('dog_backpack', img)
    
    if cv2.waitKey(20) & 0xFF==27:
        break
        
cv2.destroyAllWindows()