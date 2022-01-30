from time import sleep
from machine import Pin


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


class ClipBoard:
    def __init__(self):
        self.clipboards = []
    
    def add(self, copy_pin, paste_pin):  # adds a new clipboard as a tuple
        self.clipboards += [(new_pin(copy_pin, Pin.IN),
                            new_pin(paste_pin, Pin.IN))]
    
    def trigger(self):
        for clipboard_id, clipboard in enumerate(self.clipboards):  # for every clipboard
            for button_id, button in enumerate(clipboard):  # for every button on the clipboard
                if button.rising_trigger():  # checks if it has been triggered
                    mode = 'c' if button_id == 0 else 'v'
                    num = clipboard_id
                    return mode + str(num)  # return the code for the button pressed (e.g. c0, v2, c3...)



led = Pin(17, Pin.OUT)

clipboard = ClipBoard()

clipboard.add(10, 11)  # to add more clipboards simply add more of these lines with the copy and paste buttons respectively
clipboard.add(12, 13)
clipboard.add(14, 15)

def blink():  # debouce + visual confirmation
    led.value(1)
    sleep(0.4)
    led.value(0)

while True:
    if button_code := clipboard.trigger():  # calls the trigger() func and saves the button code returned from trigger()
        print(button_code)  # sends the code through Serial to PC
        
        blink()
