import tile
import pygame


class Map:
    def __init__(self):
        self.size = (16,16)
        self.map = list()
        self.imgWall = pygame.image.load("resources\\sprites\\wall.png")
        self.ourMap = list()

    def create(self):
        self.ourMap.append("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        self.ourMap.append("x           x                                     x")
        self.ourMap.append("x           x                                     x")
        self.ourMap.append("x           x                                     x")
        self.ourMap.append("x           x                                     x")
        self.ourMap.append("x           x             xxxxxxxxxxxxxxxxxxxxxxxxx")
        self.ourMap.append("x           x             x                       x")
        self.ourMap.append("x           x             x                       x")
        self.ourMap.append("x                         x                       x")
        self.ourMap.append("x                         x                       x")
        self.ourMap.append("x                         x                       x")
        self.ourMap.append("x                         x                       x")
        self.ourMap.append("x                         x                       x")
        self.ourMap.append("x                         x                       x")
        self.ourMap.append("x                         x                       x")
        self.ourMap.append("x                         x                       x")
        self.ourMap.append("x                         x                       x")
        self.ourMap.append("x                         x                       x")
        self.ourMap.append("x                         x                       x")
        self.ourMap.append("x                         x                       x")
        self.ourMap.append("x                         x                       x")
        self.ourMap.append("x                         x                       x")
        self.ourMap.append("x                         x                       x")
        self.ourMap.append("x                         x                       x")
        self.ourMap.append("x                         x                       x")
        self.ourMap.append("x                         x                       x")
        self.ourMap.append("xxxxxxx    xxx            x                       x")
        self.ourMap.append("x            x            x                       x")
        self.ourMap.append("x            x            x                       x")
        self.ourMap.append("x            x            x                       x")
        self.ourMap.append("x            x            x                       x")
        self.ourMap.append("x            x            x                       x")
        self.ourMap.append("x            x                                    x")
        self.ourMap.append("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


