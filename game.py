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

    def drawMap(self,mapa):
        i = 0
        a = 0
        for x in mapa.ourMap:
            for y in x:
                if y == 'x':
                    self.gameDisplay.blit(mapa.imgWall,(mapa.size[0]*i,mapa.size[1]*a))
                if y == 'y':
                    self.gameDisplay.blit(mapa.imgFloor,(mapa.size[0]*i,mapa.size[1]*a))
                i += 1
            a +=1
            i = 0

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

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.x,self.y = event.pos

                # movimiento arriba,abajo,izq,derecha
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                 self.lastDir = 1
            if keys[pygame.K_a]:
                 self.lastDir = 7
            if keys[pygame.K_d]:
                 self.lastDir = 3
            if keys[pygame.K_s]:
                 self.lastDir = 5

            if keys[pygame.K_a] and keys[pygame.K_w]:
                self.lastDir = 8
            if keys[pygame.K_a] and keys[pygame.K_s]:
                self.lastDir = 6
            if keys[pygame.K_w] and keys[pygame.K_d]:
                self.lastDir = 2
            if keys[pygame.K_s] and keys[pygame.K_d]:
                self.lastDir = 4

            #if keys[pygame.none]:
              # self.movement = False
              # self.lastDir = 0

            if not any(keys):
                self.movement = False
                self.lastDir = 0

            # if event.type == pygame.KEYUP:
            #     self.movement = False
            #     self.lastDir = 0

        return self.lastDir

        
    def destroy(self):
        pygame.quit()
        quit()
        
        
        
