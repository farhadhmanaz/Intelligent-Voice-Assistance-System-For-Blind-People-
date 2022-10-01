def snap_tam():
    
    from PIL import Image
    import pytesseract
    import cv2
    import time
    import keyboard
    import RPi.GPIO as GPIO
    from time import sleep
    import gtts as gt 
    import os 
    import io
    import time
    from pynput.keyboard import Key, Listener
    from pydub import AudioSegment
    from pydub.playback import play
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(16,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(12,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    count = 0
    gv = gt.gTTS(text="OCR Tamil",lang = 'ta')
    c = "wel.mp3"
    gv.save(c)
    play(AudioSegment.from_mp3(c))
    os.remove(c)
     #OCR தமிழ் பயன்முறை
    cap = cv2.VideoCapture(0) # capture from camera
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        f = open("tamil.txt","w+")
        
        
        
                #print("Nothing Detected")
        _,frame = cap.read()
         
        cv2.imshow('Frame1',frame) #display the captured image
            
        if (cv2.waitKey(1) & 0xFF == ord('y'))or ((GPIO.input(16) == GPIO.HIGH)): #save on pressing 'y'
            cv2.imwrite('c1.png',frame)
            imgH ,imgW,_ = frame.shape
            x1,y1,w1,h1 = 0,0,imgH ,imgW
            
            imgchar = pytesseract.image_to_string(frame, lang = 'tam')
            imgboxes =  pytesseract.image_to_boxes(frame, lang = 'tam')
            print(imgchar)
            #with open("voice.txt","w") as f:
            f.write(imgchar)
        f.write("\nNothing Detected")
        #f.close()
                    
                    
        with open('tamil.txt',encoding="utf8") as f:
            TamilText1 = f.readlines()
           
        
        print("###")
        for TamilText in TamilText1:
            print(TamilText)
            if(TamilText == "\n" or TamilText == "Nothing Detected"):
               continue
            else:
                
                try:
                    if (TamilText != "Nothing Detected"):
                        gv = gt.gTTS(text=TamilText,lang = 'ta')
                        b = "tamil.mp3"
                        gv.save(b)
                        play(AudioSegment.from_mp3(b))
                        os.remove(b)
                    
                except:
                    continue
        #if cv2.waitKey(1) == ord('q'):
        if(GPIO.input(12) == GPIO.HIGH):
            break
    cap.release()
    cv2.destroyAllWindows()





