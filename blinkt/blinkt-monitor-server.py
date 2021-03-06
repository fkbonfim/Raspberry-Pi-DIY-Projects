# https://pastebin.com/7TvNKqMV

# http://forums.pimoroni.com/t/simple-network-monitor-with-blinkt/5915

import os,signal
from blinkt import clear,set_brightness, set_pixel, show,set_all
from time import sleep

hostlist = ["192.168.178.1", "192.168.178.28", "192.168.178.32", "192.168.178.2", "192.168.178.130", "192.168.178.103", "192.168.178.100", "8.8.8.8"]
hostid = ["Router", "ESP-3B1053", "ESP-3A2DC2", "OpenELEC", "PiSpy", "Pantiltpi", "pisense", "Internet"]

clear()
set_brightness(0.05)
set_all(0,0,255)
show()
sleep(30)

def handler(signum, frame):
   clear()
   show()
   exit(0)

signal.signal(signal.SIGTERM, handler)

while True:
   for hostnum, hostname in enumerate(hostlist):
      response = os.system("ping -c 1 -w2 " + hostname + " > /dev/null 2>&1")
      if response == 0:
#         print hostnum, ' - ', hostid[hostnum], 'is up!'
         set_pixel(hostnum, 0, 255, 0)
      else:
#         print hostnum, ' - ', hostid[hostnum], 'is down!'
         set_pixel(hostnum, 255, 0, 0)
   show()
   sleep(60)
