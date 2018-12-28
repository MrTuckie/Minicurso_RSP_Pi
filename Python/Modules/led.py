import RPi.GPIO as GPIO
import time
from time import sleep

def pisca(n,led):
    for x in range(0,n):
        GPIO.output(led,0)
        sleep(0.5)
        GPIO.output(led,1)
        sleep(0.5)
