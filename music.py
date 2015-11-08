import pygame


class Music:
    def __init__(self):
        self.name = "musica"
    def playSong(self):

        pygame.init()

        pygame.mixer.music.load("resources\\music\\songWaiting.mp3")

        pygame.mixer.music.play(-1)

    def playPersuitSong(self):
        pygame.init()

        pygame.mixer.music.load("resources\\music\\songWarning.wav")

        pygame.mixer.music.play(-1)