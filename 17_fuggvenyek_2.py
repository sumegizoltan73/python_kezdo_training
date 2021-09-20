
a = 10
b = 20

def osszeadas1():
    print(a+b)

def osszeadas2(a, b):
    return a+b

def osszeadas3():
    pass

def osszeadas4(*args):
    return sum(args)

def udvozlesek(*args):
    koszones = 'Ennyi féle köszönés létezik: '
    for k in args:
        koszones += k
        koszones += ", "
    print(koszones[0:len(koszones)-2])

udvozlesek('szia', 'szevasz', 'hello', 'szervusz')

osszeadas1()
print(osszeadas2(45, 25))
print(osszeadas4(1,2,3,4,5))


