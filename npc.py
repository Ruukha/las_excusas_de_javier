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
        while True:
            message = self.diags[chat][thread]
            print(message)

            if 'ending' in message.lower():
                return True
            elif 'fin' in message.lower():
                return False

            ans = input('Respuesta: ')
            if ans not in self.diags[chat]:
                print('Introduce una respuesta válida (los números de las opciones)')
            else:
                thread = thread + ans

class Event(Npc):
    locs = []
    npcs = []
    def __init__(self, pos, diags):
        self.__pos = pos
        self.diags = diags
        type(self).locs.append(pos)
        type(self).npcs.append(self)

    def activate(self, chat='normal'):
        thread = ''
        time = 0
        while True:
            situation = self.diags[chat][thread]
            print(situation['message'], end='')

            if situation['time']:
                print(f'+{situation['time']} minutos')
                time += situation['time']
            if situation['repeat']:
                thread = thread[:-1]
                continue
            if situation['end']:
                break

            ans = input('Respuesta: ')
            if ans not in self.diags[chat]:
                print('Introduce una respuesta válida (los números de las opciones)')
            else:
                thread = thread + ans

        return time
    
    @property
    def pos(self):
        return self.__pos