from serial import Serial
import time

sp = Serial("/dev/ttyAMA0", 9600, timeout=2)
if (sp.isOpen() == False):
    sp.open()

sp.flushInput()

while 1:
    time.sleep(5)
    data = sp.read(sp.inWaiting())
    print "data =  " + data

sp.close()
