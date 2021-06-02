from threading import Thread
from serial import Serial, SerialException


class MIDI(Thread):
    def __init__(self, volume_left, volume_right, song_left, song_right):
        super().__init__()
        try:
            self.board = Serial('/dev/ttyUSB0', 9600)
        except SerialException:
            self.board = None
        self.volume_left = volume_left
        self.volume_right = volume_right
        self.song_left = song_left
        self.song_right = song_right
    
    def read_serial(self):
        if self.board is not None:
            response = self.board.readline().decode('utf-8').strip()
            return response
        else:
            return None
    
    def run(self):
        while True:
            val = self.read_serial()
            if val is None:
                exit()
            elif val == 'a':
                self.volume_left.set(self.read_serial())
            elif val == 'b':
                self.volume_right.set(self.read_serial())
            elif val == 'c':
                self.song_left.set(self.read_serial())
            elif val == 'd':
                self.song_right.set(self.read_serial())
