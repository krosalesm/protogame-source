import tile
import pygame


class Map:
    def __init__(self):
        self.size = (32,32)
        self.map = list()
        self.imgWall = pygame.image.load("resources\\sprites\\wall.png")

    def create(self,len):
        for tilesCounter in range(len):
            self.map.append(tile.Tile("wall"))
