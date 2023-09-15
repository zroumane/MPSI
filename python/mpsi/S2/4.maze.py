def init_grille(h, w):
    G = []
    for i in range(h):
        G.append([])
        for j in range(w):
            G[i].append(w*i+j)
    return G

def substituer(a,b,grille):
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille[i][j] == a:
                grille[i][j] = b


def liste_murs(h, w):
    M = []
    for i in range(h):
        for j in range(w-1):
            M.append(((i, j), (i, j+1)))
    for i in range(h-1):
        for j in range(w):
            M.append(((i, j), (i+1, j)))
    return M


import random

def generer(grille, murs):
    random.shuffle(murs)
    garde = []
    supp = []
    for m in murs:
        a = grille[m[0][0]][m[0][1]]
        b = grille[m[1][0]][m[1][1]]
        if b != a:
            substituer(a, b, grille)
            supp.append(m)
        else:
            garde.append(m)
    return garde, supp


import matplotlib.pyplot as plt

def afficher(Lg, h, w):
    plt.xlim(-1, w)
    plt.ylim(-1, h)


    plt.plot([-0.5, -0.5 + w], [-0.5, -0.5])
    plt.plot([-0.5, -0.5 + w], [-0.5+h, -0.5+h])
    plt.plot([-0.5, -0.5], [-0.5, -0.5+h])
    plt.plot([-0.5 + w, -0.5 + w], [-0.5+h, -0.5])

    for c1, c2 in Lg:
        if c1[0] == c2[0]:
            plt.plot([(c2[1] + c1[1])/2, (c2[1] + c1[1])/2], [-0.5+c1[0], -0.5+c1[0]+1])
        else:
            plt.plot([-0.5 + c1[1], -0.5 + c1[1]+1], [(c2[0] + c1[0])/2, (c2[0] + c1[0])/2])



def liste_adjacence(Ls):
    d = {}
    for m1, m2 in Ls:
        if m2 not in d:
            d[m2] = []
        if m1 not in d:
            d[m1] = []
        d[m1].append(m2)
        d[m2].append(m1)
    return d


def explorer(x, y, La, marques):
    Vs = La[(x, y)]
    for u, v in Vs:
        if (u, v) not in marques.keys():
            marques[(u,v)] = (x, y)
            explorer(u, v, La, marques)


def chemin(marques, u, v):
    m = marques[(u, v)]
    if not m:
        return [(0, 0)]
    else:
        return chemin(marques, m[0], m[1]) + [(u, v)]

import time


def maze(h, w):
    print('Init')
    init = init_grille(h,w)
    print('Murs')
    murs = liste_murs(h,w)
    print('Generation')
    Lg, Ls = generer(init, murs)
    print('Adjacent')
    La = liste_adjacence(Ls)
    print('Resolution')
    s = time.time()
    marques = {(0,0): None}
    explorer(0, 0, La, marques)
    L = chemin(marques, h-1, w-1)
    e = time.time()
    print(e-s)
    print('Affichage')
    afficher(Lg, h, w)

    for i in range(len(L)-1):
        x1, y1 = L[i]
        x2, y2 = L[i+1]
        plt.plot([y1, y2], [x1, x2] , 'm--')
    plt.show()

maze(10,10)





