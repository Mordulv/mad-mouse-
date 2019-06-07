from pynput.mouse import Controller, Button
from random import randint as al

raton = Controller()

while True:
    raton.position = (al(-1000,1000),al(-1000,1000))
