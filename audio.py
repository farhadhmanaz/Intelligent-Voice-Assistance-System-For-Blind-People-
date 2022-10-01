import gtts as gt 
import os 
import io
import time
import keyboard
from pynput.keyboard import Key, Listener
from pydub import AudioSegment
from pydub.playback import play

while (True):
    
    with open('voice.txt',encoding="utf8") as f:
        TamilText1 = f.readlines()
       
    
    print("###")
    for TamilText in TamilText1:
        print(TamilText)
        if(TamilText == "\n" or TamilText == "Nothing Detected"):
           continue
        else:
            
            try:
                if (TamilText != "Nothing Detected"):
                    gv = gt.gTTS(text=TamilText)
                    b = "voice.mp3"
                    gv.save(b)
                    play(AudioSegment.from_mp3(b))
                    os.remove(b)
                
            except:
                continue
        
        
    

                

  
# Collect all event until released

        

