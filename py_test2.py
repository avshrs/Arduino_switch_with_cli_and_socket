import socket
import time
import serial
from ctypes import *
import struct

UDP_IP = "192.168.1.249"
UDP_PORT = 1337

"""   
-------------------------------------------------
uint8_t INSTRUCTIONS = 0;          
uint8_t MCPNR = 0; 
uint8_t MCPSIDE = 0; 
uint8_t VALUE = 0;
-----------------------------------------------
 
write one: 
uint8_t  - 0x00 | write one 
uint8_t  - 0xYZ | MCP NUMBER 0-7
uint8_t  - 0xYZ | SIDE  0 A | 1 B 
uint8_t  - 0xYZ | Y - PIN 0 - 7 , Z - value 0|1 0x00 | null

write all: 
uint8_t  - 0x01 | write all
uint8_t  - 0xYZ | MCP NUMBER 0-7
uint8_t  - 0xYZ | SIDE  0 A | 1 B 
uint8_t  - 0xYZ | 0x00 - 0xff | egz. 0b00010001


read all: 
uint8_t  - 0x11 | read all
uint8_t  - 0xYZ | MCP NUMBER 0-7
uint8_t  - 0xYZ | SIDE  0 A | 1 B 
uint8_t  - 0x00 | null

change delay:
uint8_t  - 0xF1 | change delay
uint8_t  - 0xYZ | MCP NUMBER 0-7
uint8_t  - 0xYZ | SIDE  0 A | 1 B 
uint8_t  - 0x00 | null      
"""    
def send_data(INSTRUCTIONS,MCPNR,MCPSIDE,VALUE):
    HEAD_ = '{:08b}'.format(INSTRUCTIONS)
    MCPADDRESS_  = '{:08b}'.format(MCPNR)
    PIN_ = '{:08b}'.format(MCPSIDE)
    RW_ = '{:08b}'.format(VALUE)
    frame = int(HEAD_+MCPADDRESS_+PIN_+RW_, 2)
    frame_be = struct.pack('>I', frame)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.sendto(frame_be , (UDP_IP, UDP_PORT))


#send_data(0x00,0x00,0x01,0x31)
#send_data(0x00,0x01,0x01,0x31)

#send_data(0x11,0x01,0x01,0xff)
#send_data(0x11,0x00,0x01,0xff)


send_data(0x00,0x01,0x01,0x00) 
send_data(0x00,0x00,0x01,0x00) 

send_data(0x11,0x00,0x00,0x00) #0x20 in A  

send_data(0x11,0x01,0x00,0x00)
