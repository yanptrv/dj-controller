import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory

root = Tk()
root.minsize(300, 300)
root.maxsize(1920, 1080)
pygame.mixer.init()

songs = []
current_song = 0
songs_counter = 0

v = StringVar()
song_label = Label(root, textvariable=v, width=35)


def directory_chooser():
    global songs_counter
    directory = askdirectory()
    os.chdir(directory)
    
    for file in os.listdir(directory):
        if file.endswith(".ogg"):
            songs.append(file)
            print(file)
    
    pygame.mixer.music.load(songs[current_song])
    # pygame.mixer.music.play()
    
    # PRINTING THE SONG NAMES
    songs.reverse()
    songs_counter = len(songs)
    i = songs_counter
    for song in songs:
        listbox.insert(0, str(i) + ". " + song)
        i -= 1
    songs.reverse()


def change_label():
    global current_song
    v.set(songs[current_song])


def play_song(event):
    global current_song
    pygame.mixer.music.load(songs[current_song])
    pygame.mixer.music.play()
    change_label()


def stop_song(event):
    pygame.mixer.music.stop()
    v.set("")


def pause_song(event):
    pygame.mixer.music.pause()


def unpause_song(event):
    pygame.mixer.music.unpause()


def next_song(event):
    global current_song
    global songs_counter
    if current_song < songs_counter - 1:
        current_song += 1
        pygame.mixer.music.load(songs[current_song])
        pygame.mixer.music.play()
        change_label()


def prev_song(event):
    global current_song
    if current_song > 0:
        current_song -= 1
        pygame.mixer.music.load(songs[current_song])
        pygame.mixer.music.play()
        change_label()


label = Label(root, text='Music Player')
label.pack()

listbox = Listbox(root)
listbox.pack()

directory_chooser()

buttons = dict()
buttons["play"] = Button(root, text="Play")
buttons["stop"] = Button(root, text="Stop")
buttons["pause"] = Button(root, text="Pause")
buttons["unpause"] = Button(root, text="Unpause")
buttons["prev"] = Button(root, text="Prev")
buttons["next"] = Button(root, text="Next")

for button in buttons:
    buttons[button].pack()

buttons["play"].bind("<Button-1>", play_song)
buttons["stop"].bind("<Button-1>", stop_song)
buttons["pause"].bind("<Button-1>", pause_song)
buttons["unpause"].bind("<Button-1>", unpause_song)
buttons["next"].bind("<Button-1>", next_song)
buttons["prev"].bind("<Button-1>", prev_song)

song_label.pack()

root.mainloop()
