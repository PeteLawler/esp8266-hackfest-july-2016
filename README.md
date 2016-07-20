# esp8266-hackfest-july-2016

Follow along EtherPad:
https://pad.taslug.org.au/p/july-esp8266-hackfest

Repository:
https://git.scriptforge.org/taslug/esp8266-hackfest-july-2016
https://github.com/taslug/esp8266-hackfest-july-2016 (mirror)

What's in this repository:

firmware - NodeMCU and MicroPython Firmware

examples - Some simple examples
examples/javascript
examples/python
examples/lua

remotepower - Our remote power source code

Requirements:
Linux:
Terminal program (minicom, screen, putty)
Python (pip install esptool)
WIndows:
Terminal program (putty.exe)
Node Flasher

esptool --pro /dev/ttyUSB0 write_flash 0x00000 <Firmware/firmware_filename>
