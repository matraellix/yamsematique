from random import randint
from math import exp, cos, sqrt, log, pi, prod


def uniformdisc(m, M):
    return randint(m, M)


def uniformcont():
    return randint(0, 10**6)/10**6


def binom(p):
    return uniformcont() < p


def binomdice(p):
    return 1+sum([binom(p) for i in range(5)])


def poisson(lambd):
    l = exp(-lambd)
    k = 0
    p = 1
    while p > l:
        k += 1
        p *= uniformcont()
    return k-1


def poissondice(lambd):
    if (k := poisson(lambd)) >= 6:
        return 6
    elif k == 0:
        return 1
    return k


def normal(mu, sigma):
    u1 = uniformcont()
    u2 = uniformcont()
    z = sqrt(-2*log(u1))*cos(2*pi*u2)
    return sigma*z+mu


def expo(lambd):
    # fonction de repartition : f(x) = 1-exp(-lambda * x)
    # reciproque : ln(-y+1)/(-lambda) = f(y)
    return log(1-uniformcont())/(-lambd)


def laplace(mu, b):
    u = uniformcont()
    return mu-b*(-1 if ((u-0.5) < 0) else 1)*log(1-2*abs(u-0.5))


def gamma(n):
    # Very simple approximation of Gamma(N, 1)
    return -log(prod([uniformcont() for i in range(n)]))


if __name__ == "__main__":

    dices = [0 for i in range(6)]
    for i in range(2500):
        dices[uniformdisc(1, 6)-1] += 1
    print(dices)

    dices = [0, 0]
    for i in range(2500):
        dices[binom(0.25)] += 1
    print(dices)
    print("here is binomial")

    dices = []
    for i in range(1500):
        x = poisson(4)
        while x+1 > len(dices):
            dices.append(0)
        dices[x] += 1
    print(dices)

    dicespos = []
    dicesneg = []
    m = 0
    for i in range(1500):
        x = normal(4, 2)
        m += x
        rax = abs(round(x))
        if x > 0:
            tab = dicespos
        else:
            tab = dicesneg
        while rax+1 > len(tab):
            tab.append(0)
        tab[rax] += 1
    dicesneg.reverse()
    print(dicesneg+dicespos, m/1500)

    dicespos = []
    m = 0
    for i in range(1500):
        x = expo(1)
        m += x
        rax = round(x)
        while rax+1 > len(dicespos):
            dicespos.append(0)
        dicespos[rax] += 1
    print(dicespos)

    dicespos = []
    dicesneg = []
    m = 0
    for i in range(1500):
        x = laplace(-5, 2)
        m += x
        rax = abs(round(x))
        if x > 0:
            tab = dicespos
        else:
            tab = dicesneg
        while rax+1 > len(tab):
            tab.append(0)
        tab[rax] += 1
    dicesneg.reverse()
    print(dicesneg+dicespos, m/1500)

    dicespos = []
    m = 0
    for i in range(1500):
        x = gamma(4)
        m += x
        rax = round(x)
        while rax+1 > len(dicespos):
            dicespos.append(0)
        dicespos[rax] += 1
    print(dicespos, m/1500)
