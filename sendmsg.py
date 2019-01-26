#!/usr/bin/python3

import socket
import struct
import time
import ComfoNetCan as CN

def msgclass():
    data =[
            0x84, #CmdID
            0x15, #ItemInLookupTable
            0x01, #Type --> selects field1 or field2... if that field is 1, OK
            #Start actual command... 
            0x01, #FF special case, otherwise -1 selects timer to use..?SubCMD?
            0x00, 0x00, 0x00, 0x00, #v9
            0x00, 0x1C, 0x00, 0x00, #v10
            0x03, #v11 Check vs type-1 0: <=3, 1,2,9:<=2, 3,4,5,6,7,8<=1
            0x00,
            0x00,
            0x00]


# create a raw socket and bind it to the given CAN interface
s = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
s.bind(("slcan0",))
cnet = CN.ComfoNet(s)
cnet.FindComfoAirQ()

#Set Ventilation level
#write_CN_Msg(0x11, 0x32, 1, 0, 1, 0, [0x84,0x15,0x01,0x01,0x00,0x00,0x00,0x00,0x00,0x1C,0x00,0x00,0x03,0x00, 0x00, 0x00]) 

#cnet.write_CN_Msg(0x11, cnet.ComfoAddr, 1, 0, 1, [0x84,0x15,0x02,0x01,0x00,0x00,0x00,0x00,0x10,0x3E,0x00,0x00,0x01,0x00, 0x00, 0x00])

#Set bypass to auto
#cnet.write_CN_Msg(0x11, cnet.ComfoAddr, 1, 0, 1, [0x85,0x15,0x02,0x01])

#set Bypass
#cnet.write_CN_Msg(0x11, cnet.ComfoAddr, 1, 0, 1, [0x84,0x15,0x02,0x01,0x00,0x00,0x00,0x00,0x10,0x0E,0x00,0x00,0x01,0x00, 0x00, 0x00])
#set Boost
#CN.write_CN_Msg(0x11, 0x32, 1, 0, 1, [0x84,0x15,0x01,0x06,0x00,0x00,0x00,0x00,0x10,0x0E,0x00,0x00,0x03,0x00, 0x00, 0x00])

#Set Exhaust only
#cnet.write_CN_Msg(0x11, cnet.ComfoAddr, 1, 0, 1, [0x84,0x15,0x07,0x01,0x00,0x00,0x00,0x00,0x10,0x0E,0x00,0x00,0x01,0x00, 0x00, 0x00])
#cnet.write_CN_Msg(0x11, cnet.ComfoAddr, 1, 0, 1, [0x85,0x15,0x07,0x01])

cnet.write_CN_Msg(0x11, cnet.ComfoAddr, 1, 0, 1, [0x83,0x15,0x01,0x06])

#for n in range(0xF):
#    write_CN_Msg(0x11, 0x32, 1, 0, 1, 0, [0x87,0x15,n])
#    time.sleep(1)
#write_long_message(0x01, 0x1F005051, [0x84,0x15,0x01,0x01,0x00,0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x01,0x00])
#write_long_message(0x01, 0x1F005078, [0x84,0x15,0x01,0x01,0x00,0x00,0x00,0x00,0x20,0x1C,0x00,0x00,0x03,0x00,0x00,0x00])
#for iterator in range(0xF):
#    time.sleep(4)
#write_long_message(1, 0x1F005051, [0x84,0x15,0x01,0x01,0x00,0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x03,0x00,0x00,0x00])
#write_long_message(1, 0x1F005051, [0x84,0x15,0x08,0x01,0x00,0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x01]) #manual mode
#write_long_message(1, 0x1F005051, [0x85,0x15,0x08,0x01]) #auto mode
#canwrite(0x1F015051, [0x85,0x15,0x08,0x01]) #auto mode
#for iterator in range(0xF):
#    write_long_message(iterator,0x1F005051, [0x84, 0x15, 0x08, 0x01, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01])
#    time.sleep(0.5)
#    write_long_message(iterator, 0x1F005051, [0x84,0x15,0x01,0x01,0x00,0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x03,0x00])
#    time.sleep(2)
#canwrite(0x1F075051|socket.CAN_EFF_FLAG, [0x00, 0x84, 0x15, 0x01, 0x01, 0x00, 0x00, 0x00])
#canwrite(0x1F075051|socket.CAN_EFF_FLAG, [0x01, 0x00, 0x20, 0x1C, 0x00, 0x00, 0x03, 0x00])
#while True:
#    canwrite(0x10140001,[0x21,0x22,0xC2,0x22])
#    time.sleep(4)

#write_long_message(0x05, 0x1F005051, [0x01,0x01,0x01,0x10,0x08,0x00,0x00])

cnet.ShowReplies()