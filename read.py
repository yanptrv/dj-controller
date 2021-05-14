import serial

board = serial.Serial('/dev/ttyUSB0', 9600)
volume = ''


def read_serial():
    response = board.readline().decode('utf-8').strip()
    return response


while True:
    if read_serial() == 'v1':
        print(read_serial() + ' ' + 'volume1')
    if read_serial() == 'v2':
        print(read_serial() + ' ' + 'volume2')
    if read_serial() == 's1':
        print(read_serial() + ' ' + 'seek1')
    if read_serial() == 's2':
        print(read_serial() + ' ' + 'seek2')
