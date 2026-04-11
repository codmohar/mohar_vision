import cv2
import sys

s=0            #by default, we use the first camera (index 0). If you have multiple cameras and want to use a different one, you can change the index accordingly. For example, if you want to use the second camera, you can set s=1.
if len(sys.argv)>1:
    s=int(sys.argv[1])   #if we want to use external camera, we can pass the camera index as an argument when running the script. For example, if we want to use the second camera, we can run the script with the command: python script.py 1 (since camera indices start from 0).
    
source=cv2.VideoCapture(s)   #

win_name="Camera Feed"
cv2.namedWindow(win_name,cv2.WINDOW_NORMAL)  #To create a resizable window for displaying the camera feed.

while cv2.waitKey(1) != 27:  #This loop will continue until the 'Esc' key (ASCII code 27) is pressed. Inside the loop, we read frames from the camera and display them in the window.
    has_frame, frame=source.read()   #The read() method returns a boolean value (ret) indicating whether the frame was successfully read, and the frame itself (frame).
    if not has_frame:
        print("Failed to capture video")
        break
    cv2.imshow(win_name,frame)
    
source.release()   #After the loop, we release the video capture object to free up system resources. This is important to ensure that the camera is properly released and can be used by other applications if needed.  
cv2.destroyAllWindows()   #Finally, we call cv2.destroyAllWindows() to close all OpenCV windows that were opened during the execution of the script. This ensures that any windows created for displaying the camera feed are properly closed when the script ends.


#in command promp write
# c:/Users/466mo/Prgm/Python_prg/OpenCV/opencv/Scripts/python.exe c:/Users/466mo/Prgm/Python_prg/OpenCV/learn/camera.py
#to execute the script