#!/usr/bin/env python

import os
import traceback
import webbrowser
try:
	# file_path = os.getcwd() # For testing
	file_path = os.path.dirname(__file__)	 # For click and run

	# MacOS
	chrome_path = r'open -a /Applications/Google\ Chrome.app %s'

	url = "http://localhost:8888/tree" + file_path.replace('\\','/').split('huangqiliang')[1]
	print(url)
	# url = "http://localhost:8888/notebooks" + file_path.replace('\\','/').split('huangqiliang')[1]
	# print(url)
	# os.system("start CHROME.EXE " + url)
	webbrowser.get(chrome_path).open(url)


except Exception as e:
	print(e)
	traceback.print_exc()
	import time
	time.sleep(10) 

