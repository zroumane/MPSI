def jeu(N):
    a = 0
    b = N
    while True:
        c = (a + b) // 2
        r = input(str(c) + ' ?\n')
        if r == "+":
            a = c + 1
        if r == "-":
            b = c - 1
        if r == "=":
            break



def recherche(L, x):
    a = 0
    b = len(L) - 1
    while True:
        c = (a + b) // 2
        if L[c] == x :
            return c
        elif c == b:
            return -1
        elif x < L[c] :
            b = c - 1
        elif L[c] < x:
            a = c + 1


def test():
    import time
    import random

    L = random.sample(range(10**9), 100000)
    L.sort()

    s1 = time.time()
    o = 0
    for i in range(10000):
        x = random.choice(L)
        pos=recherche(L,x)
        if L[pos] == x:
            o+=1
    e1 = time.time()
    if o == 10000:
        print("Test réussi")
    else:
        print("Test raté")
    print("Duree : ", e1-s1, "secondes")

    s2 = time.time()
    for i in range(10000):
        x = random.choice(L)
        pos=L.index(x)
    e2 = time.time()
    print("Duree : ", e2-s2, "secondes")

    print("Différence : ", abs((e1 - s1) - (e2 - s2)) , "secondes")





