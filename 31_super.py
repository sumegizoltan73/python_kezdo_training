
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
    def __init__(self, nev, kor, neme, nemzetiseg, vallas, tapasztalat, megbizhatosag, vegzettseg):
        super().__init__(nev, kor, neme, nemzetiseg, vallas)
        self.tapasztalat = tapasztalat
        self.megbizhatosag = megbizhatosag
        self.vegzettseg = vegzettseg

Eni = Alkalmazott('Enikő', 32, 'nő', 'Magyar', 'protestáns', 12, 8, 'könyvelő')