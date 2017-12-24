from datetime import datetime
import numpy as np
import gpio_interface
import txrx

def main():
    comms = TxRx()
    sensor = GPIO_interface(comms)
    comms.listen(sensor.ir_pin)
    sensor.event_detector()


    comms.close_all()
    sensor.close_all()
if __name__ == "__main__":
    main()
