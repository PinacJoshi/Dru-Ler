import tor
import time
import multiprocessing as mp

def starttor():
  global torhash
  torhash = tor.gethash()
  tor.tor(torhash)