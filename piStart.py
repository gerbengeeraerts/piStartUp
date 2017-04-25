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

###############################################################################
