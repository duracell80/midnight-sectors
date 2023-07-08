#!/usr/bin/python3
# Author: Lee Jordan
# Github: Duracell80

import os, sys, subprocess, time, logging
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
def speak_time(lang = "en", delta = 15, cmdline = False):
	message_go = False

	while int(message_go) == False:
		timegrab = datetime.today()
		rewinds  = timegrab + timedelta(seconds = delta)

		message_h = rewinds.strftime('%H')
		message_m = rewinds.strftime('%M')
		message_s = rewinds.strftime('%S')

		if(int(int(message_s) - delta) == 15):
                        #pips_play("single-short-high", cmdline)
			os.system(f'espeak -v {lang} -g 10 "{message_m}"')
		if(int(int(message_s) - delta) == 30):
			#pips_play("single-short-high", cmdline)
			os.system(f'espeak -v {lang} -g 10 "{str(int(message_m) + 1)}"')

		if int(message_s) == 0:
			message_go = True
			message  = f"On the long stroke the time will be, {message_h} hours, {message_m} minutes and {message_s} seconds, precisely"

			pips_play("single-short", cmdline)

			try:
				start = timer()
				os.system(f'espeak -v {lang} -g 10 "{message}"')
				pips_play("speakingclock")
				end = timer()
				delta = end - start
				print(f"[i] {message} [{delta}]")

				break

			except:
				print("[i] espeak library missing?")

	return round(delta, 3)


def speaking_clock(lang = 'en', x = 10, cmdline = False):
	m_1 = "the :00 second of the minute"
	m_2 = f"[i] Speaking clock is set to language: {lang} and will chime on {m_1}"

	if x == 0:
		i = -1; print(f"{m_2} infinitely.")
	else:
		i = 0; print(f"{m_2} for {x} repetitions.")

	while i < x:
		delta = 15;
		delta = speak_time(lang, delta, cmdline)

		print(f"[i] Next time signal occurs on the stroke of {m_1} ...")
		time.sleep(0.25)
		if x > 0:
			i =+1


if import_safe("pysine", "0.9.2"):
	from pysine import sine

	def pips_beats(type = "gmt"):
		if type.lower() == "uk" or type.lower() == "uk6" or type.lower() == "nz":
			pips = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]
			beat = [0]
			freq = "1000:1300"
		elif type.lower() == "uk5" or type.lower() == "speakingclock":
			pips = [0.25, 0.25, 0.25, 0.25, 0.25]
			beat = [0.5]
			freq = "1000:1300"
		elif type.lower() == "ire":
			pips = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
			beat = [0]
			freq = "1000:1300"
		elif type.lower() == "aus":
			pips = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
			beat = [0]
			freq = "1000:1300"
		elif type.lower() == "chi":
			pips = [0.25, 0.25, 0.25, 0.25, 0.25]
			beat = [0.5]
			freq = "800:1600"
		elif type.lower() == "hk":
			pips = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
			beat = [0]
			freq = "1000:1300"
		elif type.lower() == "ind":
			pips = [0.15, 0.15, 0.15, 0.15, 0.15, 0.15]
			beat = [0]
			freq = "1000:1300"
		elif type.lower() == "isr":
			pips = [0.1, 0.1, 0.1, 0.1, 0.1]
			beat = [1]
			freq = "1100:1100"
		elif type.lower() == "bra":
			pips = [0.15, 0.15, 0.15]
			beat = [0.15]
			freq = "920:1360"
		elif type.lower() == "spa":
			pips = [0.15, 0.15]
			beat = [0.25, 0.25]
			freq = "1000:800"
		elif type.lower() == "ita":
			pips = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
			beat = [0]
			freq = "1000:1300"
		elif type.lower() == "ger":
			pips = [0.15, 0.15, 0.5]
			beat = [0]
			freq = "1200:1200"
		elif type.lower() == "jap":
			pips = [0.1, 0.1, 0.1]
			beat = [3]
			freq = "1000:1500"
		elif type.lower() == "usa":
			pips = [1]
			beat = [0]
			freq = "1000:1300"
		elif type.lower() == "rom":
			pips = [0.05, 0.15, 0.05, 0.15, 0.05, 0.15, 0.05, 0.15, 0.05, 0.15, 0.05, 0.15, 0.05, 0.15, 0.05, 0.5]
			beat = [0]
			freq = "1000:1300"
		elif type.lower() == "slo":
			pips = [0.05, 0.05, 0.05, 0.05, 0.05]
			beat = [0.05]
			freq = "900:1800"
		elif type.lower() == "single-short":
			pips = [0.5]
			beat = [0]
			freq = "1000:1300"
		elif type.lower() == "single-short-high":
			pips = [0.25]
			beat = [0]
			freq = "1500:1600"
		else:
			# Greenwhich Time Signal
			pips = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]
			beat = [0]
			freq = "1000:1300"

		return pips, beat, freq


	def pips_play(type = "gmt", cmdline = False):
		pips, beats, freq = pips_beats(type)
		freqs = freq.split(":")

		subprocess.call(["amixer", "-D", "pulse", "sset", "Master", "15%-"])
		start = timer()
		for i in range(len(pips)):
			if cmdline:
				subprocess.check_output('python3 -m pysine ' + str(freqs[0]) + ' ' + str(pips[i]), shell=True)
				time.sleep(abs(float(0.555-pips[i])))
			else:
				sine(frequency = float(freqs[0]), duration = pips[i]);
				time.sleep(abs(float(1-pips[i])))


		for i in range(len(beats)):
			subprocess.check_output('python3 -m pysine ' + str(freqs[1]) + ' ' + str(beats[i]), shell=True)
			time.sleep(abs(float(0.555-pips[i])))

		end = timer(); delta = end - start
		subprocess.call(["amixer", "-D", "pulse", "sset", "Master", "15%+"])
		#print(f"[i] Duration of pips [{delta}]")

		return delta


#pips_play("gmt, False")

# language (espeak --help) number of loops (0 infinite), False = use python module, True = use command line call
speaking_clock('en', 0, False)
