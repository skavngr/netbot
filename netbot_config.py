ATTACK_TARGET_HOST = "192.168.0.109" # IP address of the machine to be attacked.
ATTACK_TARGET_PORT = "80" # Port Number of the machine to be attacked.

# Type of Attack
ATTACK_TYPE = "HTTP_FLOOD"

#Status codes that has to be set from the below list. 
	# HALT - To stop attacks immediately.
	# LAUNCH - To immediately start the attack.
	# HOLD - Wait for command.
	# UPDATE - Update Client.

ATTACK_STATUS = "HALT" # Choose any one Flag from above

ATTACK_STATUS = ATTACK_TARGET_HOST + "_" + ATTACK_TARGET_PORT + "_" + ATTACK_STATUS
