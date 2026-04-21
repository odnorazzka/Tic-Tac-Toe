from gameparts import Board
from inspect import getsource, isfunction, ismethod

game = Board()

print('='*20, 'Способ 1', '='*20)
print(type(game))
print(type(game) == Board)
print(type(game) is Board)
print(type(game) == str)

print(isinstance(game, Board))
print(isinstance(game, str))

print('='*20, 'Способ 2', '='*20)
print(game.__class__)

print('='*20, 'Способ 3', '='*20)
print(dir(game))
print('__str__' in dir(game))
print(hasattr(game, '__str__'))

print('='*20, 'Способ 4', '='*20)
print(game.__dict__)

print('='*20, 'Способ 5', '='*20)
print(getsource(Board))
