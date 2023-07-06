#!/usr/bin/python3
# Author: Lee Jordan
# Github: Duracell80

# An attempt at linking base 8 time to real time in a .beats style format with an astrological and cosmic twist

import os, sys, socket, time, math, json, requests

from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime
from dateutil import tz

global hn, ip, ea

hn = socket.gethostname()
ip = socket.gethostbyname(hn)
if ip == "127.0.1.1":
	ip = "127.0.0.1"
#ea = requests.get('https://checkip.amazonaws.com').text.strip()


def import_safe(m, v = "0.0.0"):
	import os, sys, logging

	if m.isnumeric():
		logging.error("Module parameters incorrect")
		sys.exit()
	try:
		__import__(m)
		result = True
	except ModuleNotFoundError:
		logging.error(f"Module not found: {m} ({v})")
		os.system(f"pip install {m}=={v}")
		result = True
	except:
		os.system(f"pip install {m}=={v}")
		result = True


	if result:
		return True
	else:
		sys.exit()



if import_safe("asyncio", "3.4.3"):
	import asyncio

if import_safe("schedule", "1.2.0"):
	import schedule



def background(f):
	def wrapped(*args, **kwargs):
		return asyncio.new_event_loop().run_in_executor(None, f, *args, **kwargs)

	return wrapped


if import_safe("pysinewave", "0.0.7"):
	from pysinewave import SineWave

	@background
	def pips():
		sinewave = SineWave(pitch = 23, decibels = -20)
		pips = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]
		# Run 60 seconds before and wait 55 seconds
		print(f"[i] Pips activated ...")
		time.sleep(55)
		for i in range(len(pips)):
			sinewave.play(); time.sleep(float(pips[i]))
			sinewave.stop(); time.sleep(float(1-pips[i]))






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
	return 100 * float(part / whole)

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
	return "LS 1 2 3 4 5 6 7 8 9 10AM/PM  2 3 4 5 6 7 8 9 10  LE"


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
		sector_l = "somnus"
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
		sector_l = "nocturnis"
	elif spc <= 100:
		sector_p = "N"
		sector_d = "Night"
		sector_l = "nox"
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
	sat_string_2 = "Hour:" + str(int(float(sector_hh))).rjust(2, '0') + "  (" + str(sector_hc).rjust(2, '0')  + "% complete)"
	sst_string = str(sector_hd) + ":" + str(sector_m) + "." + str(sector_s) + ":" + str(sector_d)
	sss_string = str("H" + str(sector_h) + ":" + str(sector_m) + "." + str(sector_s) + ":" + str(sector_p) + "ꝑ Segment[" + str(sector_q) + "] Period[" + str(sel) + "]")

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

		if dec <= 3:
			deg = 1
		elif dec <= 6:
			deg = 2
		elif dec <= 9:
			deg = 3
		elif dec <= 12:
			deg = 4
		elif dec <= 15:
			deg = 5
		elif dec <= 18:
			deg = 6
		elif dec <= 21:
			deg = 7
		elif dec <= 24:
			deg = 8
		elif dec <= 27:
			deg = 9
		elif dec <= 30:
			deg = 10
		elif dec <= 33:
			deg = 11
		elif dec <= 36:
			deg = 12

		dec_d = {
			"1": {
				"z": "aries",
				"1": "mars",
				"2": "sun",
				"3": "jupiter"
			},
			"2": {
				"z": "tarus",
                                "4": "venus",
                                "5": "mercury",
                                "6": "saturn"
                        },
			"3": {
				"z": "gemini",
                                "7": "mercury",
                                "8": "venus",
                                "9": "uranus"
                        },
			"4": {
				"z" : "cancer",
                                "10": "moon",
                                "11": "pluto",
                                "12": "neptune"
                        },
			"5": {
				"z" : "leo",
                                "13": "sun",
                                "14": "jupiter",
                                "15": "mars"
                        },
			"6": {
				"z" : "virgo",
                                "16": "mercury",
                                "17": "saturn",
                                "18": "venus"
                        },
			"7": {
				"z" : "libre",
                                "19": "venus",
                                "20": "uranus",
                                "21": "mercury"
                        },
			"8": {
				"z" : "scorpio",
                                "22": "pluto",
                                "23": "neptune",
                                "24": "moon"
                        },
			"9": {
				"z" : "sagittarius",
                                "25": "jupiter",
                                "26": "mars",
                                "27": "sun"
                        },
			"10": {
				"z" : "capricorn",
                                "28": "saturn",
                                "29": "venus",
                                "30": "mercury"
                        },
			"11": {
				"z" : "aquarius",
                                "31": "uranus",
                                "32": "mercury",
                                "33": "venus"
                        },
			"12": {
				"z" : "pisces",
                                "34": "neptune",
                                "35": "moon",
                                "36": "pluto"
                        }
		}
		zoo = dec_d[str(deg)]["z"]
		ele = dec_d[str(deg)][str(dec)]
		#zoo = "test"
		#ele = str(deg)
	else:
		zoo = "Sagittarius"
		ele = "Sun"
		dec = 0


	if mts:
		#rot = int(float((dec * 10) + mod)) # trip through 10 days
		rot = int(float(dec * 10))
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
	#ssm = get_ssm()
	#bld = float(1000 - 864)
	#blt = float(float(ssm) + bld)
	#blt = float(ssm)

	h, m, s = map(int, time.strftime("%H %M %S").split())
	blt = ((h * 3600) + (m * 60) + s) / 86.4

	if blt > 1000:
		blt = 0
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

	if beats > 999:
		beats = 999
	elif beats < 1:
		beats = 1
	elif beats < 0:
		beats = 0
	if beats > 997:
		bmt = str(format(float(beats), 0)).rjust(3, '0')
	else:
		bmt = str(format(float(beats - 0.5), 0)).rjust(3, '0')
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
def server_api(port = "3633"):
	os.system("uvicorn api:app --host 127.0.0.1 --port " + port)


