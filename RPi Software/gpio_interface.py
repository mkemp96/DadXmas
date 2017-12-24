from datetime import datetime
import RPi.GPIO as GPIO


class GPIO_interface:
    def __init__(self, comms):
        self.txrx = comms
        GPIO.setwarning(False)
        GPIO.setmode(GPIO.BCM)
        self.ir_pin = 23
        GPIO.setup(self.ir_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def event_detector(self):
        GPIO.add_event_detect(self.ir_pin, GPIO.falling, callback=triggered)


    def triggered(self):
        message = str(datetime.now()) + ":   " + " Sensor triggered"
        self.txrx.sendToClient(message)
        print("Sensor detected object!")


    def get_state(self, pin):
        if GPIO.input(pin):
            return 1
        else:
            return 0

    def close_all(self):
        GPIO.cleanup()
