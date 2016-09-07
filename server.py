#!/usr/bin/python

import socket
import sys

s = socket.socket()

#host = socket.gethostname()
#host = socket.hostname('0.0.0.0')
port = int(sys.argv[1])
#print "listening on host:port", host, port
s.bind(('0.0.0.0', port))

s.listen(5)

while True:
	c, addr = s.accept()
	print addr
	c.send("Connected")
	c.close()
