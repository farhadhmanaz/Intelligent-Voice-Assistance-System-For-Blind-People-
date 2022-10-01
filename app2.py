from PIL import Image
import pytesseract
import cv2
import time
cap = cv2.VideoCapture(0)   # capture from camera
cap.set(3, 640)
cap.set(4, 480)

while True:
    _,frame = cap.read()
    imgH ,imgW,_ = frame.shape
    x1,y1,w1,h1 = 0,0,imgH ,imgW
    
    imgchar = pytesseract.image_to_string(frame, lang='tam')
    imgboxes =  pytesseract.image_to_boxes(frame, lang='tam')
    print(imgchar)
    for boxes in imgboxes.splitlines():
        boxes = boxes.split(' ')
        x,y,w,h = int(boxes[1]),int(boxes[2]),int(boxes[3]),int(boxes[4])
        cv2.rectangle(frame,(x,imgH-y),(w,imgH-h),(0,0,255),3)
        cv2.putText(frame,imgchar,(x1 +int(w1/50),y1+int(h1/50)),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255),2) 
        
        cv2.imshow('text',frame)
        if cv2.waitKey(2) & 0xFF ==ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
