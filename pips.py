#!/usr/bin/python3
# Author: Lee Jordan
# Github: Duracell80

import os, sys, subprocess, time, logging
from timeit import default_timer as timer
from datetime import datetime, timedelta

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

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
def speak_time(lang = "en", m = "The time will be", delta = 15, cmdline = False):
	message_go = False

	while int(message_go) == False:
		timegrab = datetime.today()
		rewinds  = timegrab + timedelta(seconds = delta)

		message_h = rewinds.strftime('%H')
		message_m = rewinds.strftime('%M')
		message_s = rewinds.strftime('%S')

		if(int(int(message_s) - delta) == 15):

			min_curr_message = "The current minute is " + str(int(message_m)).rjust(2, '0')
			logging.info(f"[i] {min_curr_message}")
			pips_play("single-short-low", cmdline)
			os.system(f'espeak -v {lang} -g 10 "{min_curr_message}"')

		if(int(int(message_s) - delta) == 30):

			min_next_message = "The next minute will be " + str(int(message_m) + 1).rjust(2, '0')
			logging.info(f"[i] {min_next_message}")
			pips_play("single-short-high", cmdline)
			os.system(f'espeak -v {lang} -g 10 "{min_next_message}"')

		if int(message_s) == 0:
			message_go = True
			message  = f"{m}, {message_h} hours, {message_m} minutes and {message_s} seconds, precisely"

			pips_play("single-short-low", cmdline)

			try:
				start = timer()
				os.system(f'espeak -v {lang} -g 10 "{message}"')
				pips_play("speakingclock", False)
				end = timer()
				delta = end - start
				logging.info(f"[i] {message} [{delta}]")

				break

			except:
				print("[i] espeak library missing?")

	return round(delta, 3)


def speak_clock(lang = 'en', m = "On the long stroke the time will be", x = 10, cmdline = False):
	m_1 = "the :00 second of the minute"
	m_2 = f"[i] Speaking clock is set to language: {lang} and will chime on {m_1}"

	if x == 0:
		i = -1; logging.info(f"{m_2} infinitely.")
	else:
		i = 0; logging.info(f"{m_2} for {x} repetitions.")

	while i < x:
		delta = 15;
		delta = speak_time(lang, m, delta, cmdline)

		logging.info(f"[i] Next time signal occurs on the stroke of {m_1} ...")
		time.sleep(0.15)
		if x > 0:
			i =+1


if import_safe("pysine", "0.9.2"):
	from pysine import sine

	def pips_beats(type = "gmt"):
		if type.lower() == "uk5" or type.lower() == "speakingclock":
			pips = [0.25, 0.25, 0.25, 0.25, 0.25]
			beat = [0.5]
			freq = "1000:1000"
			return pips, beat, freq

		elif type.lower() == "uk" or type.lower() == "uk6" or type.lower() == "nz":
                        pips = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]
                        beat = [0]
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
		elif type.lower() == "single-long":
			pips = [0.5]
			beat = [0]
			freq = "1000:1300"
		elif type.lower() == "single-short-high":
			pips = [0.15]
			beat = [0]
			freq = "1500:1600"
		elif type.lower() == "single-short-low":
			pips = [0.15]
			beat = [0]
			freq = "980:800"

		else:
			# Greenwhich Time Signal
			pips = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]
			beat = [0]
			freq = "1000:1300"

		return pips, beat, freq


	def pips_play(type = "gmt", cmdline = False):
		pips, beats, freq = pips_beats(type)
		freqs = freq.split(":")

		vdown = subprocess.check_call(["amixer", "-D", "pulse", "sset", "Master", "15%-"], stdout=subprocess.DEVNULL)
		start = timer()
		for i in range(len(pips)):
			if cmdline:
				subprocess.check_output('python3 -m pysine ' + str(freqs[0]) + ' ' + str(pips[i]), shell=True)
				time.sleep(abs(float(0.555-pips[i])))
			else:
				sine(frequency = float(freqs[0]), duration = pips[i]);
				time.sleep(abs(float(1-pips[i])))


		for i in range(len(beats)):
			if cmdline:
				subprocess.check_output('python3 -m pysine ' + str(freqs[0]) + ' ' + str(beats[i]), shell=True)
				time.sleep(abs(float(0.555-beats[i])))
			else:
				sine(frequency = float(freqs[1]), duration = beats[i]);
				#time.sleep(abs(float(1-beats[i])))

		end = timer(); delta = end - start
		vup = subprocess.check_call(["amixer", "-D", "pulse", "sset", "Master", "15%+"], stdout=subprocess.DEVNULL)

		logging.info(f"[i] Duration of the pips [{delta}]")

		return delta


#pips_play("gmt, False")

# language (espeak --help), message prepend,  number of loops (0 infinite), False = use python module, True = use command line call
speak_clock("en", "On the long stroke the time will be", 0, False)

#speak_time("en", "On the long stroke the time will be")
