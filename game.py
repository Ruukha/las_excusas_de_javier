from player import Player
from map import Map
from npc import Npc

map = Map({
    'habitacion': ['bano', None, 'comedor', None],
    'bano': [None, 'habitacion', None, None]
})
javier = Player(map, 'habitacion')