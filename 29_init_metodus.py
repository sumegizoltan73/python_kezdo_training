

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

Ildi = Szemely('Ildikó', 32, 'nő', 'Magyar')
Laci = Szemely('Laszló', 47, 'férfi', 'Kínai')

print(type(Ildi))
print(type(Laci))