# esp8266 Wifi Garage Door Opener
----

## Description

**Here I am using a esp8266 wifi enabled microcontroller to open my garage door**

__The plan is to have it controlled though a home automation system where it can send a text message if the door is open for longer then a hour.__

I use a HTTP app for android called **HTTP Shortcuts**.

## Requirements

This will require the esptool.py https://github.com/espressif/esptool

MicroPython https://github.com/micropython/micropython

## Uploading to the NodeMCU/esp8266

`cd /project/home/`

### Flash the MicroPython firmware to the esp8266

`esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect -fm dio 0 esp8266-20171101-v1.9.3.bin`

### Upload the boot.py and the main.py

- I like to use the WebREPL website makes in easy http://micropython.org/webrepl/.
- now upload the boo.py and the main.py.
- once that completes you should be able to trigger the relay with a HTTP PUT.


