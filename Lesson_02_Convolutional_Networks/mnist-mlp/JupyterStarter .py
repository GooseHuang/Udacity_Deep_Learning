import os

try:
	# print(os.getcwd())
	# os.system("start CHROME.EXE " + "http://localhost:8889/notebooks" + os.getcwd().replace('\\','/').split('qiliang.huang')[1])

	url = "http://localhost:8888/notebooks" + os.path.dirname(__file__).replace('\\','/').split('Goose')[1]
	print(url)
	os.system("start CHROME.EXE " + url)


except Exception as e:
	print(e)
	import time
	time.sleep(10) 

