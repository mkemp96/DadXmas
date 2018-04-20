from datetime import datetime
import numpy as np
import gpio_interface as gp
import txrx
import time
import threading

def main():
    comms = txrx.TxRx('192.168.1.1', 7777, 512)
    sensor = gp.GPIO_interface(comms)
    comms.listen(sensor)

    try:
        print("help me")
        sensor.event_detector()
        while 1:
            time.sleep(100)
    except KeyboardInterrupt:
        print("Quitting!")
        comms.close_all()
        sensor.close_all()
if __name__ == "__main__":
    main()
