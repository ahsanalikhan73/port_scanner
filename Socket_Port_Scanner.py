#!/usr/bin/env python
import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])	# Translate hostname to IPv4
else:
	print('\n[-] Invalid Syntax')
	print('\n[-] Syntax: python file-name.py <ip> ')
#Add a pretty banner
print('\n')
print('-' * 70)
print('\nScanning Target ' + target)
print('\nTime Started : ' + str(datetime.now()) + '\n')
print('-' * 70 + '\n')

try:
	for port in range(0, 1024):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)	# wait for 1 sec and then move on
		result = s.connect_ex((target, port))
		#print('checking port {}'.format(port))
		if result == 0:		# connect_ex return 0 if port is open
			print('[+] Port {} is open'.format(port))
		s.close()	# close the connection and make new connection for other port
except KeyboardInterrupt:
	print('\n[-] Exitting Program ...')
	sys.exit()

except socket.gaierror:
	print('[-] Hostname could not be resolved ...')
	sys.exit()

except socket.error:
	print('[-] Could not connect to server ...')
	sys.exit()




'''
This Port Scanner script works fine but have a little vulnerability i.e., a Human error
(192.tjkreth.678.45t or 257.4.525 like this etc human errors)

socket.setdefaulttimeout(1) --> attemp to connect to a port. if port is not connectable,
wait for 1 second and then move on.
connect_ex returns integer value. 0 for success and 1 for failure
'''
