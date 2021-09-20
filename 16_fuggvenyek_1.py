
nevek1 = ['Xena', 'Bözsi', 'Vica', 'Eni', 'Ildi', 'Zsuzsi', 'Evi', 10]
nevek2 = ['Pityu', 'Ati', 'Peti', 'Bence', 'Feri']

def nev_printer(nev_lista):
    for nev in nev_lista:
        if isinstance(nev, str):
            print(nev.upper())
        else:
            print('nem string típus, hanem: ' + str(type(nev)))

nev_printer(nevek1)
nev_printer(nevek2)