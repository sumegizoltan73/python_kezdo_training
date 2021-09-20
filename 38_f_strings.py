
# String formátozás, és f stringek

# régi mód
szoveg1 = "A te neved %s, és %d éves vagy." % ("Andi", 17)
print(szoveg1)


# nem olyan régi mód
szoveg2 = "A te neved {}, és {} éves vagy.".format("Ildi", 28)
print(szoveg2)


# új mód (f strings)
nev = "Enikő"
kor = 35
szoveg3 = f"A te neved {nev}, és {kor} éves vagy."
print(szoveg3)

nevek_szotar = {"Betti":23, "Évi":32, "Ildi":31, "Zsuzsi":40, "Andi":34}

for nev, kor in nevek_szotar.items():
    print(f"A te neved {nev}, és {kor + 5} éves vagy.")
