#!/usr/bin/python

import socket
import sys

s = socket.socket()


port = int(sys.argv[1])

s.bind(('0.0.0.0', port))

s.listen(5)

while True:
	c, addr = s.accept()
	print addr
	c.send("Connected")
	c.close()
