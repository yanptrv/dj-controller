from threading import Thread
from serial import Serial, SerialException


class MIDI(Thread):
    def __init__(self, pl, pr,
                 volume_left,
                 volume_right,
                 song_left,
                 song_right):
        super().__init__()
        self.daemon = True
        self.board = None
        
        self.pl = pl
        self.pr = pr
        self.volume_left = volume_left
        self.volume_right = volume_right
        self.song_left = song_left
        self.song_right = song_right
        self.connect()
    
    def connect(self):
        try:
            self.board = Serial('/dev/ttyUSB0', 9600)
        except SerialException:
            pass

    def read_serial(self):
        if self.board is not None:
            try:
                response = self.board.readline().decode('utf-8').strip()
                return response
            except SerialException:
                self.connect()
        self.connect()
        return None
    
    def run(self):
        while True:
            val = self.read_serial()
            if val is None:
                self.connect()
            elif val == 'vol2':
                self.volume_left.set(self.read_serial())
            elif val == 'vol1':
                self.volume_right.set(self.read_serial())
            elif val == 'seek1':
                self.song_left.set(self.read_serial())
            elif val == 'seek2':
                self.song_right.set(self.read_serial())
            elif val == 'play1':
                self.pl.play_song()
            elif val == 'stop1':
                self.pl.stop_song()
            elif val == 'pause1':
                self.pl.pause_song()
            elif val == 'next1':
                self.pl.next_song()
            elif val == 'prev1':
                self.pl.prev_song()
            elif val == 'play2':
                self.pr.play_song()
            elif val == 'stop2':
                self.pr.stop_song()
            elif val == 'pause2':
                self.pr.pause_song()
            elif val == 'next2':
                self.pr.next_song()
            elif val == 'prev2':
                self.pr.prev_song()
