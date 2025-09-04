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

    def hablar(self):
        print('muy bien')