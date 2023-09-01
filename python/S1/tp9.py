# Exo 1

def age():
    age = 2022 - int(input())
    print("Vous êtes né(e) en " + str(age - 1) + " ou en " + str(age))


# Exo 2

def puiss2(n):
    p = 1
    while 2**p < n:
        p+=1
    return p


# Exo 4

def mot():
    s = True
    m = ""
    while s:
        m = str(input())
        if len(m) == 8:
            s = False
    return m


# Exo 5
import random

def jeu(N):
    x = random.randrange(0, N-1)
    s = True
    while s:
        g = int(input())
        if g < x:
            print("trop petit")
        elif g > x:
            print("trop grand")
        else:
            print("gagné")
            s = False


# Exo 6

def response(L, G):
    e = 0
    d = 0
    for i in range(len(G)):
        if G[i] == L[i]:
            L[i] = -1
            e+=1
    for i in range(len(G)):
        if G[i] in L:
            d+=1
            L[i] = -1
    return [e, d]

def mm():
    L = [random.randint(1, 9) for i in range(0, 4)]
    s = True
    while s:
        G = [int(i) for i in list(input())]
        r = response(L.copy(), G)
        if r[0] == 4:
            print("gagné")
            s = False
        else:
            print("exacte.s : " + str(r[0]) + " ; déplacé.s : " + str(r[1]))




