@background
def run_segment(when = "now"):
	global iso, soi, pkd, mts, msm, mat1, mpc, zoo, ele, rot, dec, tz_mar, hst, hnd, hrd, sss, ssm, stm, sbm, sst, sat1, sat2, spc, spr, sph, spd, seg, sel, blt, bmt, bmr, lum, sol
	iso  = [1, 24, 1440, 86400, 864] # Clocks on Earth
	soi  = [1, 24, 1440, 88775, 888] # Clocks on Mars ... 8*3 = 24, 8 and a bit hedrons (8 hour day with 4 periods, (or 16, also with 4 periods))

	dir_home = os.path.expanduser('~')

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
	ele  = "Earth"
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
	zoo  = "Sagittarius"
	tz_mar = ""

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

		if mts:
			tz_mar = "MTS" # Mars Time Slip
		else:
			tz_mar = "MTC" # Mars Coordinated Time


		jsn_d = {
			"local_time": str(get_lst()),
			"local_timezone": str(get_ltz()),
			"local_time_srt": str(sat1).replace("\ua751", ""),
			"local_time_seg": str(sss).replace("\ua751", ""),
			"local_time_sst": str(sst),
			"local_angle_hedron": float(hst),
			"local_angle_sector": float(hrd),
			"local_angle_decond": float(hnd),
			"local_beat_sector": str(sbm).rjust(3, '0'),
			"local_beat_locale": str(blt).rjust(3, '0'),
			"local_beat_global": str(bmt).rjust(3, '0'),
			"local_ssm": str(ssm).rjust(3, '0'),
			"local_stm": str(stm).rjust(3, '0'),
			"local_lum_elapsed": int(spc),
			"local_lum_remaining": int(spr),
			"local_lum_name": str(lum).lower(),
			"local_lum_period": str(sel).lower(),
			"local_lum_segment": str(seg).lower(),
			"mars_time": str(mat1).replace("\ua751", ""),
			"mars_timezone": str(tz_mar),
			"mars_sol_elapsed": mpc,
			"mars_beat": str(bmr).rjust(3, '0'),
			"mars_ts_active": mts,
			"mars_ts_angle": float(rot),
			"mars_ts_decan": int(dec),
			"mars_ts_planet": str(ele).lower(),
			"mars_ts_zodiac": str(zoo).lower(),
		}

		jsn_o = json.dumps(jsn_d, indent=4)
		with open(dir_home + "/.local/share/midnight-sectors.json", "w") as jsn_f:
			jsn_f.write(jsn_o)

		os.system("clear")

		print(f"Local Time  : {get_lst()} [ssm @ {ssm} stm @ {stm} lpc: {spc}% lpr: {spr}%]")
		print(f"Range Bar   : {get_bar()}")
		print(f"              {get_labels()}")
		print(f"")
		print(f"Earth Lumin : (lum: {lum}) (period: {sel}) (segment: {seg})")
		print(f"Earth Time  : {sat1}")

		if mts:
			print(f"⋅Mars Time  : {mat1} Time-Slip Active ({str(rot).rjust(3, '0')}°) (decan {str(dec).rjust(2, '0')}: {ele} in {zoo})")
			xs = 0
			ds = ""
			while xs <= int(dec)-1:
				ds+="•"
				xs+=1
			print(f" Decan Line : {ds}")
			print("\n")
		else:
			print(f"⋅Mars Time  : {mat1}")
			print("\n\n")

		print(f"Sector Time [SRT]   (Sec:Percent:Period)  : {sat1}    {sat2}")
		print(f"Sector Time [SEG]   (Oct:Dec:Dec:Period)  : {sss}")
		print(f"Sector Time [STD]   (Sec:Dec:Dec:Period)  : {sst}")

		print(f"Angle of Hedron              (Hour hand)  : {hst}°")
		print(f"Angle of Sector            (Minute hand)  : {hrd}°")
		print(f"Angle of Decond            (Second hand)  : {hnd}°")

		print("\n")

		print(f"MarSol Beat        [Sol Complete = {str(mpc).rjust(3, '0')}%]  : @{bmr}.sectors ({tz_mar})")
		print(f"Sector Beat        [Lum Complete = {str(spc).rjust(3, '0')}%]  : @{str(sbm).rjust(3, '0')}.sectors (SMT)")

		if blt != 0:
			print(f"Locale Beat                        (Dec)  : @{blt}.beats   ({get_ltz()})")
		if bmt != 0:
			print(f"Global Beat                        (Dec)  : @{bmt}.beats   (BMT)")

		print(f"\n\nAPI: {ip}:3633/docs\nWEB: {ip}:3636")

		schedule.run_pending()
		time.sleep(1)

schedule.every().day.at("23:59").do(pips)
schedule.every().day.at("11:59").do(pips)


run_segment("CDT"); server_api("3633")
webhost = "localhost"; webport = 3636

def read_file(path):
	try:
		with open(path) as f:
			file = f.read()
	except Exception as e:
		file = e
	return file


def serve_data(self):
	file = read_file("/home/lee/.local/share/midnight-sectors.json")
	self.send_response(200, "OK")
	self.end_headers()
	self.wfile.write(bytes(file, "utf-8"))


class WebServer(BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path == '/data':
			serve_data(self)
		else:
			self.send_response(200)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
			self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
			self.wfile.write(bytes("<body>", "utf-8"))
			self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
			self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":
	webserver = HTTPServer((webhost, webport), WebServer)
	print("Server started http://%s:%s" % (webhost, webport))

	try:
		webserver.serve_forever()
	except KeyboardInterrupt:
		pass

	webserver.server_close()
	print("Server stopped.")
