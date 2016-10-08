import socket

def get(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    res = ''
    while True:
        text = s.readline()
        while text != b'\r\n':
            print(text)
            text = s.readline()

        while text:
            res += str(text, 'utf8')
            text = s.readline()
        else:
            break
    return res
