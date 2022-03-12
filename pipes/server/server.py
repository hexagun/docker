#!/usr/bin/python3

import os, sys
import time

path = "/tmp/nikhil"
try:
    os.mkfifo(path)
except:
    pass
# s = input("Enter text: ")
for i in range(0, 11):
    file = open(path, 'w')
    text = str(i)
    print(text)
    file.write(str(text))
    time.sleep(1)
    file.close()
