import os

def checktorcon(): #Used to check current status of tor and return boolean
    connection = len((os.popen("curl --socks5 localhost:9050 --socks5-hostname localhost:9050 -s  https://check.torproject.org/api/ip")).read())
    if connection > 0:
        return True
    else:
        return False

def modprint(out): #Use this function later to print with timestamp and current action
    print(out)

def gethash():
    modprint("Generating Hash")
    return (os.popen("tor --hash-password test | grep -e 16: | grep -x '.\{61\}'")).read().strip()

def gettorusername():    
    return (os.popen("compgen -u | grep -e tor | grep -wv operator")).read().strip()

def tor(torhash):
    modprint("Getting Tor Username")
    toruser = gettorusername()

    s1, s2, s3, s4 = "sudo -u",toruser,"tor --ControlPort 9051 --HashedControlPassword",torhash
    torcmd = ('%s %s %s %s' % (s1,s2,s3,s4)).strip()
    modprint("Starting Tor Proxy")

    os.system(torcmd)