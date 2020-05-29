import socket
import machine
import time

led = machine.Pin(2, machine.Pin.OUT)
led.on()

def http_get(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    string = ""
    while True:
        data = s.recv(100)
        if data:
            string += str(data, 'utf8')
        else:
            break
    s.close()
    return string

def set_led():
    s = http_get('http://192.168.0.3/api/status')
    enabled = s[-5: -1] == 'true'
    if enabled:
        led.off()
    else:
        led.on()

def nerf():
    while True:
        set_led()
        time.sleep(0.1)