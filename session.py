#creates a session with tor as the proxy. ie. enables access to the deep web
import requests
def createSession():
    session=requests.session()
    session.proxies={'http':'socks5://127.0.0.1:9050','https':'socks5://127.0.0.1:9050'}
    return(session)
