
with open('mondasok.txt', 'r', encoding='utf-8') as file:

    sor = file.readline()

    while sor:
        print(sor.strip())
        sor = file.readline()