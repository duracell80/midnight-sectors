#!/usr/bin/python3
# Author: Lee Jordan
# Github: Duracell80

import os, sys, logging

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
		return '{"result": 200, "status": "online", "ipaddr": "test"}'


