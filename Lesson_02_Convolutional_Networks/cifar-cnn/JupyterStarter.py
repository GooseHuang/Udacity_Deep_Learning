import os

try:
    url = "http://localhost:8888/notebooks" + \
            os.path.dirname(__file__).replace('\\', '/').split('Goose')[1]
    print(url)
    os.system('start CHROME.EXE "%s"' % url)


except Exception as e:
    print(e)
    import time
    time.sleep(10) 

