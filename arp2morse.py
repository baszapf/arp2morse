#!/usr/bin/env python
 
import sys, time, pygame, logging
from scapy.all import *

logging.basicConfig(format='%(levelname)s/%(asctime)s: %(message)s', level=logging.INFO)

ONE_UNIT = 0.5
THREE_UNITS = 3 * ONE_UNIT
SEVEN_UNITS = 7 * ONE_UNIT
PATH = '[FULL OR RELATIVE PATH TO SOUND FILES]/morse_sound_files/'
LEASE_TIME_HOURS = 2

device_list = {}

# Add the MAC addresses of your devices in the list below
mac_notification_list = {'aa:bb:cc:dd:ee:ff': 'Tom Laptop Tom',
					'ff:ee:dd:cc:bb:aa': 'Jack Cellphone'
					}

def playmorsecode(msg):
	logging.debug("Morse: " + msg)
	for char in msg:
		pygame.mixer.music.load(PATH + char.upper() + '_morse_code.ogg')
		pygame.mixer.music.play()
		time.sleep(THREE_UNITS)
	time.sleep(SEVEN_UNITS)

if len(sys.argv) != 2:
    print "Usage: python arp2morse.py 192.168.1.0/24"
    sys.exit(1)

try:.py
	while True:
		logging.debug(device_list)

		pygame.init()
		now = time.time() # timestamp in seconds

		# Mark and delete old entries in device_list
		# Source: http://stackoverflow.com/questions/5384914/how-to-delete-items-from-a-dictionary-while-iterating-over-it
		for device, val in device_list.items(): 
			difference = now - val
			if (difference > LEASE_TIME_HOURS*3600):
				logging.info( device + " will be removed from list.")
				del device_list[ device ]			
			# else:
				# logging.debug("Lease time of " + device + " is still ok.")

		# Perform scan and check for new devices
		logging.debug("Scanning for devices ...")
		alive,dead=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=sys.argv[1]), timeout=2, verbose=0)
		logging.debug("MAC - IP")
		for i in range(0,len(alive)):
			logging.debug( alive[i][1].hwsrc + " - " + alive[i][1].psrc ) # "MAC - IP"
			mac_address = alive[i][1].hwsrc
			# notify if applicable and updates list
			if not device_list.has_key(mac_address):
				if mac_notification_list.has_key(mac_address):
					logging.info("Device found (" + mac_address + ", " + mac_notification_list[ mac_address ] + ")")
					playmorsecode( mac_notification_list[ mac_address ] )
			device_list[ mac_address ] = now # create/update entry
		logging.debug("... sleeping ...")
		time.sleep(30)

except Exception as e:
	logging.warning("Error: %s" % str(e) )