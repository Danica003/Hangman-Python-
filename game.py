class Game:
    def __init__(self, word):                   # konstruktor
        self.word=word                          # rec koju pogadjamo
        self.guessed=[False] * len(word)        # lista pogodjenih
        self.victory=False
        self.loss=False
        self.tries=0                            #pokusaji do sada
        self.used=set()                         #pokusana slova, set je kao lista ali se ne ponavljaju clanovi i nisu u nekom redosledu
    def Round(self, letter):
        z=0
        success = False
        for i in range(len(self.word)):
            if self.word[i] == letter:
                success = True
                self.guessed[i] = True
            if self.guessed[i] == True:
                z = z + 1
        if not success:
            self.tries = self.tries + 1
            self.used.add(letter)
        if z==len(self.word):
            self.victory = True
        elif self.tries == 6:
            self.loss=True







