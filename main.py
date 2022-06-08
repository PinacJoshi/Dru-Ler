import tor
import time
import multiprocessing as mp
import threading
import signal
#file: color.py
from color import printColor as pc
#file: session.py
from session import createSession as cs

def starttor():
  global torhash
  torhash = tor.gethash()
  tor.tor(torhash)
process = mp.Process(target=starttor)

def handle(signal,frame):
	print("exiting gracefully")
	process.exit()


if __name__ == "__main__":

	process.start()
	signal.signal(signal.SIGINT,handle)
	listener = threading.Event()
	listener.wait()
	while(not tor.checktorcon()):
		pass
	pc("tor is up and running.","green")
	#starting a session
	session=cs()
	pc(session.get("https://check.torproject.org/api/ip").text,"bold")
	#add functionality down below
