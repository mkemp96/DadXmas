from datetime import datetime
import RPi.GPIO as GPIO
import time


class GPIO_interface:
    def __init__(self, comms):
        self.txrx = comms
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        self.ir_pin = 26
        GPIO.setup(self.ir_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def event_detector(self):
        GPIO.add_event_detect(self.ir_pin, GPIO.FALLING, callback=self.triggered, bouncetime =2000)


    def triggered(self, pin):
        print(pin)
        message = str(datetime.now()) + ":   " + " Sensor triggered"
        self.txrx.sendToClient(message)
        print("Sensor detected object!")
        time.sleep(0.5)


    def get_state(self, pin):
        if GPIO.input(pin):
            return 1
        else:
            return 0

    def close_all(self):
        GPIO.cleanup()
