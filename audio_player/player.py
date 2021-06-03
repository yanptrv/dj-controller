import os
import tkinter
import vlc
from tkinter import *
from tkinter.filedialog import askdirectory


class Player:
    def __init__(self):
        self.music = vlc.MediaPlayer()
        self.directory = ""
        self.songs = []
        self.current_song = 0
        self.songs_counter = 0
        self.playing = False
        self.volume = IntVar()
        self.position = IntVar()
        
        self.listbox = None
        self.song_label = None
    
    def set(self, listbox, song_label):
        self.listbox = listbox
        self.song_label = song_label
    
    # FUNCTIONS FOR THE BUTTONS
    def directory_chooser(self, event):
        self.directory = ''
        self.songs = []
        self.listbox.delete(0, tkinter.END)
        self.directory = askdirectory()
        
        for file in os.listdir(self.directory):
            if file.endswith(".mp3") \
                    or file.endswith(".wav") \
                    or file.endswith(".ogg"):
                self.songs.append(file)
                # print(file)
        
        self.music.set_media(vlc.Media(self.directory + "/" +
                                       self.songs[self.current_song]))
        
        # PRINTING THE SONG NAMES
        self.songs.reverse()
        self.songs_counter = len(self.songs)
        i = self.songs_counter
        for song in self.songs:
            self.listbox.insert(0, str(i) + ". " + song)
            i -= 1
        self.songs.reverse()
    
    def change_volume(self, event):
        self.music.audio_set_volume(self.volume.get())
    
    def change_position(self, event):
        self.music.set_position(float(self.position.get()) / float(100))
    
    def change_label(self, text=None):
        if text is None:
            self.song_label.set(self.songs[self.current_song])
        else:
            self.song_label.set(text)
        pass
    
    def play_song(self, event):
        self.music.set_media(vlc.Media(self.directory + "/" +
                                       self.songs[self.current_song]))
        self.music.play()
        self.playing = True
        self.change_label()
    
    def stop_song(self, event):
        self.music.stop()
        self.playing = False
        self.change_label("Music Stopped")
    
    def pause_song(self, event):
        if self.playing:
            self.music.set_pause(1)
            self.playing = False
            self.change_label("Music Paused")
        else:
            self.music.set_pause(0)
            self.playing = True
            self.change_label()
    
    def next_song(self, event):
        if self.current_song < self.songs_counter - 1:
            self.current_song += 1
            self.music.set_media(vlc.Media(self.directory + "/" +
                                           self.songs[self.current_song]))
            self.music.play()
            self.playing = True
            self.change_label()
    
    def prev_song(self, event):
        if self.current_song > 0:
            self.current_song -= 1
            self.music.set_media(vlc.Media(self.directory + "/" +
                                           self.songs[self.current_song]))
            self.music.play()
            self.playing = True
            self.change_label()
