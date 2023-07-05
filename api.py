#!/usr/bin/python3
# Author: Lee Jordan
# Github: Duracell80

import os, sys, logging, socket, requests
global hn, ip, ea

hn = socket.gethostname()
ip = socket.gethostbyname(hn)
if ip == "127.0.1.1":
	ip = "127.0.0.1"
ea = requests.get('https://checkip.amazonaws.com').text.strip()

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


if import_safe("fastapi", "0.97.0"):
	from fastapi import FastAPI, Depends

	app = FastAPI()

	@app.get("/v1/status", status_code=200)
	async def status():
		return '{"result": 200, "status": "online", "ip_int": "'+ ip +'", "ip_ext": "'+ ea +'"}'


