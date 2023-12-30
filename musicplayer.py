import pygame
from tkinter import *
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Music Player By Blessy")
        self.root.geometry("900x500")

        pygame.init()
        pygame.mixer.init()

        self.playlist = Listbox(root, selectbackground="purple", selectmode=SINGLE)
        self.playlist.pack(fill="both", expand="true")

        self.loadButton = Button(root, text="Load ✔ ", command=self.load)
        self.loadButton.pack()

        self.playButton = Button(root, text="Play  🙌 ", command=self.play)
        self.playButton.pack()

        self.pauseButton = Button(root, text="Pause 👀", command=self.pause)
        self.pauseButton.pack()

        self.stopButton = Button(root, text="Stop  🤢", command=self.stop)
        self.stopButton.pack()

        self.root.mainloop()

    def load(self):
        file = filedialog.askopenfilename(defaultextension=".mp3",
                                           filetypes=[("Music files", "*.mp3"), ("All files", "*.*")])
        self.playlist.insert(END, file)

    def play(self):
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def stop(self):
        pygame.mixer.music.stop()


root = Tk()
app = MusicPlayer(root)
