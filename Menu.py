import urwid
import GameState
import Entities
import main
def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

palette = [
    ('banner2', 'black', 'light gray'),
    ('streak', 'black', 'dark red'),
    ('bg', 'black', 'dark magenta'),
    ('Floor', 'black', 'dark red' ),
    ('Wall', 'black', 'light green')]

txt = urwid.Text(('banner2', u" Hello World "), align='center')
map1 = urwid.AttrMap(txt, 'streak')
fill = urwid.Filler(map1)
map2 = urwid.AttrMap(fill, 'bg')
loop = urwid.MainLoop(map2, palette, unhandled_input=exit_on_q)
loop.run()
main.main3()