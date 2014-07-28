from serial import Serial
import time

sp = Serial("/dev/ttyAMA0", 9600, timeout=5)
if (sp.isOpen() == False):
    sp.open()

sp.flushInput()

while 1:
    time.sleep(4)
    
    sp.flushInput()
    data = sp.read(14)
    
    #data = sp.read(sp.inWaiting())
    print "data =  " + data
    print "data length = " + str(len(data))
    print "data hex = " + data.encode('hex')

sp.close()
