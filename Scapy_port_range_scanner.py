#!/usr/bin/env python
from logging import getLogger, ERROR
getLogger('scapy.runtime').setLevel(ERROR)
from scapy.all import *	
import socket
# import time

target = raw_input('\nEnter Your Target : ')
ip  = socket.gethostbyname(target)
start_port = int(raw_input('Enter Starting Port : '))
end_port = int(raw_input('Enter Ending Port : '))

print('\n[ --> ] Scanning ' + target + ' For Open TCP Ports ...\n')

if start_port == end_port:
	end_port += 1

for x in range(start_port, end_port):
	packet = IP(dst=ip)/TCP(dport=x, flags='S')
	response = sr1(packet, timeout=0.5, verbose=0)

	if(str(type(response))=="<type 'NoneType'>"):
		pass

	elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
		print(' > Port ' + str(x) + ' is Open!')
	sr1(IP(dst=ip)/TCP(dport=x, flags='R'), timeout=0.5, verbose=0)
	# time.sleep(0.5)

print('\n[~#~ Scan is Complete ...!')