<<<<<<< HEAD
import cv2
import matplotlib.pyplot as plt
print ("OpenCV version:", cv2.__version__)
img=cv2.imread(r"C:\Users\466mo\Prgm\Python_prg\OpenCV\learn\checker.png")
cv_lam=cv2.imread(r"C:\Users\466mo\Prgm\Python_prg\OpenCV\learn\car.jpeg")

print ("Checkerboard image shape:", img.shape)
print ("Car image shape:", cv_lam.shape)

# Convert BGR to RGB for correct color display in matplotlib
cv_img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv_lam_rgb = cv2.cvtColor(cv_lam, cv2.COLOR_BGR2RGB)

# Displaying corrected images
plt.imshow(cv_img_rgb)
plt.title("Checkerboard - RGB")
plt.show()

plt.imshow(cv_lam_rgb)
plt.title("Car - RGB")
plt.show()



#using opencvv to display images

windowq1=cv2.namedWindow("Checkerboard")
cv2.imshow(windowq1, img)
cv2.waitKey(8000)
cv2.destroyWindow(windowq1)

windowq2=cv2.namedWindow("W2")
cv2.imshow(windowq2, cv_lam)
cv2.waitKey(3000)
cv2.destroyWindow(windowq2)




#changing window by pressing key 
winmdow4=cv2.namedWindow("W4")


Alive=True
while Alive:
    cv2.imshow(winmdow4, img)
    keypress=cv2.waitKey(1000)
    if keypress==ord('q'):
        Alive=False
cv2.destroyWindow(winmdow4)

cv2.destroyAllWindows()
=======
import cv2
import matplotlib.pyplot as plt
print ("OpenCV version:", cv2.__version__)
img=cv2.imread(r"C:\Users\466mo\Prgm\Python_prg\OpenCV\learn\checker.png")
cv_lam=cv2.imread(r"C:\Users\466mo\Prgm\Python_prg\OpenCV\learn\car.jpeg")

print ("Checkerboard image shape:", img.shape)
print ("Car image shape:", cv_lam.shape)

# Convert BGR to RGB for correct color display in matplotlib
cv_img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv_lam_rgb = cv2.cvtColor(cv_lam, cv2.COLOR_BGR2RGB)

# Displaying corrected images
plt.imshow(cv_img_rgb)
plt.title("Checkerboard - RGB")
plt.show()

plt.imshow(cv_lam_rgb)
plt.title("Car - RGB")
plt.show()



#using opencvv to display images

windowq1=cv2.namedWindow("Checkerboard")
cv2.imshow(windowq1, img)
cv2.waitKey(8000)
cv2.destroyWindow(windowq1)

windowq2=cv2.namedWindow("W2")
cv2.imshow(windowq2, cv_lam)
cv2.waitKey(3000)
cv2.destroyWindow(windowq2)




#changing window by pressing key 
winmdow4=cv2.namedWindow("W4")


Alive=True
while Alive:
    cv2.imshow(winmdow4, img)
    keypress=cv2.waitKey(1000)
    if keypress==ord('q'):
        Alive=False
cv2.destroyWindow(winmdow4)

cv2.destroyAllWindows()
>>>>>>> 33c8f2b (add all)
stop=1