import numpy as np
import cv2
import time


#import the cascade for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



def TakeSnapshotAndSave():
    # access the webcam (every webcam has a number, the default is 0)
    cap = cv2.VideoCapture(0)

    num = 0 
    #Analyse de la tête avant snapshot en se basant sur le dossier Filtered
    #Si tête connue unknow = 0, pas de snapshot, si tête inconnu on rentre dans boucle
    #if unknow=1:
    
    while num<10:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # to detect faces in video
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

        x = 0
        y = 20
        text_color = (0,255,0)
        #récupérer le dernier fichier opencv en base de donnée, récupérer son id
        cv2.imwrite('Unfiltered/'+str(num)+'.jpg',frame)
        num = num+1

    # When everything done, release the capture
    #cap.release()
    #cv2.destroyAllWindows()

    #Puis le logiciel de découpe analyse l'image, la découpe en 128x128px et la stock dans le fichier
    #Si tête connue on peut afficher le nombre de fois que la tête est apparu dans la frame




if __name__ == "__main__":
    TakeSnapshotAndSave()