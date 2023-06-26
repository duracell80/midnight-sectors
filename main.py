#!/usr/bin/python3
# Author: Lee Jordan
# Github: Duracell80

import time, os
from datetime import datetime

# Padding
def format(n, digits):
	formatter = '{:.' + '{}'.format(digits) + 'f}'
	x = round(n, digits)
	return formatter.format(x)

# Seconds per day
def get_spd():
	d = 1
	h = d * 24
	m = h * 60
	s = m * 60

	return int(s/100)

# Sectors per hour
def get_sph():
	s = get_spd()
	return int(round(float((int(s) / 24)), 0))

# Sectors since midnight
def get_ssm():
	now = datetime.now()
	ssm = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()

	return format(float((ssm/100)), 2)

# Sectors to midnight
def get_stm():
	now = datetime.now()
	ssm = get_ssm()
	stn = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
	stm = format(float(864 - (stn/100)), 2)

	return stm



# Sector Clock for Today's Segment
while True:
	now = datetime.now()
	ssm = get_ssm() # sectors since midnight
	stm = get_stm() # sectors to midnight
	sph = get_sph() # sectors per hour

	os.system("clear")
	print("Local Time: " + str(now.strftime("%H:%M:%S")) + "  [ssm @" + str(ssm) + " stm @" + str(stm) + " (sph: " + str(sph)  + ")]")

	time.sleep(1)
