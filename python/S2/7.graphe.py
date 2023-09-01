import csv

f = open(r"D:\mpsi\info\python\doc\positions.csv", encoding='utf-8')
villes = list(csv.reader(f, delimiter=','))
f = open(r"D:\mpsi\info\python\doc\voisins.txt", encoding='utf-8')
liens = list(csv.reader(f, delimiter=','))

xville = {}
yville = {}

for v in villes:
    xville[v[0]] = int(v[1])
    yville[v[0]] = int(v[2])


def lignedroite(ville1, ville2):
    return ((xville[ville1] - xville[ville2])**2 +  (yville[ville1] - yville[ville2])**2)**(1/2)


adjacence = {}

for v in liens:
    adjacence[v[0]] = v[1:]


def dijkastra(depart):
    parent = {}
    dist = {}

    candidats = [(depart, depart, 0)]

    while len(candidats) != 0:
        todel = 0
        u, p, d = candidats[0]
        for i in range(len(candidats)):
            if candidats[i][2] < d:
                u, p, d = candidats[i]
                todel = i

        candidats.pop(todel)

        if u not in parent:
            parent[u] = p
            dist[u] = d
            for v in adjacence[u]:
                l = lignedroite(u, v)
                if v not in parent:
                    candidats.append((v, u, d + l))
    return parent, dist


def chemin(depart, arrivee):
    parent, dist = dijkastra(depart)
    L = [arrivee]
    while True:
        p = parent[L[-1]]
        L.append(p)
        if p == depart:
            break
    return L


import matplotlib.pyplot as plt

plt.plot(xville.values(), yville.values(), 'ob')

for p, vs in adjacence.items():
    for v in vs:
        plt.plot([xville[p], xville[v]], [yville[p], yville[v]],'-r')

for v in xville.keys():
    plt.text(xville[v]+6, yville[v]-3, v, fontsize='xx-small')

ax = plt.gca()
ax.set_aspect('equal', 'box')
plt.show()






