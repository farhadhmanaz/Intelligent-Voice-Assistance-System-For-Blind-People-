from gps import *
import time

running = True
import RPi.GPIO as GPIO
from time import sleep
from twilio.rest import Client 
account_sid = 'AC835e177f879dc1ebd27ef760f6e6e705'
auth_token = '570d003f4a485e932db9e4c1b1876d66' 
client = Client(account_sid, auth_token)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def getPositionData(gps):
    nx = gpsd.next()
    # For a list of all supported classes and fields refer to:
    # https://gpsd.gitlab.io/gpsd/gpsd_json.html
    
    if nx['class'] == 'TPV':
        latitude = getattr(nx,'lat',"NA")
        longitude = getattr(nx, 'lon',"NA")
        lat = str(latitude)
        lon = str(longitude)
        if (lat != "NA" and lon != "NA"): 
            a = ("Emergency!!!: lat = " + lat + ", lon = " + lon)
            f = open("location.txt","w+")
            f.write(a)
            with open('location.txt',encoding="utf8") as f:
                locate = f.readlines()
            print(locate)
            
        else:
            with open('location.txt',encoding="utf8") as f:
                locate = f.readlines()
            print(locate)
        if GPIO.input(18) == GPIO.HIGH:
                print("response recieved")
                message = client.messages.create(  
                                      messaging_service_sid='MG510d4b2b4b0c51641892a6ae5913eb32', 
                                      body=locate,      
                                      to='+917373632850 ' 
                                  )
                print(message.sid, locate)
                time.sleep(0.5)

gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

try:
    print("Application started!")
    while running:
        getPositionData(gpsd)
        time.sleep(1.0)

except (KeyboardInterrupt):
    running = False
    print("Applications closed!")
