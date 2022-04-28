# Python 3.10.4
import requests

def main():
    import requests
    session = requests.session()
    session.proxies = {'http':  'socks5h://localhost:9050',
                       'https': 'socks5h://localhost:9050'}
    print(session.get('http://httpbin.org/ip').text) # prints {"origin": "67.205.146.164" }

    print(requests.get('http://httpbin.org/ip').text) # prints {"origin": "5.102.254.76" }

    print(session.get('http://http://torchdeedp3i2jigzjdmfpn5ttjhthh5wbmda2rr3jvqjg5p77c54dqd.onion/').text) # Prints the contents of the page


if(__name__ == "__main__"):
    main()