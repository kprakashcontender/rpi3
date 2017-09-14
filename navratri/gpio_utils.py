import RPi.GPIO as GPIO

ON = False
OFF = True
mode = GPIO.BCM


def pin_setup_for_output(pin_numbers):
    for i in pin_numbers:
        GPIO.setup(i, GPIO.OUT)


def pin_setup_for_input(pin_numbers):
    for i in pin_numbers:
        GPIO.setup(i, GPIO.IN)


def turn_on(pin_number):
    GPIO.output(pin_number, ON)


def turn_off(pin_number):
    GPIO.output(pin_number, OFF)


def refresh_board():
    GPIO.cleanup()
    GPIO.setmode(mode)
