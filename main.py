import pyfirmata
import time
from subprocess import call

if __name__ == '__main__':
    board = pyfirmata.ArduinoMega('/dev/ttyUSB1')
    print("Communication Successfully started")

    it = pyfirmata.util.Iterator(board)
    it.start()

    potentiometer = board.analog[0]
    potentiometer.enable_reporting()

    lastVol = ""

    while True:
        vol = potentiometer.read()
        if vol is not None:
            floatVol = float(potentiometer.read())*100
            intVol = int(floatVol)
            stringVol = str(intVol) + '%'
            if stringVol != lastVol:
                lastVol = stringVol
                call(["amixer", "-D", "pulse", "sset", "Master", stringVol])
        time.sleep(0.1)