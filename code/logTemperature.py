#!/usr/bin/python
import os
import time
import sqlite3
import sys 
""" Log Current Time, Temperature in Celsius and Fahrenheit
Returns a list [time, tempC, tempF] """

def readTemp():
 tempfile = open("/sys/bus/w1/devices/28-000006979949/w1_slave")
 tempfile_text = tempfile.read()
 currentTime=time.strftime('%x %X %Z')
 tempfile.close()
 tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
 tempF=tempC*9.0/5.0+32.0

 params = (currentTime, tempC, tempF)
 con = sqlite3.connect('temperature2.db')
 
 with con:
  cur = con.cursor()
  cur.execute("INSERT INTO tempData2 VALUES(?, ?, ?)",params)

  data = cur.fetchone()

 return [currentTime, tempC, tempF]

print "current temperature is:", readTemp()
print "Temperature logged"
