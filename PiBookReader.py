from serial import Serial
import time
import argparse
#import pygame
import random
import subprocess
import shlex

parser = argparse.ArgumentParser()
parser.add_argument("-r","--register", action="store_true", help="register RFID cards interactively")
args = parser.parse_args()


#Initialize serial port
sp = Serial("/dev/ttyAMA0", 9600, timeout=5)
if (sp.isOpen() == False):
    sp.open()
sp.flushInput()


if args.register:
    print "Registering new RFID cards"
    fname = raw_input('Enter filename --> ')
    rfid_dict = {}
    
    active = True
    while active:
        time.sleep(1)
        sp.flushInput()
        data = sp.read(14)
        if len(data) == 14 and data.encode('hex') not in rfid_dict.keys():
            print "Read new card id: " + data.encode('hex')
            id = raw_input('Enter Tag ID --> ')
            rfid_dict[data.encode('hex')] = id
            stop = raw_input("Exit? (Y/N)")
            if stop == 'Y' or stop == 'y':
                active = False
    
    ofile = open(fname,'w')
    for key in rfid_dict.keys():
    	ofile.write(key + " " + rfid_dict[key] + "\n")
    ofile.close()
else:
    from cards import card_dict
    #pygame.mixer.init()
    print "Done initializing...scan card for playback"
    playing = False
    while 1:
        time.sleep(1)
        sp.flushInput()
        data = sp.read(14)
        if len(data) == 14 and data.encode('hex') in card_dict.keys():
            if playing == True:
                #Kill previous process
                pass
            print "Successful read: " + data.encode('hex')
            print "File options are: "
            print card_dict[data.encode('hex')]
            if len(card_dict[data.encode('hex')]) == 0:
                print "No files found"
            else:
                print "Playing audio"
                audio_file = random.choice(card_dict[data.encode('hex')])
                mp3_player = subprocess.Popen(['mpg321',audio_file])
                playing = True
                #audio = pygame.mixer.Sound(audio_file[0])
                #audio.play()
        
    sp.close()
