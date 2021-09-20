
# Jelszó program

bemenet = input('Mi a jelszó? ')

proba = 0

while bemenet != jelszo:
    proba += 1
    if proba == 3:
        print('Rendszer lezárva!')
        break
    print('Rossz jellszó, próbáld újra!')
    bemenet = input('Mi a jelszó? ')


if bemenet == jelszo:
    print('Hozzáférés a nukleáris indító kódokhoz biztosítva!')
