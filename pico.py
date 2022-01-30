from time import sleep
from machine import Pin, UART


class new_pin:
    def __init__(self, gpio_num, mode, resistor=Pin.PULL_DOWN):
        self.pin = Pin(gpio_num, mode, resistor)
        self.last_read = self.pin.value()
        self.new_read = self.last_read
    
    def read(self):  # simple read
        self.last_read = self.new_read
        self.new_read = self.pin.value()
        return self.new_read
    
    def rising_trigger(self):  # returns true only on a rising edge
        if self.read() and not self.last_read:
            return True
        else:
            return False
    
    def falling_trigger(self):  # returns true only on a falling edge
        if not self.read() and self.last_read:
            return True
        else:
            return False
    
    def edge_trigger(self):  # returns true on any edge
        if self.read() != self.last_read:
            return True
        else:
            return False


uart = UART(1, 115200)

led = Pin(17, Pin.OUT)

ctrl_c1 = new_pin(10, Pin.IN)
ctrl_v1 = new_pin(11, Pin.IN)

ctrl_c2 = new_pin(12, Pin.IN)
ctrl_v2 = new_pin(13, Pin.IN)

ctrl_c3 = new_pin(14, Pin.IN)
ctrl_v3 = new_pin(15, Pin.IN)

def blink():  # debounce + visual confirmation
    led.value(1)
    sleep(0.4)
    led.value(0)

while True:
    if ctrl_c1.rising_trigger():
        print('c1')
        uart.write('c1')
        blink()
    
    if ctrl_v1.rising_trigger():
        print('v1')
        uart.write('v1')
        blink()
        
    if ctrl_c2.rising_trigger():
        print('c2')
        uart.write('c2')
        blink()
        
    if ctrl_v2.rising_trigger():
        print('v2')
        uart.write('v2')
        blink()
        
    if ctrl_c3.rising_trigger():
        print('c3')
        uart.write('c3')
        blink()
        
    if ctrl_v3.rising_trigger():
        print('v3')
        uart.write('v3')
        blink()
