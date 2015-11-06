import imports
import map

def main():

    game = imports.ini.Game()
    game.create()
    player = imports.person.Person("spritePlayer.png")

    map1 = map.Map()
    #Se da lo largo del mapa
    map1.create(20)

    while not game.gameOverBool:
     
        keys = game.getKey()

        player.move(keys)

        game.drawMap(map1)

        game.draw(player)
        
        game.update()

    game.destroy()

if __name__ == "__main__":
    main()
