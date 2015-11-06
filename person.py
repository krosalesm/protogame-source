import imports
import world
SIZE = (32,32)
class Person:
    def __init__(self,img):
        self.pos = (0,0)
        self.size = SIZE
        self.img = img
        self.acceleration = .001
        self.maxSpeed = 8
        self.speed = 1.2
        self.speedDefault = 0.01
        self.speedNow = 0.1
        self.health = 100
        self.rotation = 0 # Direccion ha donde esta volteando
        self.item = 0 #El item que tiene'
        self.sprite = imports.pygame.image.load("resources\\sprites\\"+ self.img)
    def move(self,whereTo): #Le envie el movimiento que hizo en x,y

#FALTA VER HACIA DONDE SE VA A DIRIJIR Y QUE FRENE CON LA GRAVEDAD
        
        worldPhysics = world.World()
        if whereTo == 0:
            if self.speedNow > self.speedDefault:
                self.speedNow -= worldPhysics.gravity
            if self.speedNow < self.speedDefault:
                self.speedNow = self.speedDefault
            
        else:
            self.speedNow += self.acceleration

        if self.speedNow > self.maxSpeed:
                self.speedNow = self.maxSpeed


            
        if whereTo == 3:
            self.pos = (self.pos[0]+self.speedNow,self.pos[1])
        if whereTo == 7:
            self.pos = (self.pos[0]-self.speedNow,self.pos[1])
        if whereTo == 1:
            self.pos = (self.pos[0],self.pos[1]-self.speedNow)
        if whereTo == 5:
            self.pos = (self.pos[0],self.pos[1]+self.speedNow)

        if whereTo == 2:
            self.pos = (self.pos[0]+self.speedNow,self.pos[1]-self.speedNow)
        if whereTo == 4:
            self.pos = (self.pos[0]+self.speedNow,self.pos[1]+self.speedNow)
        if whereTo == 6:
            self.pos = (self.pos[0]-self.speedNow,self.pos[1]+self.speedNow)
        if whereTo == 8:
            self.pos = (self.pos[0]-self.speedNow,self.pos[1]-self.speedNow)
