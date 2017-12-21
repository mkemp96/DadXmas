import time
import RPi.GPIO as GPIO


class GPIO_interface:
    def __init__(self):
        GPIO.setwarning(False)
        GPIO.setmode(GPIO.BCM)
        self.ir_pin = 23
        GPIO.setup(ir_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(ir_pin, GPIO.falling, callback=triggered)

    def triggered(self):
        print("Sensor detection event")

    def get_state(self, pin):
        if GPIO.input(pin):
            return 1
        else:
            return 0
