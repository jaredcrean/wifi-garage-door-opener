import network

#Connect to wifi network and also set adhoc wifi for debuging
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect('wifi-access-point-name', 'password')
    while not sta_if.isconnected():
        pass
print('network config:', sta_if.ifconfig())
print('mac addres:' sta_if.config('mac'))
