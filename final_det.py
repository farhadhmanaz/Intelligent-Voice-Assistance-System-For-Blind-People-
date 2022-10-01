from tfdet import *
from ocrsnap import *
from ocrsnap_tam import *        
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
count = 0



while True:
    
    
    while GPIO.input(12) == GPIO.HIGH:    
        sleep(0.2)
    count = count + 1
    while GPIO.input(12) == GPIO.LOW:
        sleep(0.1)
    print(count)
    
    if count == 1:
        detection()
    elif count == 2:
        snap()
    elif count == 3:
        count = 0
        snap_tam()
        
        
        
        
