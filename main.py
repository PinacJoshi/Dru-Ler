import tor
import time
import multiprocessing as mp
#file: color.py
from color import printColor as pc
#file: session.py
from session import createSession as cs

def starttor():
  global torhash
  torhash = tor.gethash()
  tor.tor(torhash)

if __name__ == "__main__":

	subprocess_tor = mp.Process(target=starttor)
	subprocess_tor.start() #Starting Tor Proxy Subprocess

	while(not tor.checktorcon()): #Checking if Tor is Running
		time.sleep(0.5)

	pc("tor is up and running.","green")
	#starting a session
	session=cs()
	pc(session.get("https://check.torproject.org/api/ip").text,"bold")
	#add functionality down below
