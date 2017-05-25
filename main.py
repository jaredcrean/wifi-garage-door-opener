import socket
import machine
import webrepl
import time

webrepl.start()

#HTML to send to browsers
html = """<!DOCTYPE html>
<html>
<head> <title>ESP8266 LED ON/OFF</title> </head>
<center><h2>Garage Door Opener</h2></center>
<form>
LED0:
<button name="LED" value="OFF0" type="submit">Open Garage Door</button><br><br>
</form>
</html>
"""

#Setup PINS
LED0 = machine.Pin(5, machine.Pin.OUT)

#Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
while True:
    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    request = str(request)
    LEDOFF0 = request.find('/?LED=OFF0')
    if LEDOFF0 == 6:
        print('TURN LED0 OFF')
        LED0.value(not LED0.value()) # toggle
        time.sleep(1)
    response = html
    conn.send(response)
    conn.close()
