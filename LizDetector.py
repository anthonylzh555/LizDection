import cv2
import numpy as np

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam = cv2.VideoCapture(0);
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)


rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("trainningData.yml")
id = 0
font = cv2.FONT_HERSHEY_COMPLEX_SMALL,1,1,0,1,1
while(True):
    ret,img = cam.read();
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5);
    for (x,y,w,h) in faces :
        cv2.rectangle(img,(x,y),(x+w,y+h), (0,0,255),2)
        id,conf = rec.predict(gray[y:y+h,x:x+w])
        if (conf<40) :   
            if (id==1) :
                   id = "Liz"
        else :
                id = "can't recongnize!!"
                
        """elif(id==2):
               id = "Obama"
        elif(id==3):
               id = "Wayne"
       """
        cv2.putText(img,str(id),(x,y+h),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,255)
    cv2.imshow("Face",img);
    if (cv2.waitKey(1) == ord('q')):
        break;
    
cam.release()
cv2.destroyAllWindows()
