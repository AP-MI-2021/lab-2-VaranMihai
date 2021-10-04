
a = float(input("Dati valoare temperatura: "))
b = str(input("Din: "))
c = str(input("In: "))


def get_temp(a, b, c):
    '''
    Transformă o temperatură dată într-o scară dată într-o altă scară dată.
    :param a: valoare temperatura
    :param b: scara temperatura data
    :param c: scara temperatura ceruta
    :return: valoare temperatura in scara ceruta
    '''
    if c == 'K':
       if b == 'C':
           a = a+273.15
       elif b == 'F':
            a = (a-32)*5/9+273.15
       else:
           return a
    elif c == 'C':
       if b == 'K':
           a = a-273.15
       elif b == 'F':
           a = (a - 32) * 5 / 9
       else:
            return a
    elif c == 'F':
        if b == 'K':
            a =(a-273.15) * 9/5 + 32
        elif b == 'C':
            a = (a*9/5)+32
        else:
            return a
    return a

assert get_temp(100, 'C', 'F') == 212
assert get_temp(50, 'F', 'K') == 283.15

print(get_temp(a, b, c))

def cmmdc(e, f):
    '''
    Calculeaza cmmdc-ul a 2 numere
    :param e: nr intreg
    :param f: nr intreg
    :return: cmmdc-ul numerelor
    '''
    if f == 0:
        if e == 0:
            return 0
        else:
            return e
    else:
        r = e % f
        while r > 0:
            e = f
            f = r
            r = e % f
    return f

assert cmmdc(50,16) == 2
assert cmmdc(123,66) == 3
assert cmmdc(40,350) == 10
assert cmmdc(216,324) == 108

n = int(input("Dati valoarea lui n: "))
tlis = []

for i in range(0, n):
    zeta = int(input("Adaugati numere in lista: "))
    tlis.append(zeta)

def get_cmmmc(tlis,n):
    '''
    Calculează CMMMC al n numere date.
    :param tlis: lista de numere date
    :param n: numarul de numere in lista
    :return: cmmmc numerelor din lista
    '''
    cmmmc = 1
    for i in range(0, n):
        cmmmc = cmmmc * tlis[i]/cmmdc(cmmmc, tlis[i])
    return int(cmmmc)

assert get_cmmmc([2, 4, 8, 16], 4) == 16
assert get_cmmmc([3, 15, 6, 5], 4) == 30
assert get_cmmmc([20, 4, 50], 3) == 100

print(get_cmmmc(tlis, n))

