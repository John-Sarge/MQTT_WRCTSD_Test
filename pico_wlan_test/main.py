# A simple example that:
# - Connects to a WiFi Network defined by "ssid" and "password"
# - Performs a GET request (loads a webpage)
# - Queries the current time from a server

import network   # handles connecting to WiFi
import urequests # handles making and servicing network requests
import socket
import dht
import time
from time import sleep

# Connect to network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
# prevent the wireless chip from
# activating power-saving mode when it is idle
wlan.config(pm = 0xa11140)
# set a static IP address for Pico
# your router IP could be very different eg:
# 192.168.1.1
wlan.ifconfig((ip, subnet, gateway, dns))
# Fill in your network name (ssid) and password here:
ssid = 'put SSID inside these quotes'
#password = 'idontknow'
wlan.connect(ssid)#, password)

led = machine.Pin('LED', machine.Pin.OUT)
for i in range(wlan.status()):
    led.on()
    time.sleep(0.2)
    led.off()
    time.sleep(0.2)
    print('Connected')
    status = wlan.ifconfig()
    print('ip = ' + status[0])

# Example 1. Make a GET request for google.com and print HTML
# Print the html content from google.com
print("1. Querying google.com:")
r = urequests.get("http://www.google.com")
print(r.content)
r.close()

# Example 2. urequests can also handle basic json support! Let's get the current time from a server
print("\n\n2. Querying the current GMT+0 time:")
r = urequests.get("http://date.jsontest.com") # Server that returns the current GMT+0 time.
print(r.json())
