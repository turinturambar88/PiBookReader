from serial import Serial
import time
import argparse

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
        if len(data) == 14 and data not in rfid_dict:
            print "Read new card id: " + data.encode('hex')
            id = raw_input('Enter Tag ID --> ')
            rfid_dict[data.encode('hex')] = id
        stop = raw_input("Exit? (Y/N)")
        if stop == 'Y' or stop == 'y':
            active = False
    
    ofile = open(fname,'w')
    #NEED TO WRITE DICTIONARY HERE
    ofile.close()
else:
    while 1:
        time.sleep(4)
    
        sp.flushInput()
        data = sp.read(14)
    
        #data = sp.read(sp.inWaiting())
        print "data =  " + data
        print "data length = " + str(len(data))
        print "data hex = " + data.encode('hex')
    
    sp.close()
