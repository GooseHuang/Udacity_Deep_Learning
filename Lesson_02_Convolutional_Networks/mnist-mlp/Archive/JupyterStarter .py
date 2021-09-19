import os
import traceback
import webbrowser
try:
	file_path = os.getcwd()

	# MacOS
	chrome_path = r'open -a /Applications/Google\ Chrome.app %s'

	file_path = os.getcwd()
	url = "http://localhost:8888/notebooks" + file_path.replace('\\','/').split('huangqiliang')[1]

	# url = "http://localhost:8888/notebooks" + file_path.replace('\\','/').split('huangqiliang')[1]
	# print(url)
	# os.system("start CHROME.EXE " + url)
	webbrowser.get(chrome_path).open(url)


except Exception as e:
	print(e)
	traceback.print_exc()
	import time
	time.sleep(10) 

