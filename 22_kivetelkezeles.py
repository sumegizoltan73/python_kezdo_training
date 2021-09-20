
lista = [1,2,3]

try:
    print(bla)
    #print(lista[5])
    #print(1 / 0)
except NameError as e:
    print(e, ' - Nem létező változó!')
except IndexError as e:
    print(e, ' - Tartományon kívüli index!')
except ZeroDivisionError as e:
    print(e, ' - Nullával osztás!')


lista = ['1', '2', '3', None, '4', '', '5', True, 'Bözsi', '12.64']

for i in lista:
    try:
        print(int(i)*2)
    except:
        continue

try:
    print(bla)
except:
    print('nem jó változó név!')
else:
    print('az else!')
finally:
    print('Try vége!')

