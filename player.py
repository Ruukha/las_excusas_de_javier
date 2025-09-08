from npc import Npc

class Player:
    def __init__(self, map, pos, conditions = None):
        self.__map = map
        self.__pos = pos
        self.inv = []
        self.time = 0
        self.conditions = conditions if conditions else []
    
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
        room = self.__map[self.pos]
        match dir:
            case 'norte':
                d = 0
            case 'sur':
                d = 1
            case 'este':
                d = 2
            case 'oeste':
                d = 3
        if 'time' in room and room['time'][d]:
            self.add_time(room['time'][d])
        self.pos = room['dir'][d] if room['dir'][d] else self.pos
        
    def collect(self, obj):
        print(f'+{obj}')
        self.inv.append(obj)

    def display_time(self):
        return f'{8 + (self.time + 30)//60}:{(30 + self.time)%60:02d}'

    def describe(self):
        print(f'Son las: {self.display_time()}')
        print(f'{self.pos.title()}: {self.__map[self.pos]['desc']}')

    def add_time(self, time):
        print(f'+{time} minutos')
        self.time += time

    def hablar(self, npc, chat='normal'):
        if chat == None:
            chat = 'normal'
        thread = ''
        param = None
        while True:
            situation = npc.diags[chat][thread]
            print(situation['message'], end='')

            if 'time' in situation and situation['time']:
                self.add_time(situation['time'])
            if 'move'in situation and situation['move']:
                param = situation['move']
            if 'repeat' in situation and situation['repeat']:
                thread = thread[:-1]
                continue
            if 'end' in situation and situation['end']:
                if type(npc) == Npc:
                    print("Fin de la conversación.")
                break
            if 'ending' in situation and situation['ending']:
                param = True
                break

            ans = input('Respuesta: ')
            if ans not in npc.diags[chat]:
                print('Introduce una respuesta válida (los números de las opciones)')
            else:
                thread = thread + ans

        if 'return' in situation and not param:
            param = situation['return']
        return param