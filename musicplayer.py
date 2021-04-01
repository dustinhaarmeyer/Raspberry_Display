import pygame
import os
import time
from time import sleep

playlist = ""
actual = 0
musicDir = '/test/'
plN = 0

class Musicplayer():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
    def getPlaylist(self):
        global actual
        global playlist
        global musicDir
        actual = 0
        os.chdir(musicDir)
        playlist = os.listdir()
        for x in playlist:
            plN += 1
        print('Songs:' + plN)
    def load(self):
        global actual
        global playlist
        pygame.mixer.music.load(playlist[actual])
    def play(self):
        pygame.mixer.music.play()
        print('Play')
    def pause(self):
        pygame.mixer.music.pause()
        print('Pause')
    def resume(self):
        pygame.mixer.music.unpause()
        print('Resume')
    def next(self):
        global actual
        stop()  
        actual += 1
        if actual >= plN:
            actual = 0
        load()
        play()
        print('Playing next')
    def back(self):
        global actual
        stop()  
        actual -= 1
        if actual <= 0:
            actual = 0
        load()
        play()
    def stop(self):
        pygame.mixer.music.stop()
        print('Stop')