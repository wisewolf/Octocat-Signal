
import socket
import ure

def get(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    res = ''
    while True:
        text = s.readline()
        print(text)

        if text:
            r = ure.search('\"type\":[ ]*\"([A-Za-z]+)', text)
            if r:
                return r.group(1)
        if not text:
            return 0;