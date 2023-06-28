#!/usr/bin/python3
# Author: Lee Jordan
# Github: Duracell80

# An attempt at linking base 8 time to real time in a .beats style format

import time, os
from datetime import datetime
from dateutil import tz

def init():
	global iso; iso = [1, 24, 1440, 864000, 864]
	return iso

def format(n, digits):
	formatter = '{:.' + '{}'.format(digits) + 'f}'
	x = round(n, digits)
	return formatter.format(x)

def scale(max = 864, min = 0, sector = 432):
	return ((sector - min) / (max - min)) * 100

def get_bar():
	spc = get_spc()
	tl = ""; tr = "";
	ti = "+"

	for x in range(0, int((spc / 2))):
		tl+="-"; x+=1

	for y in range(0, int((100 - spc) / 2)):
		tr+="-"; y+=1

	tb = str(tl) + "[" + str(ti) + "]" + str(tr)
	return tb

def get_labels():
	return "DS 1 2 3 4 5 6 7 8  11 AM/PM  2 3 4 5 6 7 8 9 10  DE"

# Seconds per day
def get_spd():
	return int(iso[3])

# Sectors per hour
def get_sph():
	return int(round(float((int(iso[4]) / iso[1])), 0))

# Sectors elapsed in this segment
def get_spc():
	ssm = get_ssm()
	return int(round(scale(int(iso[4]), 0, float(ssm)),0))

# Sectors remaining in this segment
def get_spr():
	spc = get_spc()
	return int(abs(100-spc))

# Sectors since midnight
def get_ssm():
	now = datetime.now()
	return format(float(((now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()/100)), 2)

# Sectors to midnight
def get_stm():
	now = datetime.now()
	ssm = get_ssm()
	stn = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
	stm = format(float(iso[4] - (stn/100)), 2)

	return stm

# Slice Sectors into 8 Slices
def get_sst():
	spc		= get_spc()
	sst     	= float(float(get_ssm()) / 100)
	slice  		= str(sst).replace(".", ":").split(":")

	if spc <= 22:
		slice_p = "N"
		slice_d = "Night"
	elif spc < 50:
		slice_p = "M"
		slice_d = "Morning"
	elif spc <= 75:
		slice_p = "A"
		slice_d = "Afternoon"
	elif spc <= 85:
		slice_p = "E"
		slice_d = "Evening"
	elif spc <= 100:
		slice_p = "N"
		slice_d = "Night"
	else:
		slice_p = "N"
		slice_d = "Deep Night"

	slice_h	= str(slice[0]).rjust(2, '0')
	slice_m	= str(slice[1][0:2]).rjust(2, '0')
	slice_s = str(slice[1][2:4]).ljust(2, '0')

	return str(str(slice_h) + ":" + str(slice_m) + ":" + str(slice_s) + " Sector[" + str(slice_h) + "] Period[" + str(slice_d) + "]")

def get_tick():
	ssm = str(get_ssm()).split(".")
	tic = ssm[1]
	return tic

# Create a degree of first hand
def get_first_hand():
	ssm = get_ssm()
	#d = 1
	#h = d * 24
	#p = h / 10 #2.4

	return int(float(float(ssm) / 2.4))

# Create a degree of second hand
def get_second_hand():
	sec = get_tick()
	s = scale(28, 0, int(sec))

	return int(s)


# Define local time in beats
def get_blt():
	ssm = get_ssm()
	bld = float(1000 - 864)
	blt = float(float(ssm) + bld)

	return str(format(float(blt), 0)).rjust(3, '0')

# Define universal time in beats
def get_bit(tz_base = "UTC"):
	from_zone = tz.gettz(tz_base)
	to_zone = tz.gettz('Europe/Zurich')
	time = datetime.utcnow()
	utc_time = time.replace(tzinfo=from_zone)
	zurich_time = utc_time.astimezone(to_zone)

	h, m, s = zurich_time.timetuple()[3:6]

	beats = ((h * 3600) + (m * 60) + s) / 86.4

	if beats > 1000:
		beats -= 1000
	elif beats < 0:
		beats += 1000

	return str(format(float(beats), 0)).rjust(3, '0')

def get_ltz():
	now = datetime.now()
	local_now = now.astimezone()
	local_tz = local_now.tzinfo
	local_tzname = local_tz.tzname(local_now)

	return str(local_tzname)

# Local Standard Time
def get_lst():
	now = datetime.now()

	return str(now.strftime("%H:%M:%S"))

# Sector Clock for Today's Segment
iso = init()

while True:

	ssm = get_ssm() # sectors since midnight
	stm = get_stm() # sectors to midnight
	sph = get_sph() # sectors per hour
	spc = get_spc()	# progress through the sector as completed percentage
	spr = get_spr()	# sectors remaining this segment as percentage to be completed
	hst = get_first_hand()
	hnd = get_second_hand()

	blt = get_blt()	# produce a local version of a .beat
	bit = get_bit("UTC+1")	# produce the universal internet time from Swatch during daylight savings









	os.system("clear")
	print("Local Time: " + get_lst() + "  [ssm @" + str(ssm) + " stm @" + str(stm) + " spc: " + str(spc)  + "% spr: " + str(spr)  + "%]")
	print("Range Bar : " + get_bar())
	print("            " + get_labels())
	print("\n\n")
	print("Where")
	print("- stm = Sectors til midnight      (.tick is a sector's second [0-100])")
	print("- ssm = Sectors since midnight    (.tick   = 1 minute 40 seconds)")
	print("- spc = Segment percent completed (.range  = from 0 to 100%)")
	print("- spr = Segment percent remaining")
	print("- sph = Sectors per standard hour (~" + str(sph) + " .sectors in an hour)")
	print("- blt = Beats in Local time (.beat = 1min:25s, ~42 .beats in an hour)")
	print("\nPERIOD = [N]ight [A]fternoon [M]orning [E]vening")
	print("DS/DE  = [D]ay[S]tart [D]ay[E]nd")

	print("\n\n")
	print("Segment Time  (Oct:Dec:Dec)  : " + str(get_sst()))
	print("Angle of Tick (second hand)  : °" + str(hnd))
	print("Angle of Sector (hour hand)  : °" + str(hst))
	print("\n")
	print("Local Beat                   : @" + str(blt) + ".beats (" + str(get_ltz())  + ")")
	print("Universal Beat               : @" + str(bit) + ".beats (BMT)")

	# Simulate a real clock display
	time.sleep(1)
