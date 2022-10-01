# Intelligent-Voice-Assistance-System-For-Blind-People

## Download the given File using 
  ```
   $ wget https://github.com/farhadhmanaz/Intelligent-Voice-Assistance-System-For-Blind-People-.git
  ```

## Then Set up TFLite object detection system on your Raspberry Pi
   ```
   $ sudo apt-get update
   $ sudo apt-get dist-upgrade
   ```
## Install OpenCV TensorFlow Lite and Relavant Packages
   ```
   $ bash get_pi_requirements.sh
   ```
## Now Setup OCR (Optical Character Recognition)
```
   $ sudo apt-get update
   
   ### Install OpenCV
   $ sudo apt-get install python3-pil.imagetk
   $ pip install opencv-python 
   $ pip install opencv-contrib-python
   ### Install Tesseract/Pytesseract
   $ sudo apt install tesseract-ocr
   $ sudo apt install libtesseract-dev
   $ pip install pytesseract
 ```
## SetUp Raspberry Pi GPIO and Enable buttons
```
   $ sudo apt-get install rpi.gpio
   $ sudo raspi-config 
   ```
   ### Now enable relavant pins of respective protocols 

## Setup GTTS (Google Text To speech)
```
   $  sudo pip3 install gTTS
```   
   ### Install other lagging packages on running the program


## Setup GPS 
   ### Connect GPS Module
      Vcc - pin 1 (3.3v)
      RX  - pin 8
      TX  - pin 10
      Gnd - pin 6 
### Download the required Packages 
   ```
   $ sudo apt-get install gpsd gpsd-clients
   $ man gpsd
   ```
### Edit the /boot/config.txt file, you need to open this file in any text editor  using nano:
      
        $ sudo nano /boot/config.txt
     
### At the end of the file add the following lines:
      dtparam=spi=on
      dtoverlay=pi3-disable-bt
      core_freq=250
      enable_uart=1
      force_turbo=1
 ### You need to backup for the cmd so raspbian uses the UART as a serial console and so we need to turn off that functionality. To do so we need to change the      /boot/cmdline.txt file. 
 ```
   $ sudo cp /boot/cmdline.txt /boot/cmdline_backup.txt
 ```
### Open the file in a text editor and edit it.
   ```
   $ sudo nano /boot/cmdline.txt
   ```
### Replace the content with the following line (delete everything in it and write down the following content)
    
   $ dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet splash plymouth.ignore-serial-consoles
    
### Now reboot pi using:
   ```
   $ sudo reboot
   ```
#### Now it will start working here you need to make sure that the LED with blue light is blinking if it's no blinking I would you recommend going on the terrace or open sky or window because it needs to catch at least 3 satellites to generate NMEA sentence it might take around 20 to 30 mins to catch the  signals so you need to have patience while using Neo 6m 2V.When the Red led is blinking, run the following command
```
   $ sudo cat /dev/ttyAMA0
```   
#### After this, it Generates NMEA sentence which is basically the location you can convert these sentence into Latitude and longitude.
 
 ### This Set of command need to be executed everytime you boot into the pi.
 ```
   $ sudo systemctl stop gpsd.socket
   $ sudo systemctl disable gpsd.socket
   $ sudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock
```
## To check Whether we are connected with satelite and Lat Long is recieved use any one of the below given command.
```
  $ sudo cgps -s
  $ sudo gpsmon
```


## Setup steps have been executed. 

## To run the program 
   ### Open Terminal
   ```
      $ cd tflite1_cpy
      $ python3 main.py
   ```   
      

#### ____________________________________________@Copyrights belongs to Edge Matrix Corporation ____________________________________________________
