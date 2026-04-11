import cv2
import sys
import numpy as np

Preview=0 #preview mode
Blur=1 #blur mode
Feature=2 #feature detection mode
Canny=3 #canny edge detection mode

feature_params=dict(maxCorners=100,
                    qualityLevel=0.3,
                    minDistance=7,
                    blockSize=7)  

s=0
if len(sys.argv)>1:
    s=int(sys.argv[1])
    
image_filter =Preview
alive=True

win_name="Camera Filter"
cv2.namedWindow(win_name,cv2.WINDOW_NORMAL)
result=None

source=cv2.VideoCapture(s)

while alive:
    has_frame, frame=source.read()
    if not has_frame:
        print("Failed to capture video")
        break
    
    if image_filter==Preview:
        result=frame
        
    elif image_filter==Canny:
        result=cv2.Canny(frame,80,150) #100 and 200 is threshold values for edge detection. You can adjust these values to get better results based on your specific use case and the characteristics of the video feed.
        
    elif image_filter==Blur:
        result=cv2.GaussianBlur(frame,(15,15),0)
        
    elif image_filter==Feature:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        corners=cv2.goodFeaturesToTrack(gray,**feature_params)
        
        if corners is not None:
            for x, y in np.float32(corners).reshape(-1, 2):
                cv2.circle(frame,(x,y),3,(0,255,0),-1)
        result=frame
    
    
    cv2.imshow(win_name,result)
    
    key=cv2.waitKey(1) & 0xFF
    if key==27: #ESC key to exit
        alive=False
    elif key==ord('p'):
        image_filter=Preview
    elif key==ord('b'):
        image_filter=Blur
    elif key==ord('f'):
        image_filter=Feature
    elif key==ord('c'):
        image_filter=Canny
        
source.release()
cv2.destroyAllWindows()