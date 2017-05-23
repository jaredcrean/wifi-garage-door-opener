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
#LED2 = machine.Pin(2, machine.Pin.OUT)

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
#    LEDON0 = request.find('/?LED=ON0')
    LEDOFF0 = request.find('/?LED=OFF0')
#    LEDON2 = request.find('/?LED=ON2')
#    LEDOFF2 = request.find('/?LED=OFF2')
    #print("Data: " + str(LEDON0))
    #print("Data2: " + str(LEDOFF0))
#    if LEDON0 == 6:
#        print('TURN LED0 ON')
#        LED0.low()
    if LEDOFF0 == 6:
        print('TURN LED0 OFF')
        LED0.value(not LED0.value()) # toggle
        time.sleep(1)
        LED0.value(not LED0.value()) # toggle
#        LED0.high()
#        time.sleep_ms(500)
#        LED0.high()
#    if LEDON2 == 6:
#        print('TURN LED2 ON')
#        LED2.low()
#    if LEDOFF2 == 6:
#        print('TURN LED2 OFF')
#        LED2.high()
    response = html
    conn.send(response)
    conn.close()
