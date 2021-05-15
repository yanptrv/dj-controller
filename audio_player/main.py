import os
import pygame
import vlc
from tkinter import *
from tkinter.filedialog import askdirectory

window = Tk()
window.title("DJCON")
window.minsize(700, 350)
# window.maxsize(1920, 1080)


class PlayerLeft:
    def __init__(self):
        pygame.mixer.init()
        self.music = pygame.mixer.music
        self.directory = ""
        self.songs = []
        self.current_song = 0
        self.songs_counter = 0
        self.volume = IntVar()
    
    # FUNCTIONS FOR THE BUTTONS
    def directory_chooser(self, event):
        self.directory = askdirectory()
        
        for file in os.listdir(self.directory):
            if file.endswith(".wav") \
                    or file.endswith(".mp3") \
                    or file.endswith(".ogg"):
                self.songs.append(file)
                print(file)
        
        self.music.load(self.directory + "/" + self.songs[self.current_song])
        
        # PRINTING THE SONG NAMES
        self.songs.reverse()
        self.songs_counter = len(self.songs)
        i = self.songs_counter
        for song in self.songs:
            listbox_left.insert(0, str(i) + ". " + song)
            i -= 1
        self.songs.reverse()
    
    def change_volume(self, event):
        self.music.set_volume(float(self.volume.get()) / float(100))
    
    def change_label(self, text=None):
        if text is None:
            song_label_left_value.set(self.songs[self.current_song])
        else:
            song_label_left_value.set(text)
    
    def play_song(self, event):
        self.music.load(self.directory + "/" + self.songs[self.current_song])
        self.music.play()
        self.change_label()
    
    def stop_song(self, event):
        self.music.stop()
        self.change_label("Music Stopped")
    
    def pause_song(self, event):
        if self.music.get_busy():
            self.music.pause()
        else:
            self.music.unpause()
    
    def next_song(self, event):
        if self.current_song < self.songs_counter - 1:
            self.current_song += 1
            self.music.load(self.directory + "/" +
                            self.songs[self.current_song])
            self.music.play()
            self.change_label()
    
    def prev_song(self, event):
        if self.current_song > 0:
            self.current_song -= 1
            self.music.load(self.directory + "/" +
                            self.songs[self.current_song])
            self.music.play()
            self.change_label()


class PlayerRight:  # todo
    def __init__(self):
        self.music = vlc.MediaPlayer()
        self.directory = ""
        self.songs = []
        self.current_song = 0
        self.songs_counter = 0
        self.playing = False
        self.volume = IntVar()
    
    # FUNCTIONS FOR THE BUTTONS
    def directory_chooser(self, event):
        self.directory = askdirectory()
        print(self.directory)
        
        for file in os.listdir(self.directory):
            if file.endswith(".mp3") \
                    or file.endswith(".wav") \
                    or file.endswith(".ogg"):
                self.songs.append(file)
                print(file)
        
        self.music.set_media(vlc.Media(self.directory + "/" +
                                       self.songs[self.current_song]))
        
        # PRINTING THE SONG NAMES
        self.songs.reverse()
        self.songs_counter = len(self.songs)
        i = self.songs_counter
        for song in self.songs:
            listbox_right.insert(0, str(i) + ". " + song)
            i -= 1
        self.songs.reverse()

    def change_volume(self, event):
        self.music.audio_set_volume(self.volume.get())

    def change_label(self, text=None):
        if text is None:
            song_label_right_value.set(self.songs[self.current_song])
        else:
            song_label_right_value.set(text)
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
        else:
            self.music.set_pause(0)
            self.playing = True

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


pl = PlayerLeft()
pr = PlayerRight()

player_left = Frame(window)
player_left.pack(side=LEFT)
player_right = Frame(window)
player_right.pack(side=RIGHT)

# VOLUME LABELS
volume_string = StringVar()
volume_string.set("Volume: ")

Label(player_left, textvariable=volume_string).pack(side=TOP)
volume_label_left = Label(player_left, textvariable=pl.volume)
volume_label_left.pack(side=TOP)

Label(player_right, textvariable=volume_string).pack(side=TOP)
volume_label_left = Label(player_right, textvariable=pr.volume)
volume_label_left.pack(side=TOP)

# VOLUME SLIDERS
volume_slider_left = Scale(player_left, length=300, from_=100, to=0,
                           showvalue=0, variable=pl.volume,
                           command=pl.change_volume)
volume_slider_left.set(50)
volume_slider_left.pack(side=RIGHT)
volume_slider_right = Scale(player_right, length=300, from_=100, to=0,
                            showvalue=0, variable=pr.volume,
                            command=pr.change_volume)
volume_slider_right.set(50)
volume_slider_right.pack(side=LEFT)

