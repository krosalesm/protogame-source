import imports

def main():
    game = imports.ini.Game()
    game.create()
    player = imports.person.Person()

    while not game.gameOverBool:
     
        keys = game.getKey()


        player.move(keys)
        
        game.draw(player)
        
        game.update()



    game.destroy()



if __name__== "__main__":
    main()
