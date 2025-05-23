# pygame++
better than pygame.

But not as annoying as pgzero

Here on github i didn't put the someassets folder because its too much.

## How to use

Install requirements:
`pip install pygame cairosvg`

`brew install cairo`

on mac:
`pip3 install pygame cairosvg`

you need to import first (I personally recommend wildcard)

`from pygamepp import *`

then make a game variable with Game()

`game = Game()`

you could even put resizeable/fullscreen args, width and height, and title

but that is not required

you can define draw and update functions and then do this:

`
def draw(game):
  pass
def update(game, events):
  pass
game.draw = draw
game.update = update

game.run()
`