# SONG LIST LEFT
songs_frame_left = Frame(player_left)
songs_frame_left.pack()
scrollbar_left = Scrollbar(songs_frame_left)
scrollbar_left.pack(side=RIGHT, fill=Y)
listbox_left = Listbox(songs_frame_left, yscrollcommand=scrollbar_left.set,
                       selectmode=SINGLE, height=10, width=30)
listbox_left.pack()
scrollbar_left.config(command=listbox_left.yview)

# SONG LIST RIGHT
song_frame_right = Frame(player_right)
song_frame_right.pack()
scrollbar_right = Scrollbar(song_frame_right)
scrollbar_right.pack(side=RIGHT, fill=Y)
listbox_right = Listbox(song_frame_right, yscrollcommand=scrollbar_right.set,
                        selectmode=SINGLE, height=10, width=30)
listbox_right.pack()
scrollbar_left.config(command=listbox_right.yview)

# BUTTONS LEFT
buttons_frame_up_left = Frame(player_left)
buttons_frame_up_left.pack()
buttons_frame_mid_left = Frame(player_left)
buttons_frame_mid_left.pack()
buttons_frame_down_left = Frame(player_left)
buttons_frame_down_left.pack()

buttons_left = dict()
buttons_left["play"] = Button(buttons_frame_up_left, text="Play")
buttons_left["pause"] = Button(buttons_frame_up_left, text="Pause")
buttons_left["prev"] = Button(buttons_frame_up_left, text="Prev")
buttons_left["next"] = Button(buttons_frame_up_left, text="Next")
buttons_left["stop"] = Button(buttons_frame_up_left, text="Stop")
buttons_left["change_playlist"] = Button(buttons_frame_down_left,
                                         text="Change Playlist")

buttons_left["play"].pack(side=LEFT)
buttons_left["pause"].pack(side=LEFT)
buttons_left["prev"].pack(side=LEFT)
buttons_left["next"].pack(side=LEFT)
buttons_left["stop"].pack(side=LEFT)
buttons_left["change_playlist"].pack(side=LEFT)

buttons_left["play"].bind("<Button-1>", pl.play_song)
buttons_left["pause"].bind("<Button-1>", pl.pause_song)
buttons_left["next"].bind("<Button-1>", pl.next_song)
buttons_left["prev"].bind("<Button-1>", pl.prev_song)
buttons_left["stop"].bind("<Button-1>", pl.stop_song)
buttons_left["change_playlist"].bind("<Button-1>", pl.directory_chooser)

song_slider_left = Scale(buttons_frame_mid_left, orient=HORIZONTAL, length=200)
song_slider_left.pack()

song_label_left_value = StringVar()
song_label_left = Label(buttons_frame_mid_left,
                        textvariable=song_label_left_value,
                        width=35)
song_label_left.pack()

# BUTTONS RIGHT
buttons_frame_up_right = Frame(player_right)
buttons_frame_up_right.pack()
buttons_frame_mid_right = Frame(player_right)
buttons_frame_mid_right.pack()
buttons_frame_down_right = Frame(player_right)
buttons_frame_down_right.pack()

buttons_right = dict()
buttons_right["play"] = Button(buttons_frame_up_right, text="Play")
buttons_right["pause"] = Button(buttons_frame_up_right, text="Pause")
buttons_right["prev"] = Button(buttons_frame_up_right, text="Prev")
buttons_right["next"] = Button(buttons_frame_up_right, text="Next")
buttons_right["stop"] = Button(buttons_frame_up_right, text="Stop")
buttons_right["change_playlist"] = Button(buttons_frame_down_right,
                                          text="Change Playlist")

buttons_right["play"].pack(side=LEFT)
buttons_right["pause"].pack(side=LEFT)
buttons_right["prev"].pack(side=LEFT)
buttons_right["next"].pack(side=LEFT)
buttons_right["stop"].pack(side=LEFT)
buttons_right["change_playlist"].pack(side=LEFT)

buttons_right["play"].bind("<Button-1>", pr.play_song)
buttons_right["pause"].bind("<Button-1>", pr.pause_song)
buttons_right["next"].bind("<Button-1>", pr.next_song)
buttons_right["prev"].bind("<Button-1>", pr.prev_song)
buttons_right["stop"].bind("<Button-1>", pr.stop_song)
buttons_right["change_playlist"].bind("<Button-1>", pr.directory_chooser)

song_slider_right = Scale(buttons_frame_mid_right, orient=HORIZONTAL,
                          length=200)
song_slider_right.pack()

song_label_right_value = StringVar()
song_label_right = Label(buttons_frame_mid_right,
                         textvariable=song_label_right_value,
                         width=35)
song_label_right.pack()

# EXIT BUTTON
button_exit = Button(window, text="Exit",
                     command=window.destroy)
button_exit.pack(side=BOTTOM)

# LOOP THAT RUNS THE PROGRAM
window.mainloop()
