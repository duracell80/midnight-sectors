#!/usr/bin/python3
# Author: Lee Jordan
# Github: Duracell80

import os, sys, time, logging
from timeit import default_timer as timer
from datetime import datetime, timedelta

def import_safe(m, v = "0.0.0"):
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


# https://www.sitepoint.com/talking-clock-birth-voice-based-ui
def speak_time(lang = "en", delta = 12):
	timegrab = datetime.today()
	rewinds  = timegrab + timedelta(seconds = delta)

	message_h = rewinds.strftime('%H')
	message_m = rewinds.strftime('%M')
	message_s = rewinds.strftime('%S')


	message  = f"At the third stroke the time will be, {message_h} hours, {message_m} minutes and {message_s} seconds, precisely"

	try:
		start = timer()
		os.system(f'espeak -v {lang} -g 10 "{message}"')
		pips("uk3")
		end = timer()
		delta = end - start
		print(f"[i] {message} [{delta}]")

	except:
		print("[i] espeak library missing?")

	return round(delta, 3)


def speaking_clock(lang = 'en', x = 10, w = 15):
	i = 0
	while i < x:
		delta = 12; delta = speak_time(lang, delta)
		print(f"[i] Next time signal in {w} seconds ...")
		time.sleep(w)
		i =+1



if import_safe("pysinewave", "0.0.7"):
	from pysinewave import SineWave

	def pips(type = "gmt"):
		if type.lower() == "uk" or type.lower() == "nz":
			sinewave = SineWave(pitch = 23, decibels = -20)
			pips = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]
		if type.lower() == "uk3" or type.lower() == "nz":
			sinewave = SineWave(pitch = 31, decibels = -20)
			pips = [0.15, 0.15, 0.5]
		elif type.lower() == "ire":
			sinewave = SineWave(pitch = 23, decibels = -20)
			pips = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
		elif type.lower() == "aus":
			sinewave = SineWave(pitch = 18, decibels = -20)
			pips = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
		elif type.lower() == "chi":
			sinewave = SineWave(pitch = 26, decibels = -20)
			pips = [0.25, 0.25, 0.25, 0.25, 0.25]
		elif type.lower() == "hk":
			sinewave = SineWave(pitch = 23, decibels = -20)
			pips = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
		elif type.lower() == "ind":
			sinewave = SineWave(pitch = 29, decibels = -20)
			pips = [0.15, 0.15, 0.15, 0.15, 0.15, 0.15]
		elif type.lower() == "bra":
			sinewave = SineWave(pitch = 22, decibels = -20)
			pips = [0.15, 0.15, 0.15]
		elif type.lower() == "spa":
			sinewave = SineWave(pitch = 21, decibels = -20)
			pips = [0.15, 0.15]
		elif type.lower() == "ita":
			sinewave = SineWave(pitch = 29, decibels = -20)
			pips = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
		elif type.lower() == "ger":
			sinewave = SineWave(pitch = 18, decibels = -20)
			pips = [0.15, 0.15, 0.5]
		elif type.lower() == "jap":
			sinewave = SineWave(pitch = 27, decibels = -20)
			pips = [0.15, 0.15, 0.15]
		elif type.lower() == "usa":
			sinewave = SineWave(pitch = 12, decibels = -20)
			pips = [1]
		elif type.lower() == "nbc":
			sinewave = SineWave(pitch = 25, decibels = -20)
			pips = [0.5]
		elif type.lower() == "rom":
			sinewave = SineWave(pitch = 22, decibels = -20)
			pips = [0.05, 0.15, 0.05, 0.15, 0.05, 0.15, 0.05, 0.15, 0.05, 0.15, 0.05, 0.15, 0.05, 0.15, 0.05, 0.5]
		elif type.lower() == "slo":
			sinewave = SineWave(pitch = 22, decibels = -20)
			pips = [0.05, 0.05, 0.05, 0.05, 0.05]

		else:
			# GMT
			sinewave = SineWave(pitch = 23, decibels = -20)
			pips = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]

		# Run 60 seconds before and wait 55 seconds
		#print(f"[i] Pips activated ...")
		#time.sleep(55)
		for i in range(len(pips)):
			sinewave.play(); time.sleep(float(pips[i]))
			sinewave.stop(); time.sleep(abs(float(1-pips[i])))

		if type == "chi":
			sinewave = SineWave(pitch = 30, decibels = -20)
			sinewave.play(); time.sleep(0.5)
			sinewave.stop()
		if type == "bra":
			sinewave = SineWave(pitch = 23, decibels = -20)
			sinewave.play(); time.sleep(0.25)
			sinewave.stop()
		if type == "spa":
			sinewave = SineWave(pitch = 23, decibels = -20)
			sinewave.play(); time.sleep(0.25)
			sinewave.stop(); time.sleep(0.25)
			sinewave.play(); time.sleep(0.25)
			sinewave.stop()
		if type == "slo":
			sinewave = SineWave(pitch = 32, decibels = -40)
			sinewave.play(); time.sleep(0.05)
			sinewave.stop()

		if type == "jap":
			sinewave = SineWave(pitch = 30, decibels = -40)
			sinewave.play(); time.sleep(3)
			sinewave.stop()
pips("uk")

# language as seen in espeak eg en-sc, number of loops, seconds between each reading
speaking_clock('en', 10, 15)
