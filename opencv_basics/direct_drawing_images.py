import cv2
import numpy as np

#True While mouse button down and vice versa
drawing = False
ix, iy = -1, -1

"""""
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,255,0),-1)
    
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,0,255),-1)
"""""



def draw_line(event,x,y,flags,param):
    global ix, iy, drawing
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.line(img,(ix,iy),(x,y),(255,0,0),5)
            
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(img,(ix,iy),(x,y),(255,0,0),5)

def draw_rectangle(event,x,y,flags,param):
    global ix, iy, drawing
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),(255,0,0), -1)
            
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(255,0,0), -1)
        
cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing', draw_line)

img = np.zeros((512,512,3))

while True:
    cv2.imshow('my_drawing', img)
    
    if cv2.waitKey(20) & 0xFF==27:
        break
        
cv2.destroyAllWindows()