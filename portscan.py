#!/usr/bin/python
from __future__ import print_function
import socket

host = socket.gethostname()

print("Scanning this host:", host)
#ports = 22, 80, 443, 8080

def scan(port):
	try:
		s = socket.socket()
		s.connect((host, port))
	except:
		print('', end="")
	else:
		print("Connected to port", port, "successfully")
	
	s.close

ports = range(1, 65535)
for port in ports:
	scan(port)
