#!/usr/bin/python

import socket
import struct

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x800))
#rawSocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.htons(0x0800))
#the 0x0800 means IP protocol
#/usr/include/linux/if_ether.h will show you the defined Ethernet Protocol ID's / Numbers
# PF_PACKET is used on linux, AF_INET is used on Mac

rawSocket.bind(("eth0", socket.htons(0x0800)))
#set ethernet adapter to use eth0

packet = struct.pack("!6s6s2s", '\xaa\xaa\xaa\xaa\xaa\xaa', '\xbb\xbb\xbb\xbb\xbb\xbb','\x08\x00')
#6s6s2s is the bytes used and how they are divided up.
#6 bytes, 6 bytes and 2 bytes
#the 3 parts are in Hex values which are the SRC and DST MAC addresses and the ethernet type 0x0800 which is IP

rawSocket.send(packet + "Hello there")
#send the data onto the wire.

