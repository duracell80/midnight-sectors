#!/usr/bin/python3
# Author: Lee Jordan
# Github: Duracell80

# An attempt at linking decimal time to real time in a .beats style format

import time, os
from datetime import datetime
from dateutil import tz

# Tear
def tear():
	global d, h, m, s, seg

	# Define the number of seconds in a day as in base 12
	d = 1
	h = d * 24
	m = h * 60
	s = m * 60

	# 864
	seg = s / 100

	return d, h, m, s, seg

# Padding
def format(n, digits):
	formatter = '{:.' + '{}'.format(digits) + 'f}'
	x = round(n, digits)
	return formatter.format(x)

# Scaling
def scale(max = 864, min = 0, sector = 432):
	return ((sector - min) / (max - min)) * 100

def get_bar(spc = 432):
	tick_left	= ""
	tick_right	= ""
	tick_icon	= "+"

	for x in range(0, int((spc / 2))):
		tick_left+="-"
		x+=1

	for y in range(0, int((100 - spc) / 2)):
		tick_right+="-"
		y+=1


	tick_bar	= str(tick_left) + "[" + str(tick_icon) + "]" + str(tick_right)
	return tick_bar

# Seconds per day
def get_spd():
	return int(s/100)

# Sectors per hour
def get_sph():
	return int(round(float((int(get_spd()) / 24)), 0))

# Sectors elapsed in this segment
def get_spc(ssm):
	return int(round(scale(int(seg), 0, float(ssm)),0))

# Sectors remaining in this segment
def get_spr(spc):
	return int(abs(100-spc))

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

# Slice Sectors into 8 Slices
def get_sst():
	spc		= get_spc(get_ssm())
	sst     	= float(float(get_ssm()) / 100)
	sliced  	= str(sst).replace(".", ":").split(":")

	if spc <= 22:
		sliced_h        = str(sliced[0]).rjust(2, 'N')
	elif spc < 50:
		sliced_h 	= str(sliced[0]).rjust(2, 'M')
	elif spc <= 75:
		sliced_h        = str(sliced[0]).rjust(2, 'A')
	elif spc <= 85:
		sliced_h        = str(sliced[0]).rjust(2, 'E')
	elif spc <= 100:
		sliced_h        = str(sliced[0]).rjust(2, 'N')
	else:
		sliced_h        = str(sliced[0]).rjust(2, 'N')

	sliced_m	= str(sliced[1][0:2]).rjust(2, '0')
	sliced_s	= str(sliced[1][2:4]).ljust(2, '0')

	return str(str(sliced_h) + ":" + str(sliced_m) + ":" + str(sliced_s))

# Create a degree out of 360 based on current segment since midnight
def get_deg(ssm):
	# 1 day = 24 hours / 10 = 2.4 (to divide the current ssm by)
	d = 1
	h = d * 24
	p = h / 10 #2.4

	return int(float(float(ssm) / p))

# Define local time in beats
def get_blt(ssm):
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


# Sector Clock for Today's Segment
d, h, m, s, seg = tear()

while True:
	now = datetime.now()
	ssm = get_ssm() # sectors since midnight
	stm = get_stm() # sectors to midnight
	sph = get_sph() # sectors per hour
	spc = get_spc(ssm)	# progress through the sector as completed percentage
	spr = get_spr(spc)	# sectors remaining this segment as percentage to be completed
	deg = get_deg(ssm)

	blt = get_blt(ssm)	# produce a local version of a .beat
	bit = get_bit("UTC+1")	# produce the universal internet time from Swatch during daylight savings









	os.system("clear")
	print("Local Time: " + str(now.strftime("%H:%M:%S")) + "  [ssm @" + str(ssm) + " stm @" + str(stm) + " spc: " + str(spc)  + "% spr: " + str(spr)  + "%]")
	print("Range Bar : " + str(get_bar(spc)))
	print("            DS 1 2 3 4 5 6 7 8  11 AM/PM  2 3 4 5 6 7 8 9  10 DE")
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
	print("Segment Slice (Octal)  : " + str(get_sst()))
	print("Segment Angle (0-360)  : @" + str(deg))
	print("Local Beat             : @" + str(blt) + ".beats (" + str(get_ltz())  + ")")
	print("Universal Beat         : @" + str(bit) + ".beats (BMT)")

	# Simulate a real clock display
	time.sleep(1)
