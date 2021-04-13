import os
import serial

board = serial.Serial('/dev/ttyUSB0', 9600)
volume = ""
i = 0

while True:
    response = board.readline().decode('ISO-8859-1').strip()
    if response is not None:
        if response != volume and i != 0:
            volume = response
            command = 'amixer -D pulse sset Master ' + volume + '%'
            os.system(command)
            # print(volume)
    i = 1
