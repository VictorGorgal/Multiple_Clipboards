from serial import Serial
from pyautogui import hotkey
from time import sleep
import pyperclip as pc

pi = Serial('COM4', 115200, timeout=1)

info = ''
mem = ['', '', '']


def copy_interface():  # copies whatever is selected
    hotkey('ctrl', 'c')


def paste_interface():  # pastes where cursor is
    hotkey('ctrl', 'v')


def copy_to_memory(i):  # moves what is saved on windows clipboard to memory
    copy_interface()
    mem[i] = pc.paste()
    print(mem[i])


def paste_from_memory(i):  # loads memory to clipboard
    pc.copy(mem[i])
    paste_interface()


while True:
    if pi.in_waiting > 0:  # reads what button was pressed
        info = pi.readline().decode('ascii').strip()
        print(f'{info=}')

    if info == 'c1':  # copies clipboard to memory at ID 0
        copy_to_memory(0)

    if info == 'v1':  # pastes from memory at ID 0
        paste_from_memory(0)

    if info == 'c2':
        copy_to_memory(1)

    if info == 'v2':
        paste_from_memory(1)

    if info == 'c3':
        copy_to_memory(2)

    if info == 'v3':
        paste_from_memory(2)

    info = ''
    sleep(0.1)  # checks only 10 times per second to not impact PC performance
