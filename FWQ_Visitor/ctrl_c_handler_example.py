#!/usr/bin/python3

import signal
import time

def handler(signum, frame):
    print("\nctrl+c")
    res = input('Salir? [Y/n]')
    if res.lower() != 'y' and len(res) > 0:
        print('La ejecución continuará')
    else:
        print('Saliendo')
        exit(1)
    
signal.signal(signal.SIGINT, handler)

counter = 0
while True:
    time.sleep(1)
    print(counter)
    counter += 1

