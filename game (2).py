import pygame
import imports

class Game:
    def __init__(self):
        pygame.init()
        self.displayWidth = 820
        self.displayHeight = 670
        self.TITLE = 'Protogame'
        self.displayDimension = (self.displayWidth,self.displayHeight)
        self.gameDisplay = pygame.display.set_mode(self.displayDimension)#(),pygame.FULLSCREEN #pygame.display.Info().current_w,pygame.display.Info().current_h
        self.gameOverBool = False
        self.movement = False #Muestra si se dejo de presionar la tecla
        self.lastDir = 0 #Guarda la ultima posicion a la que iba
    def create(self):
        pygame.display.set_caption(self.TITLE)

		
    def update(self):
        pygame.display.update()
        self.gameDisplay.fill(imports.BLACK)

    def draw(self,player):
        self.gameDisplay.blit(player.sprite,player.pos)

    def gameOver(self):
        self.gameOverBool = True

    def getKey(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameOver()
            if event.type == pygame.KEYDOWN:
                self.movement = True
                if event.key == pygame.K_p:
                    self.gameOver()

                # movimiento arriba,abajo,izq,derecha
                if event.key == pygame.K_d:
                    self.lastDir = 3
                if event.key == pygame.K_a:
                    self.lastDir = 7
                if event.key == pygame.K_w:
                    self.lastDir = 1
                if event.key == pygame.K_s:
                    self.lastDir = 5

                # movimiento diagonal
                if event.key == pygame.K_e:
                    self.lastDir = 2
                if event.key == pygame.K_c:
                    self.lastDir = 4
                if event.key == pygame.K_z:
                    self.lastDir = 6
                if event.key == pygame.K_q:
                    self.lastDir = 8

            if event.type == pygame.KEYUP:
                self.movement = False
                self.lastDir = 0
                
        return self.lastDir

        
    def destroy(self):
        pygame.quit()
        quit()
        
        
        
