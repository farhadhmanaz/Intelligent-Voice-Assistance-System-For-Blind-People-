def snap():
    from PIL import Image
    import pytesseract
    import cv2
    import time
    import keyboard
    import RPi.GPIO as GPIO
    cap = cv2.VideoCapture(0) # capture from camera
    cap.set(3, 640)
    cap.set(4, 480)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(12,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(16,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    count = 0
    f = open("voice.txt","w+")
    f.write("OCR English Mode")
    while True:
        f = open("voice.txt","w+")
        
                #print("Nothing Detected")
        _,frame = cap.read()
         
        cv2.imshow('Frame1',frame) #display the captured image
            
        if ((cv2.waitKey(1) & 0xFF == ord('y')) or (GPIO.input(16) == GPIO.HIGH)): #save on pressing 'y'
            cv2.imwrite('c1.png',frame)
            imgH ,imgW,_ = frame.shape
            x1,y1,w1,h1 = 0,0,imgH ,imgW
            
            imgchar = pytesseract.image_to_string(frame)
            imgboxes =  pytesseract.image_to_boxes(frame)
            print(imgchar)
            #with open("voice.txt","w") as f:
            f.write(imgchar)

        f.write("\nNothing Detected")
        #f.close()
                    
        #if cv2.waitKey(1) == ord('q'):
        if(GPIO.input(12) == GPIO.HIGH):
            break
    cap.release()
    cv2.destroyAllWindows()

