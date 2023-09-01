# 1
import csv

f = open(r"/media/zephyr/Zephyr/mpsi/info/python/doc/tp18_liaisons_metro.csv")
L = list(csv.reader(f, delimiter=','))


# 2
SL = []
for l in L:
    for i in l:
        if 'Saint-Lazare' in l and i != 'Saint-Lazare':
            SL.append(i)


# 3
stations = []
for l in L:
    for s in l:
        if s not in stations:
            stations.append(s)

# 4
consec = {}
for s in stations:
    consec[s] = []
    for l in L:
        if s in l:
            for i in l:
                if i != s and i not in consec[s]:
                    consec[s].append(i)


# 5
SL_d2 = []
for l in SL:
    for c in consec[l]:
        if c not in SL_d2 and c != 'Saint-Lazare':
            SL_d2.append(c)


# 6
SL_d3 = []
for l in SL_d2:
    for c in consec[l]:
        if c not in SL_d2 and c != l:
            SL_d3.append(c)


# 7, 8, 9
k = 0

dist = {'Saint-Lazare': k}
direction = {'Saint-Lazare': 'Saint-Lazare' }
SL_k = ['Saint-Lazare']

while len(SL_k) != 0:
    k += 1
    G = []
    for l in SL_k:
        for c in consec[l]:
            if c not in dist and c != l:
                direction[c] = l
                dist[c] = k
                G.append(c)
    SL_k = G




#10
def parcours_en_largeur(depart):
    k = 0
    dist = {depart: k}
    direction = {depart: depart }
    Last = [depart]

    while len(Last) != 0:
        k += 1
        G = []
        for l in Last:
            for c in consec[l]:
                if c not in dist and c != l:
                    direction[c] = l
                    dist[c] = k
                    G.append(c)
        Last = G
    return dist, direction




#11
def chemin(depart, arrivee):
    dist, direction = parcours_en_largeur(depart)
    T = [arrivee]
    k = dist[arrivee]
    while k != 0:    
        arrivee = direction[arrivee]
        T.append(arrivee)
        k -= 1
    return T













