
# 'r' = read (olvasás)
# 'w' = write (írás)
# 'a' = append (hozzáfűzés, mellékel)

with open('out.txt', 'w', encoding='utf-8') as file:
    szoveg = 'Egy jó szalonna, meg egy jó sör, bármikor jöhet.'

    file.write(szoveg)

with open('mondasok.txt', 'r', encoding='utf-8') as infile:
    with open('out2.txt', 'w', encoding='utf-8') as outfile:

        sor = infile.readline()

        while sor:
            outfile.write(sor)
            sor = file.readline()

with open('out2.txt', 'a', encoding='utf-8') as file:
    ujsor = 'Nem akarásnak nyögés a vége.'

    file.write(ujsor)

