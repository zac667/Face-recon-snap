import glob
import cv2
import os


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#select the path
path = "Unfiltered/*.*"
img_number = 0  #Start an iterator for image number.

img_list = glob.glob(path)

#Extract faces from a subset of images to be used for training.
#Resize to 128x128
i = 0
while i < 100000000:
    
    for file in img_list[0:25000]:
        print(file)     #just stop here to see all file names printed
        img= cv2.imread(file, 1)  #now, we can read each file since we have the full path
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        try:
            for (x,y,w,h) in faces:
                roi_color = img[y:y+h, x:x+w]
            #Va redimmensionner l'image en centrant sur les têtes 
            resized = cv2.resize(roi_color, (256,256))
            #Va les stocker dans le dossier Filtered
            cv2.imwrite("Filtered/"+str(img_number)+".jpg", resized)
        except:
            print("No faces detected")
        #Delete file from Unfiltered
        
        os.remove("Unfiltered/"+ str(img_number)+".jpg")
        img_number +=1     
        




