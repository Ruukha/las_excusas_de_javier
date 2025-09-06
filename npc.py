class Npc:
    locs = []
    npcs = []
    def __init__(self, pos, diags):
        self.__pos = pos
        self.diags = diags
        type(self).locs.append(pos)
        type(self).npcs.append(self)

    @property
    def pos(self):
        return self.__pos

    def hablar(self, chat='normal'):
        thread = ''
        time = 0
        param = None
        while True:
            situation = self.diags[chat][thread]
            print(situation['message'], end='')

            if 'time' in situation and situation['time']:
                print(f'+{situation['time']} minutos')
                time += situation['time']
            if 'repeat' in situation and situation['repeat']:
                thread = thread[:-1]
                continue
            if 'end' in situation and situation['end']:
                if type(self) == Npc:
                    print("Fin de la conversación.")
                break
            if 'ending' in situation and situation['ending']:
                param = True
                break

            ans = input('Respuesta: ')
            if ans not in self.diags[chat]:
                print('Introduce una respuesta válida (los números de las opciones)')
            else:
                thread = thread + ans

        if 'return' in situation and not param:
            param = situation['return']
        return time, param

class Event(Npc):
    locs = []
    npcs = []
    def __init__(self, pos, diags):
        self.__pos = pos
        self.diags = diags
        type(self).locs.append(pos)
        type(self).npcs.append(self)
    
    @property
    def pos(self):
        return self.__pos