
class Szemely:
    def __init__(self, nev, kor, neme, nemzetiseg, vallas='hindu'):
        self.nev = nev
        self.kor = kor
        self.neme = neme
        self.nemzetiseg = nemzetiseg
        self.vallas = vallas
        self.hello()

    def hello(self):
        print('hello ' + self.nev)

class Alkalmazott(Szemely):
    tapasztalat = 4
    megbizhatosag = 8
    vegzettseg = 'konyvelo'

Eni = Alkalmazott('Enikő', 32, 'nő', 'Magyar', 'protestáns')
