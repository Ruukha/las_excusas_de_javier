class Player:
    def __init__(self, map, pos):
        map = map
        if pos in map:
            pos = pos
        else:
            raise ValueError('El jugador está fuera del mapa')
        tiempo = 0
        conditions = {}
    
    def move(self, newpos, dir):
        if newpos in self.map:
            match dir:
                case 'norte':
                    d = [0]
                case 'sur':
                    d = [1]
                case 'este':
                    d = [2]
                case 'oeste':
                    d = [3]
            self.pos = newpos[d]
        else:
            raise ValueError('El jugador está fuera del mapa')