#imports########################################################################

import dothat.backlight as backlight
import dothat.lcd as lcd
import time
import math
import os
import psutil
from subprocess import *

#FUCNTIONS######################################################################

def get_CPU_Temperature():
	res = os.popen('vcgencmd measure_temp').readline()
	return(res.replace("temp=","").replace("'C\n",""))

def get_RAM_Info():
	p = os.popen('free')
	i=0
	while True:
		i = i+1
		line = p.readline()
		if i==2:
			return(line.split()[1:4])

def get_CPU_Usage():
	return psutil.cpu_percent(interval = 1)

def map_range(value, low1, high1, low2, high2):
	value = int(value)
	low1 = int(low1)
	low2 = int(low2)
	high1 = int(high1)
	high2 = int(high2)
	return int(low2) + int(high2-low2)*int(value-low1) / int(high1-low1)

def run_cmd(cmd):
	p = Popen(cmd, shell=True, stdout=PIPE)
	output = p.communicate()[0]
	return output

#CODE###########################################################################

lcd_refresh_time = 0.5

ram_data = get_RAM_Info()
ram_used = round(int(ram_data[1])/1000,1)
ram_total = round(int(ram_data[0])/1000,1)
ram_free = round(int(ram_data[2])/1000,1)

cmdlan = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"
cmdwlan = "ip addr show wlan0 | grep inet | awk '{print $2}' | cut -d/ -f1"

while True:
    x += 1
    cpuTemp = int(float(get_CPU_Temperature()))
    lcd.set_cursor_position(0,0)
    lcd.write("CPU Temp: "+str(cpuTemp))

    ipaddr = run_cmd(cmd)
    ipaddrwlan = run_cmd(cmdwlan)
    lcd.set_cursor_position(0,1)
    lcd.write(ipaddr)
    lcd.set_cursor_position(0,2)
    lcd.write(ipaddrwlan)

    time.sleep(lcd_refresh_time)
