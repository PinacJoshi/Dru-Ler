# Python 3.10.4
import requests
import os
import time

def main():
    os.system("sudo systemctl start docker")
    temp = os.popen("sudo docker run -it -p 9050:9050 -d dperson/torproxy").read()
    print("Launching Tor Proxy...")
    time.sleep(2)
    session = requests.session()
    session.proxies = {'http':  'socks5h://localhost:9050',
                       'https': 'socks5h://localhost:9050'}
    print(session.get('http://httpbin.org/ip').text) # prints {"origin": "67.205.146.164" }

    print(requests.get('http://httpbin.org/ip').text) # prints {"origin": "5.102.254.76" }

    print(session.get('http://galaxy3yrfbwlwo72q3v2wlyjinqr2vejgpkxb22ll5pcpuaxlnqjiid.onion/').text) # Prints the contents of the page

    os.system("sudo docker stop "+temp)

if(__name__ == "__main__"):
    main()