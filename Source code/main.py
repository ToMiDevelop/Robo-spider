# Source code used to control a simple spider like obstacle avoiding robot
# Published under the GPL-3.0 License
# This code uses HCSR-04 drover library created by Roberto Sánchez - https://github.com/rsc1975/micropython-hcsr04

# Version 1.0
# Published to the public use on 13-04-2021

# Author: Tomasz Michael - ToMiDevelop on github

# Hardware programmed: Raspberry Pi Pico

# All of the other details can be found in the readme.md file and the connection schematics view

import machine
import utime
import hcsr04
import random

# Engine steering pins definitions

M1A=machine.Pin(18)
M1B=machine.Pin(19)
M2A=machine.Pin(20)
M2B=machine.Pin(21)

# Button pins definitions

buttonA=machine.Pin(22,machine.Pin.IN,machine.Pin.PULL_DOWN)
buttonB=machine.Pin(28,machine.Pin.IN,machine.Pin.PULL_DOWN)

# Definining PWM objects for steering the motors

pwm_M1A=machine.PWM(M1A)
pwm_M1B=machine.PWM(M1B)
pwm_M2A=machine.PWM(M2A)
pwm_M2B=machine.PWM(M2B)

# Setiting PWM pins frequency

pwm_M1A.freq(500)
pwm_M1B.freq(500)
pwm_M2A.freq(500)
pwm_M2B.freq(500)

# Setting PWM value to 0 na on all steering pins - 0V

pwm_M1A.duty_u16(0)
pwm_M1B.duty_u16(0)
pwm_M2A.duty_u16(0)
pwm_M2B.duty_u16(0)

# Creating sensor object (to use the HC-SR04 sensor) cinnected on specified pins

sensor=hcsr04.HCSR04(trigger_pin=15,echo_pin=14,echo_timeout_us=1000000)

# Defining 0/1 variable - controls if robot is in on or off state

on=0

# Defininig maximum pwm value constant, default is max_V: 26700 (1,5 V on motor), but why not to experiment?

max_V=35000

# Defining front obstacle safe distance value /we assume using cm/

safe_distance=30.00000

# Defining movement functions

def forward():
    pwm_M1A.duty_u16(max_V)
    pwm_M1B.duty_u16(0)
    pwm_M2A.duty_u16(max_V)
    pwm_M2B.duty_u16(0)
    
def backward():
    pwm_M1A.duty_u16(0)
    pwm_M1B.duty_u16(max_V)
    pwm_M2A.duty_u16(0)
    pwm_M2B.duty_u16(max_V)

def left_in_place():
    pwm_M1A.duty_u16(0)
    pwm_M1B.duty_u16(max_V)
    pwm_M2A.duty_u16(max_V)
    pwm_M2B.duty_u16(0)

def right_in_place():
    pwm_M1A.duty_u16(max_V)
    pwm_M1B.duty_u16(0)
    pwm_M2A.duty_u16(0)
    pwm_M2B.duty_u16(max_V)

def stop():
    pwm_M1A.duty_u16(0)
    pwm_M1B.duty_u16(0)
    pwm_M2A.duty_u16(0)
    pwm_M2B.duty_u16(0)

# Defininig distance measuring function - to the front obstacle /returns value in cm/

def distance():
    return sensor.distance_cm()

# temporary mvement test function, you can uncomment to test it

# def test_ruchu():
#    forward()
#    utime.sleep(6)
#    left_in_place()
#    utime.sleep(6)
#    right_in_place()
#    utime.sleep(6)
#    backward()
#    utime.sleep(6)

# Driving with avoiding frontal obstacles function, serial prints embedded for testing purposes, you can uncomment to use 'em

def power_on():
    direction=random.randrange(2)
    if distance()>safe_distance:
        forward()
        # print('Forward driving')
        utime.sleep(0.5)
    else:
        stop()
        # print("Obstacle detected")
        backward()
        # print('Backward driving')
        utime.sleep(2.0)
        stop()
        if direction==0:
            right_in_place()
            # print('Turning left')
            utime.sleep(2.0)
            stop()
        else:
            left_in_place()
            # print('Turning right')
            utime.sleep(2.0)
            stop()

# Block od code executed only once at program start
# Serial print embedded for testing purposes, you can uncomment to use it

# print('Power is on')

# Programs main infinite loop
# Serial print embedded for testing purposes, you can uncomment to use it

while True: 
    if buttonA.value()==1:
        on=1
        # print('I'm turned on')
        utime.sleep(0.1)
    if buttonB.value()==1:
        stop()
        on=0
        # print('I'm turned off')
        utime.sleep(0.3)
    if on==1:
        # print('Distance to front obstacle: ',distance(),' cm')
        power_on()