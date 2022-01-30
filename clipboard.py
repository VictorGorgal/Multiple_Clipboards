from serial import Serial
from pyautogui import hotkey
from time import sleep
import pyperclip as pc

pi = Serial('COM4', 115200)

info = ''
mem = {}  # dict was choosen so the user can copy from any of the clipboards initially, a list would need the user to use the clipboard in sequence


def copy_interface():  # copies whatever is selected
    hotkey('ctrl', 'c')


def paste_interface():  # pastes where cursor is
    hotkey('ctrl', 'v')


def copy_to_memory(i):  # moves what is saved on the windows clipboard to memory
    copy_interface()
    mem[i] = pc.paste()
    print(f'copied: "{mem[i]}"')


def paste_from_memory(i):  # loads memory to clipboard
    pc.copy(mem[i])
    paste_interface()


while True:
    if pi.in_waiting > 0:  # reads what button code was sent
        info = pi.readline().decode('ascii').strip()

    if info:
        mode = info[0]  # c or v (copy or paste)
        clipboard_id = info[1]  # id of the clipboard used

        print(f'{mode=} {clipboard_id=}')

        if mode == 'c':
            copy_to_memory(clipboard_id)

        if mode == 'v':
            paste_from_memory(clipboard_id)

        info = ''
        
    sleep(0.1)  # checks only 10 times per second to not impact PC performance
