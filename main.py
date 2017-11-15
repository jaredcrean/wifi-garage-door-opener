import socket
import machine
import webrepl
import time
import network

#webrepl.start()

#HTML to send to browsers
html = """<!DOCTYPE html>
<html>
<head> <title>Wifi Garage Door Opener</title> </head>
<center><h2>Garage Door Opener</h2></center>
<form>
OPEN/CLOSE:
<button name="Open-Close" value="OFF0" type="submit">Open Garage Door</button><br><br>
</form>
</html>
"""

#Setup PINS
PIN1 = machine.Pin(5, machine.Pin.OUT)

#sta_if = network.WLAN(network.STA_IF)


#Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.240', 80))
s.listen(5)
while True:
    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    request = str(request)
    PINOFF1 = request.find('/?Open-Close=OFF0')
    if PINOFF1 == 6:
        print('TURN PIN1 OFF')
        PIN1.value(not PIN1.value()) # toggle
        time.sleep(1)
    response = html
    conn.send(response)
    conn.close()
