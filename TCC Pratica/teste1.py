# -- coding: utf-8 --

import cv2

video_src = 'footbal_americano_v2.avi'

cap = cv2.VideoCapture(video_src)

bike_cascade = cv2.CascadeClassifier('pedestrian.xml')

def MostraIMG(imagem):
    cv2.imshow("Jogador Detectado", imagem)

while True:
    ret, img = cap.read()
	
    
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bike = bike_cascade.detectMultiScale(gray,1.3,2)

    for(a,b,c,d) in bike:
        cv2.rectangle(img,(a,b),(a+c,b+d),(0,255,210),4)
        MostraIMG(img)
    
    cv2.imshow('video', img)
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
