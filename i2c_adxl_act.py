import smbus
from time import sleep

bus = smbus.SMBus(1)


bus.write_byte_data(0x53,0x31,0x2B) #initial data format and fall edge interrupt
bus.write_byte_data(0x53,0x24,0x10) #set ACT THREHOLD
bus.write_byte_data(0x53,0x25,0x08) #set INACT THREHOLD
bus.write_byte_data(0x53,0x26,0x01) 
bus.write_byte_data(0x53,0x27,0x66) #set ACT_x ACT_y INACT_x INACT_y
bus.write_byte_data(0x53,0x2F,0x10) #set INT2 pin receive ACT interrupt
bus.write_byte_data(0x53,0x2E,0x10) #enable ACT INACT interrupt
bus.write_byte_data(0x53,0x2D,0x08) #start measure



while True:
    inter = bus.read_byte_data(0x53,0x30)
    if((inter&0x10)==0x10):
        print("ACT detected\n")
    if((inter&0x08)==0x08):
        print("INACT detected\n")