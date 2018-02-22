import GameState
import Entities
import urwid
def main():
    game = GameState.GameState()
    game.world.createMap(12,8)
    game.world.placeEntity(1,2,Entities.Hero('H',0,1,5,'Dickbutt'))
    heroCoord = [1,2]
    while True:
        # Hero Turn
        tmp = game.worldDisplay()
        tmp += game.world.displayGrid()
        tmp += game.scoreDisplay()

        def exit_on_q(key):
            raise urwid.ExitMainLoop()

        palette = [
            ('banner2', 'black', 'dark cyan'),
            ('streak', 'black', 'light gray'),
            ('bg', 'black', 'black'),
            ('Floor', 'black', 'dark red' ),
            ('Wall', 'black', 'light green'),
            ('Hero', 'light red', 'light green')]
        print(tmp)
        values = [('Floor',"HI"),('Wall',"YO")]
        #test = eval("urwid.Text(tmp,align='center')")
        sectest = urwid.Text(tmp,align='center')
        #txt = urwid.Text([('Floor',"HELLO"),("Wall","NO")], align='center')
        txt2 = urwid.Text('Floor', align='center')
        map1 = urwid.AttrMap(sectest, 'streak')
        fill = urwid.Filler(map1)
        map2 = urwid.AttrMap(fill, 'bg')
        loop = urwid.MainLoop(map2, palette, unhandled_input=exit_on_q)
        loop.start()
        loop.draw_screen()
        loop.stop()




        userInput = input('Give input: ').upper()
        if userInput == '0':
            # Hero Faces UP
            x = 0
        elif userInput == '1':
            # Hero Faces RIGHT
            x = 0
        elif userInput == '2':
            # Hero Faces DOWN
            x = 0
        elif userInput == '3':
            # Hero Faces Right
            x = 0
        elif userInput == 'W':
            # Hero Moves UP
            game.world.moveEntity(heroCoord[0],heroCoord[1],heroCoord[0],heroCoord[1]-1)
            heroCoord[1] -= 1
        elif userInput == 'A':
            # Hero Moves LEFT
            game.world.moveEntity(heroCoord[0],heroCoord[1],heroCoord[0]-1,heroCoord[1])
            heroCoord[0] -= 1
        elif userInput == 'S':
            # Hero Moves DOWN
            game.world.moveEntity(heroCoord[0],heroCoord[1],heroCoord[0],heroCoord[1]+1)
            heroCoord[1] += 1
        elif userInput == 'D':
            # Hero Moves RIGHT
            game.world.moveEntity(heroCoord[0],heroCoord[1],heroCoord[0]+1,heroCoord[1])
            heroCoord[0] += 1
        else:
            # Bad input!
            break
        # Item Turn
        # Monster Turn
        # Noise Cleanup and other Cleanup
        
       
    
if __name__ == '__main__':
    main()