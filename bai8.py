#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : www.modmypi.com
# Link: https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi

import RPi.GPIO as GPIO
import time
from config import Config

GPIO.setmode(GPIO.BCM)


TRIG = 16
ECHO = 26


GPIO.setup(Config.BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)


while True:
    if GPIO.input(Config.BT1) == 0:
        print("Waiting For Sensor To Settle")
        time.sleep(2)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        while GPIO.input(ECHO)==0:
          pulse_start = time.time()

        while GPIO.input(ECHO)==1:
          pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance, 2)

        print("Distance: %scm" % distance)
        
        time.sleep(1)

GPIO.cleanup()
