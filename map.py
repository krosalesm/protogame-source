import tile
import pygame


class Map:
    def __init__(self):
        self.size = (32,32)
        self.map = list()
        self.imgWall = pygame.image.load("resources\\tiles\\wall.png")
        self.imgFloor = pygame.image.load("resources\\tiles\\floor.png")
        self.ourMap = list()

    def create(self):
        #Lee mapa de archivo txt generado por MapCreator y lo dibuja.
        txtMapa = open("resources\\maps\\mapa.txt")
        mapReader = txtMapa.read()
        txtMapa.close()
        mapReaderSplited = mapReader.split("\n")
        for x in mapReaderSplited:
            self.ourMap.append(x)


