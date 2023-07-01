#!/usr/bin/python3
# Author: Lee Jordan
# Github: Duracell80

# An attempt at linking base 8 time to real time in a .beats style format

import os, sys, time, math, asyncio

from datetime import datetime
from dateutil import tz


def background(f):
	def wrapped(*args, **kwargs):
		return asyncio.new_event_loop().run_in_executor(None, f, *args, **kwargs)

	return wrapped


def init():
	iso = [1, 24, 1440, 864000, 864]
	return iso

def format(n, digits):
	formatter = '{:.' + '{}'.format(digits) + 'f}'
	x = round(n, digits)
	return formatter.format(x)

def scale(max = 864, min = 0, sector = 432):
	return ((sector - min) / (max - min)) * 100

def get_lum(day = None):
	if day:
		day = str(day).lower()
	else:
		day = datetime.now().weekday()

	if day == 6 or day == "sunday" or day == "dimanche" or day == "domingo" or day == "domenica":
		return "solis"
	elif day == 0 or day == "monday" or day == "lundi" or day == "lunes" or day == "lunedi":
		return "lunae"
	elif day == 1 or day == "tuesday" or day == "mardi" or day == "martes" or day == "martedi":
		return "martis"
	elif day == 2 or day == "wednesday" or day == "mercredi" or day == "miercoles" or day == "mercoledi":
		return "mercurii"
	elif day == 3 or day == "thursday" or day == "jeudi" or day == "jueves" or day == "giovedi":
		return "jovis"
	elif day == 4 or day == "friday" or day == "vendredi" or day == "viernes" or day == "venerdi":
		return "veneris"
	elif day == 5 or day == "saturday" or day == "samedi" or day == "sabado" or day == "sabato":
		return "saturni"
	else:
		return "lumni"

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
	return "SS 1 2 3 4 5 6 7 8 9 10AM/PM  2 3 4 5 6 7 8 9 10  SE"


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
	ssm = format(float(((now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()/100)), 2)
	ssm = str(ssm).rjust(3, '0')
	return ssm

# Sectors to midnight
def get_stm():
	now = datetime.now()
	ssm = get_ssm()
	stn = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
	stm = format(float(iso[4] - (stn/100)), 2)
	stm = str(stm).rjust(3, '0')

	return stm


# Define Sectors as 8 Slices and 4 periods
def get_sst():
	spc		= get_spc()
	sst     	= float(float(get_ssm()) / 100)
	slice  		= str(sst).replace(".", ":").split(":")

	if spc <= 22:
		sector_p = "N"
		sector_d = "Night"
		sector_l = "nox"
	elif spc < 50:
		sector_p = "M"
		sector_d = "Morning"
		sector_l = "antemeridies"
	elif spc <= 75:
		sector_p = "A"
		sector_d = "Afternoon"
		sector_l = "post meridiem"
	elif spc <= 85:
		sector_p = "E"
		sector_d = "Evening"
		sector_l = "vespera"
	elif spc <= 100:
		sector_p = "N"
		sector_d = "Night"
		sector_l = "nocturnis"
	else:
		sector_p = "N"
		sector_d = "Night"
		sector_l = "nuper nocte"

	sel_string = sector_l

	#slice_h	= str(slice[0]).rjust(2, '0')
	sector_h = slice[0]
	sector_m = str(slice[1][0:2]).rjust(2, '0')
	sector_s = str(slice[1][2:4]).ljust(2, '0')

	if int(sector_m) <= 25:
		sector_q = str(int(sector_h)) + ".25"
	elif int(sector_m) <= 50:
		sector_q = str(int(sector_h)) + ".50"
	elif int(sector_m) <= 75:
		sector_q = str(int(sector_h)) + ".75"
	elif int(sector_m) <= 99:
		sector_q = str(int(sector_h)) + ".75"
	else:
		sector_q = str(int(sector_h)) + ".00"

	if int(sector_s) % 2 == 1:
		decond = " "
		period = " "
	else:
		decond = ":"
		period = str(sector_p)

	sector_hh = round(float((float(ssm) / 3.6) / 10),2)
	sector_hb = str(sector_hh).split(".")
	if int(str(sector_hb[1])) < 10:
		sector_hc = str(int(sector_hb[1])).rjust(2, '0')
	else:
		sector_hc = str(int(sector_hb[1]))
	if "0" in str(sector_hc):
                sector_hc = str(int(sector_hb[1])).ljust(2, '0')

	sector_hd = str(sector_hb[0]).rjust(2, '0')
	sector_hs = str(int(sector_hb[0]) - 12).rjust(2, '0')
	if int(sector_hb[0]) >= 13:
		sector_ht = str(int(sector_hb[0]) - 12)
	else:
		sector_ht = str(int(sector_hb[0]))

	#if int(sector_hb[0]) > 12:
	#	sector_hd = str(int(sector_hb[0]) - 12).rjust(2, '0')
	#else:
	#	sector_hd = str(sector_hb[0])

	sat_string = str(sector_ht) + ":" + str(sector_hc) + "⋅" + str(sector_p) + "ꝑ     Hour:" + str(int(float(sector_hh))) + " (" + str(sector_hc)  + "% complete)"
	sst_string = str(sector_hd) + ":" + str(sector_m) + ":" + str(sector_s) + "⋅" + str(sector_d)
	sss_string = str("H" + str(sector_h) + ":" + str(sector_m) + ":" + str(sector_s) + "⋅" + str(sector_p) + "ꝑ Segment[" + str(sector_q) + "] Period[" + str(sector_p) + "]")

	return sst_string, sat_string, sss_string, sel_string


def get_tick():
	ssm = str(get_ssm()).split(".")
	tic = ssm[1]
	return tic

def get_seg():
	if float(ssm) <= 200:
		seg = "centum"
	elif float(ssm) <= 300:
		seg = "ducenti"
	elif float(ssm) <= 400:
		seg = "trecenti"
	elif float(ssm) <= 500:
		seg = "quadrigenti"
	elif float(ssm) <= 600:
		seg = "quingenti"
	elif float(ssm) <= 700:
		seg = "sescenti"
	elif float(ssm) <= 800:
		seg = "septingenti"
	elif float(ssm) <= 900:
		seg = "octingenti"
	else:
		seg = "octodecim"

	return seg

# Create a degree of first hand
def get_first_hand():
	ssm = get_ssm()
	return int(float(float(ssm) / 2.4))

# Create a degree of second hand
def get_second_hand():
	tic = get_tick()
	return round((float(tic) * 3.55)/5.) * 5

# Create a degree of second hand
def get_third_hand():
	spc             = get_spc()
	sst             = float(float(get_ssm()) / 100)
	slice           = str(sst).replace(".", ":").split(":")
	sst_m 		= str(slice[1][0:2]).rjust(2, '0')

	return round((float(sst_m) * 3.55)/5.) * 5


# Define local time in beats
def get_blt():
	ssm = get_ssm()
	bld = float(1000 - 864)
	blt = float(float(ssm) + bld)

	return str(format(float(blt), 0)).rjust(3, '0')

# Define universal time in beats
def get_bmt(tz_base = "UTC"):
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
	bmt = str(format(float(beats), 0)).rjust(3, '0')
	return bmt

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


@background
def run_segment(when = "now"):
	global iso, hst, hnd, hrd, sss, ssm, stm, sbm, sst, sat, spc, spr, sph, spd, seg, sel, blt, bmt, lum
	iso = [1, 24, 1440, 864000, 864]
	hst = 0
	hnd = 0
	hrd = 0
	bmt = 0
	blt = 0
	sbm = 0
	stm = 0
	spc = 0
	spr = 0
	sss = "S1:00:00"
	sst = "00:00"
	sat = "00:00"
	seg = "unus"
	sel = "nox"
	lum = get_lum()

	while True:
		ssm = get_ssm() # sectors since midnight
		hst = get_first_hand()
		hnd = get_second_hand()
		hrd = get_third_hand()

		stm = get_stm() # sectors to midnight
		sph = get_sph() # sectors per hour
		spc = get_spc() # progress through the sector as completed percentage
		spr = get_spr() # sectors remaining this segment as percentage to be completed
		sst, sat, sss, sel = get_sst() # Get [S]tandard [S]ector [T]ime
		sbm = math.trunc(float(ssm))
		seg = get_seg()

		blt = get_blt() # produce a local version of a .beat
		bmt = get_bmt("UTC+1")

		time.sleep(0.5)

run_segment("CDT")


while True:
	os.system("clear")

	print("Local Time  : " + get_lst() + "  [ssm @" + str(ssm) + " stm @" + str(stm) + " spc: " + str(spc)  + "% spr: " + str(spr)  + "%]")
	print("Range Bar   : " + get_bar())
	print("              " + get_labels() + "\n")
	print("Earth Lumin : " + str(lum) + " (" + str(sel) + ")")
	print("Earth Time  : " + str(sat))

	print("\n\nWhere")
	print("- stm = Sectors til midnight      (.decond is a decimal second [0-100])")
	print("- ssm = Sectors since midnight    (.decond   = 1min:40s,  1,000d = 10m)")
	print("- spc = Segment percent completed (.range    = from 0 to 100%)")
	print("- spr = Segment percent remaining (.percent  = "+ str(float(36/10)*10) +"ds     1,000s = 16m)\n\n")
	#print("- sph = Sectors per standard hour (~" + str(sph) + " .sectors in an hour)")
	#print("- blt = Beats in Local time (.beat = 1min:25s, ~42 .beats in an hour)")
	#print("\nPERIOD = [N]ight [A]fternoon [M]orning [E]vening")
	#print("SS/SE  = [S]egment[S]tart [S]egment[E]nd\n\n")

	print("Sector Time [SRT]   (Duo:Percent:Period)  : " + str(sat))
	print("Sector Time [SEG]   (Oct:Dec:Dec:Period)  : " + str(sss))
	print("Sector Time [STD]   (Duo:Dec:Dec:Period)  : " + str(sst))

	#print("Sector Name                    (Latin)  : " + str(seg))
	print("Angle of Hedron            (Hour hand)    : " + str(hst) + "°")
	print("Angle of Sector          (Minute hand)    : " + str(hrd) + "°")
	print("Angle of Decond          (Second hand)    : " + str(hnd) + "°\n")

	print("Sector Beat              : @" + str(sbm).rjust(3, '0') + ".sectors (" + str(seg) + ")")

	if blt != 0:
		print("Locale Beat              : @" + str(blt) + ".beats   (" + str(get_ltz())  + ")")
	if bmt != 0:
		print("Global Beat              : @" + str(bmt) + ".beats   (BMT)")

	# Simulate a real clock display
	time.sleep(1)
