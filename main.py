#!/usr/bin/python3
# Author: Lee Jordan
# Github: Duracell80

# An attempt at linking base 8 time to real time in a .beats style format

import os, sys, time, math

from datetime import datetime
from dateutil import tz

try:
	import asyncio
except:
	os.system("pip install asyncio==3.4.3")

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

def percentage(part, whole):
	return 100 * float(part)/float(whole)

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

# Sectors elapsed in this segment
def get_mpc():
	return int(round(scale(int(iso[4]), 0, float(msm)),0))


# Sectors remaining in this segment
def get_spr():
	spc = get_spc()
	return int(abs(100-spc))

# Sectors since midnight on Earth
def get_ssm():
	now = datetime.now()
	ssm = format(float(((now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()/100)), 2)
	ssm = str(ssm).rjust(3, '0')
	return ssm

# Sectors since midnight on Mars
def get_msm():
	now = datetime.now()
	mss = format(float(((((now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()) - (soi[3] - iso[3])) / 100)),2)
	#msm = float(mss) - float(percentage(2.75, float(mss)))
	if pkd:
		# Introduce the time slip (frozen time for about 40 Standard Earth Minutes)
		if float(mss) < 0:
			mss = 0
			mts = True
		return mss, mts
	else:
		# Introduce the time skip (double the midnight sectors on Earth up to the first 24)
		if float(ssm) <= 23.70:
			mss = float(ssm) * 1.5
			mts = True
		else:
			mss = float(ssm) + 12
			mts = False
		return mss, mts


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

	if spc > 100:
		spc = 100

	if spc <= 22:
		sector_p = "N"
		sector_d = "Night"
		sector_l = "nox"
	elif spc <= 50:
		sector_p = "M"
		sector_d = "Morning"
		sector_l = "antemeridies"
	elif spc <= 72:
		sector_p = "A"
		sector_d = "Afternoon"
		sector_l = "post meridiem"
	elif spc <= 82:
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
		decond = "."
		period = str(sector_p)

	sector_hh = round(float((float(ssm) / 3.6) / 10),2)
	sector_hb = str(sector_hh).split(".")

	sector_hc = str(sector_hb[1]).rjust(2, '0')

	sector_hd = str(sector_hb[0]).rjust(2, '0')
	sector_hs = str(int(sector_hb[0]) - 12).rjust(2, '0')
	if int(sector_hb[0]) >= 13:
		sector_ht = str(int(sector_hb[0]) - 12).rjust(2, '0')
	else:
		sector_ht = str(int(sector_hb[0])).rjust(2, '0')


	if str(sector_hb[1])[0] == 0:
		sector_hc = str(sector_hb[1]).rjust(2, '0')
	else:
		sector_hc = str(sector_hb[1]).ljust(2, '0')


	sat_string_1 = str(sector_ht) + "." + str(sector_hc) + ":" + str(sector_p) + "ꝑ"
	sat_string_2 = "Hour:" + str(int(float(sector_hh))).rjust(2, '0') + " (" + str(sector_hc).rjust(2, '0')  + "% complete)"
	sst_string = str(sector_hd) + ":" + str(sector_m) + "." + str(sector_s) + ":" + str(sector_d)
	sss_string = str("H" + str(sector_h) + ":" + str(sector_m) + "." + str(sector_s) + ":" + str(sector_p) + "ꝑ Segment[" + str(sector_q) + "] Period[" + str(sector_p) + "]")

	return sst_string, sat_string_1, sat_string_2, sss_string, sel_string

# Track Mars time similar to Earth
def get_mst():
	mst             = float(float(msm) / 100)
	mlice           = str(mst).replace(".", ":").split(":")

	mpc = get_mpc()
	if int(mpc) > 100:
		mpc = 100

	if int(mpc) <= 22:
		mector_p = "N"
	elif int(mpc) <= 50:
                mector_p = "M"
	elif int(mpc) <= 75:
		mector_p = "A"
	elif int(mpc) <= 85:
		mector_p = "E"
	elif int(mpc) <= 100:
		mector_p = "N"
	else:
		mector_p = "N"


	mector_h = mlice[0]
	mector_m = str(mlice[1][0:2]).rjust(2, '0')
	mector_s = str(mlice[1][2:4])


	if int(mector_m) <= 25:
		mector_q = str(int(mector_h)) + ".25"
	elif int(mector_m) <= 50:
		mector_q = str(int(mector_h)) + ".50"
	elif int(mector_m) <= 75:
		mector_q = str(int(mector_h)) + ".75"
	elif int(mector_m) <= 99:
		mector_q = str(int(mector_h)) + ".75"
	else:
		mector_q = str(int(mector_h)) + ".00"


	mector_hh = round(float((float(msm) / 3.6) / 10),2)
	mector_hb = str(mector_hh).split(".")


	if str(mector_hb[1])[0] == 0:
		mector_hc = str(mector_hb[1]).rjust(2, '0')
	else:
		mector_hc = str(mector_hb[1]).ljust(2, '0')

	if int(mector_hb[0]) >= 13:
		mector_ht = str(int(mector_hb[0]) - 12).rjust(2, '0')
	else:
		mector_ht = str(int(mector_hb[0])).rjust(2, '0')

	if mts:
		mector_p = "S"
		mector_ht = "T%"
		dec = int(bmr) + 1
		if dec > 36:
			dec = 36
		ele = ""

		if dec <= 3:
			zoo = "Aries"
			if dec == 1:
				ele = "Mars"
				mod = 3.3
			if dec == 2:
				ele = "Sun"
				mod = 6.6
			if dec == 3:
				ele = "Jupiter"
				mod = 9.9
		elif dec <=6:
			zoo = "Tarus"
			if dec == 4:
				ele = "Venus"
				mod = 3.3
			if dec == 5:
				ele = "Mercury"
				mod = 6.6
			if dec == 6:
				ele = "Saturn"
				mod = 9.9
		elif dec <=9:
			zoo = "Gemini"
			if dec == 7:
				ele = "Mercury"
				mod = 3.3
			if dec == 8:
				ele = "Venus"
				mod = 6.6
			if dec == 9:
				ele = "Uranus"
				mod = 9.9
		elif dec <=12:
			zoo = "Cancer"
			if dec == 10:
				ele = "Moon"
				mod = 3.3
			if dec == 11:
				ele = "Pluto"
				mod = 6.6
			if dec == 12:
				ele = "Neptune"
				mod = 9.9
		elif dec <=15:
			zoo = "Leo"
			if dec == 13:
				ele = "Sun"
				mod = 3.3
			if dec == 14:
				ele = "Jupiter"
				mod = 6.6
			if dec == 15:
				ele = "Mars"
				mod = 9.9
		elif dec <=18:
			zoo = "Virgo"
			if dec == 16:
				ele = "Mercury"
				mod = 3.3
			if dec == 17:
				ele = "Saturn"
				mod = 6.6
			if dec == 18:
				ele = "Venus"
				mod = 9.9
		elif dec <=21:
			zoo = "Libra"
			if dec == 19:
				ele = "Venus"
				mod = 3.3
			if dec == 20:
				ele = "Uranus"
				mod = 6.6
			if dec == 21:
				ele = "Mercury"
				mod = 9.9
		elif dec <=24:
			zoo = "Scorpio"
			if dec == 22:
				ele = "Pluto"
				mod = 3.3
			if dec == 23:
				ele = "Neptune"
				mod = 6.6
			if dec == 24:
				ele = "Moon"
				mod = 9.9
		elif dec <=27:
			zoo = "Sagittarius"
			if dec == 25:
				ele = "Jupiter"
				mod = 3.3
			if dec == 26:
				ele = "Mars"
				mod = 6.6
			if dec == 27:
				ele = "Sun"
				mod = 9.9
		elif dec <=30:
			zoo = "Capricorn"
			if dec == 28:
				ele = "Saturn"
				mod = 3.3
			if dec == 29:
				ele = "Venus"
				mod = 6.6
			if dec == 30:
				ele = "Mercury"
				mod = 9.9
		elif dec <=33:
			zoo = "Aquarius"
			if dec == 31:
				ele = "Uranus"
				mod = 3.3
			if dec == 32:
				ele = "Mercury"
				mod = 6.6
			if dec == 33:
				ele = "Venus"
				mod = 9.9
		elif dec <=36:
			zoo = "Pisces"
			if dec == 34:
				ele = "Neptune"
				mod = 3.3
			if dec == 35:
				ele = "Moon"
				mod = 6.6
			if dec == 36:
				ele = "Pluto"
				mod = 9.9
		else:
			zoo = ""
			ele = ""

	else:
		zoo = ""
		ele = ""
		dec = 0


	if mts:
		#rot = int(round((int(mpc) / 100) * 360 , 0))
		rot = int(float((dec * 10) + mod))
	else:
		rot = 0

	if rot > 360:
		rot = 360

	mat_string_1 = str(mector_ht) + "." + str(mector_hc) + ":" + str(mector_p) + "ꝑ"

	return mat_string_1, mpc, zoo.lower(), ele.lower(), rot, dec

def get_tick():
	ssm = str(get_ssm()).split(".")
	tic = ssm[1]
	return tic

def get_seg():
	if float(ssm) <= 100:
		seg = "venti" # every lux (day) should start with a coffee
	elif float(ssm) <= 200:
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

# Define mars time in beats
def get_bmr():
	msm, mts = get_msm()
	#mld = float(1000 - 888)
	mld = 0
	mlt = float(float(msm) + mld)

	return str(format(float(mlt),0)).rjust(3, '0'), mts, msm


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
	global iso, soi, pkd, mts, msm, mat1, mpc, zoo, ele, rot, dec, hst, hnd, hrd, sss, ssm, stm, sbm, sst, sat1, sat2, spc, spr, sph, spd, seg, sel, blt, bmt, bmr, lum, sol
	iso  = [1, 24, 1440, 86400, 864] # Clocks on Earth
	soi  = [1, 24, 1440, 88775, 888] # Clocks on Mars ... 8*3 = 24, 8 and a bit hedrons (8 hour day with 4 periods, (or 16, also with 4 periods))
	hst  = 0
	hnd  = 0
	hrd  = 0
	bmt  = 0
	blt  = 0
	bmr  = 0
	sbm  = 0
	stm  = 0
	spc  = 0
	spr  = 0
	ele  = ""
	sss  = "S1:00:00"
	sst  = "00:00"
	sat1 = "00:00"
	sat2 = ""
	mat1 = "00:00"
	seg  = "unus"
	sel  = "nox"
	lum  = get_lum()

	# Set to True to introduce Phillip K Dick's Martian Time Slip
	pkd  = False
	mts  = False # Keep track of status of the Time Slip
	msm  = 0
	mpc  = 0
	rot  = 0
	dec  = 0
	zoo  = ""

	while True:
		ssm = get_ssm() # sectors since midnight on Earth
		hst = get_first_hand()
		hnd = get_second_hand()
		hrd = get_third_hand()

		stm = get_stm() # sectors to midnight on Earth
		sph = get_sph() # sectors per hour on Earth
		spc = get_spc() # progress through the sector as completed percentage on Earth
		spr = get_spr() # sectors remaining this segment as percentage to be completed on Earth
		sst, sat1, sat2, sss, sel = get_sst() # Get [S]tandard [S]ector [T]ime on Earth
		sbm = math.trunc(float(ssm))
		seg = get_seg()

		blt = get_blt() # produce a local version of a .beat on Earth
		bmt = get_bmt("UTC+1")

		bmr, mts, msm = get_bmr()
		mat1, mpc, zoo, ele, rot, dec = get_mst()

		time.sleep(0.5)

run_segment("CDT")


while True:
	os.system("clear")

	print("Local Time  : " + get_lst() + "  [ssm @" + str(ssm) + " stm @" + str(stm) + " lpc: " + str(spc)  + "% lpr: " + str(spr)  + "%]")
	print("Range Bar   : " + get_bar())
	print("              " + get_labels() + "\n")
	print("Earth Lumin : (lum: " + str(lum) + ") (period: " + str(sel) + ") (segment: " + str(seg) + ")")
	print("Earth Time  : " + str(sat1))

	if mts:
		print("⋅Mars Time  : " + str(mat1) + " Time-Slip Active (" + str(rot) + "°) (decan " + str(int(dec)).rjust(2, '0') + " : " + str(ele) + " in " + str(zoo) + ")")
		tz_mar = "MTS" # Mars Time Slip
	else:
		tz_mar = "MTC" # Mars Coordinated Time
		print("⋅Mars Time  : " + str(mat1))

	print("\n\n")
	#print("Where")
	#print("- stm = Sectors til midnight      (.sector   = decimal minute of an 8 hour day)")
	#print("- ssm = Sectors since midnight    (.decond   = 1min:40s,  1,000d = 10m)")
	#print("- lpc = Lumin percent completed   (.range    = from 0 to 100%)")
	#print("- lpr = Lumin percent remaining   (.percent  = "+ str(float(36/10)*10) +"ds     1,000s = 16m)\n\n")
	#print("- sph = Sectors per standard hour (~" + str(sph) + " .sectors in an hour)")
	#print("- blt = Beats in Local time (.beat = 1min:25s, ~42 .beats in an hour)")
	#print("\nPERIOD = [N]ight [A]fternoon [M]orning [E]vening")
	#print("SS/SE  = [S]egment[S]tart [S]egment[E]nd\n\n")

	print("Sector Time [SRT]   (Duo:Percent:Period)  : " + str(sat1) + "     " + str(sat2))
	print("Sector Time [SEG]   (Oct:Dec:Dec:Period)  : " + str(sss))
	print("Sector Time [STD]   (Duo:Dec:Dec:Period)  : " + str(sst))

	#print("Sector Name                    (Latin)  : " + str(seg))
	print("Angle of Hedron              (Hour hand)  : " + str(hst) + "°")
	print("Angle of Sector            (Minute hand)  : " + str(hrd) + "°")
	print("Angle of Decond            (Second hand)  : " + str(hnd) + "°\n")

	print("MarSol Beat        [Sol Complete = "+str(mpc).rjust(3, '0')+"%]  : @" + str(bmr) + ".sectors (" + str(tz_mar) + ")") # Time on Mars
	print("Sector Beat        [Lux Complete = "+str(spc).rjust(3, '0')+"%]  : @" + str(sbm).rjust(3, '0') + ".sectors (SMT)")

	if blt != 0:
		print("Locale Beat                               : @" + str(blt) + ".beats   (" + str(get_ltz())  + ")")
	if bmt != 0:
		print("Global Beat                               : @" + str(bmt) + ".beats   (BMT)")


	# Simulate a real clock display
	time.sleep(1)
