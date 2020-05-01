#!/usr/bin/env python
import nmap
scanner = nmap.PortScanner()
scanner.scan('137.74.187.103')
for host in scanner.all_hosts():
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, scanner[host].hostname()))
    print('State : %s' % scanner[host].state())
    for proto in scanner[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)
        lport = scanner[host][proto].keys()
        lport.sort()
        for port in lport:
            print ('port : %s\tstate : %s' % (port, scanner[host][proto][port]['state']))
