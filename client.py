
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

        if text[7:11] == b'type':
            return re.search('\"type\": \"([A-Za-z]+)', s).group(1)
        if not text:
            return 0;