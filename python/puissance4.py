import os
os.chdir('Q:\Documents en consultation')

print(os.listdir())

import corrige_minmax

car = ['.', 'X', 'O']


def nouvelle_grille():
    return [[car[0] for _ in range(7)] for _ in range(6)]


def afficher(G):
    s = ' '.join([str(i) for i in range(7)])
    for l in G:
        s += '\n' + ' '.join(l)
    s += '\n' + '-'*13
    print(s)


def jouer_coup(G, c, mark):
    for i in range(6):
        if G[i][c] != '.':
            G[i-1][c] = mark
            return i-1
        if i == 5:
            G[i][c] = mark
            return i



def gain(G, l, c):
    mark = G[l][c]
    for d in [(1,0), (0,1), (1,1), (1,-1)]:
        t = 1
        for o in [-1, 1]:
            for n in range(1, 4):
                p = (l+d[0]*n*o, c+d[1]*n*o)
                if p[0] in range(6) and p[1] in range(7):
                    if G[p[0]][p[1]] == mark:
                        t += 1
                    else:
                        break
        if t >= 4:
            return True
    return False

def pleine(G):
    for c in range(6):
        if G[0][c] == '.':
            return False
    return True

def demande_colonne(G, mark):
    print(mark,'to play')
    while True:
        try:
            c = int(input('column ? '))
            if G[0][c] != '.':
                raise 'column full'
            return c
        except:
            print('invalid input')


def partie():
    i = 0
    G = nouvelle_grille()
    while True:
        afficher(G)
        i = 0 if i == 1 else 1
        c = demande_colonne(G, car[i])
        l = jouer_coup(G, c, car[i])
        if gain(G, l, c):
            afficher(G)
            print(car[i], 'win')
            break
        if pleine(G):
            afficher(G)
            print('draw')
            break


def copie_grille(G):
    return [[G[i][j] for j in range(7)] for i in range(6)]


def jouer_coup_bis(grille, j, col):
    M = copie_grille(grille)
    jouer_coup(M, col, car[j])
    return M


def list_filles(u):
    j, G, c = u
    pos = []
    for col in range(7):
        if G[0][col] == '.':
            last = 0
            for i in range(1, 6):
                if G[i][col] != '.':
                    break
                last = i
            pos.append((last, col))
    return pos


def heuristique(u):
    v = 0
    for pos in list_filles(u):
        M = jouer_coup_bis(u[1], 1, pos[1])
        if gain(M, pos[0], pos[1]):
            v += 1
        M = jouer_coup_bis(u[1], 2, pos[1])
        if gain(M, pos[0], pos[1]):
            v -= 1
    return v

def valeur(u, n):
    j, G, c = u
    if gain(G, c[0], c[1]):
        if pleine(G):
            return 0
        return (-1 if j == 2 else 1)*1000
    if n == 1:
        return heuristique(u)
    else:
        filles = list_filles(u)
        val = []
        for pos in filles:
            M = jouer_coup_bis(G, 3-j, pos[1])
            val.append(valeur((3-j, M, pos), n-1))
        return max(val) if 3-j == 1 else min(val)


def choisir_colonne(grille):
    filles = list_filles((1, grille, None))
    bv = valeur((1, jouer_coup_bis(grille, 1, filles[0][1]), filles[0]), 5)
    bpos = filles[0]
    filles.pop(0)
    for pos in filles:
        M = jouer_coup_bis(grille, 1, pos[1])
        v = valeur((1, M, pos), 5)
        print(v)
        if v > bv:
            v = bv
            bpos = pos
    return bpos[1]


def partie_vs_ordi():
    j = 1
    G = nouvelle_grille()
    while True:
        afficher(G)
        c = None
        if j == 2:
            c = demande_colonne(G, car[j])
        else:
            c = choisir_colonne(G)
            print('ordi play ', c)
        l = jouer_coup(G, c, car[j])
        if gain(G, l, c):
            afficher(G)
            print('ordi' if j == 1 else 'player', ' win')
            break
        if pleine(G):
            afficher(G)
            print('draw')
            break
        j = 3 - j


partie_vs_ordi()









































