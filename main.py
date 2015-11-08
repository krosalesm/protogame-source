import imports
import map
import music

def main():

    game = imports.ini.Game()
    game.create()
    player = imports.person.Person("spritePlayer.png")

    musica = music.Music()
    musica.playSong()
    map1 = map.Map()

    map1.create()

    while not game.gameOverBool:
     
        keys = game.getKey()

        player.move(keys)

        game.drawMap(map1)

        game.draw(player)
        
        game.update()

    game.destroy()

if __name__ == "__main__":
    main()
