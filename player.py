class Player:
    def __init__(self, map, pos):
        self.__map = map
        self.__pos = pos
        self.inv = []
        self.tiempo = 0
        self.conditions = {}
    
    @property
    def pos(self):
        return self.__pos
    
    @pos.setter
    def pos(self, newpos):
        if newpos in self.__map:
            self.__pos = newpos
        else:
            raise ValueError('Esta posición está fuera del mapa')

    def move(self, dir):
        match dir:
            case 'norte':
                d = 1
            case 'sur':
                d = 1
            case 'este':
                d = 2
            case 'oeste':
                d = 3
        self.pos = self.__map[self.pos][0][d] if self.__map[self.pos][0][d] else self.pos
        
    def collect(self, obj):
        self.inv.append(obj)

    def describe(self):
        print(self.__map[self.pos][1])