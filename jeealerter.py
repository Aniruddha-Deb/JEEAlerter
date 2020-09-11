#!/usr/bin/python3

from playsound import playsound
import time
import sys
from time import sleep
from bs4 import BeautifulSoup
import requests

duration = 60
URL = "https://jeemain.nta.nic.in/webinfo/public/home.aspx"

prevct = None

if len(sys.argv) > 1:
	duration = int(sys.argv[1])

while True:
	resp = requests.get(URL);
	soup = BeautifulSoup(resp.text, "lxml")
	content = soup.find("div", {"class": "white_bg"})
	if prevct is not None and content != prevct:
		# compare containers of two pages
		print( "Two pages are not the same!! Difference at " + str([i for i in range(len(content.text)) if prevct.text[i] != content.text[i]]) )
		while True:
			playsound("beep-02.mp3")
			sleep(0.5)
	else:
		print("No updates to JEE Website at " + time.strftime("%H:%M:%S", time.localtime()));
		prevct = content
	sleep(duration)
