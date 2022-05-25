import tor
import time
import multiprocessing as mp

def starttor():
  global torhash
  torhash = tor.gethash()
  tor.tor(torhash)


if __name__ == "__main__":

	process = mp.Process(target=starttor)
	process.start()
	while(not tor.checktorcon()):
		pass
	print("Tor is up and running")
