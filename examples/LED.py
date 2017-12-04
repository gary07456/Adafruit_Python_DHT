#!/usr/bin/python
import RPi.GPIO as GPIO
import time

#Alerts OFF
GPIO.setwarnings(False)

# Use physical pin numbers
GPIO.setmode(GPIO.BOARD)
# Set up header pin 22 (GPIO18) as an input
print "Setup Pin 22 is Output..."
ledPin = 22
GPIO.setup(ledPin, GPIO.OUT)
# Set up header pin 18 (GPIO25) as an input
buttonPin = 18
print "Setup Pin 18 is Input.."
GPIO.setup(buttonPin, GPIO.IN)
prev_input = 1
i = 0

while True:
  #take a reading
  input = GPIO.input(buttonPin)
  #if the last reading was low and this one high, print
  if ((not prev_input) and input):
    i += 1
    print("Button pressed ("+str(i)+")")
    GPIO.output(ledPin, True)
    time.sleep(0.1)
    GPIO.output(ledPin, False)
  #update previous input
  prev_input = input
  #slight pause to debounce
  time.sleep(0.05)
