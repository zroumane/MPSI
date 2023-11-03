import matplotlib.pyplot as plt
import random


def init(data, k):
    return random.sample(data, k)


def distance(a, b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)**(1/2)


def min_k(pixel, moyens):
    k = 0
    dk = distance(pixel, moyens[k])
    for i in range(1, len(moyens)):
        d = distance(pixel, moyens[i])
        if d < dk:
            k = i
            dk = d
    return k


def repartition(data, moyens):
    C = [[] for _ in moyens]
    for d in data:
        k = min_k(d, moyens)
        C[k].append(d)
    return C



def moyenne(L):
    n = len(L)
    return [
        sum([l[0] for l in L])/n,
        sum([l[1] for l in L])/n,
        sum([l[2] for l in L])/n,
    ]


def mise_a_jour(C, k):
    return [moyenne(C[i]) for i in range(k)]


def kmeans(data, k):
    moyens = init(data, k)
    C = repartition(data, moyens)
    f = False
    while not f:
        print('ok')
        moyens_ = mise_a_jour(C, k)
        C = repartition(data, moyens_)
        if moyens_ == moyens:
            f = True
        moyens = moyens_
    return moyens



def construction(original, moyens):
    G = []
    for l in original:
        G.append([])
        for p in l:
            m = min_k(p, moyens)
            G[-1].append(moyens[m])
    return G


def compress(file, k):
    original = plt.imread(file).tolist()

    data = []
    for l in original:
        data += l

    moyens = kmeans(data, k)
    return construction(original, moyens)




file = "D:\mp\info\python\doc\exemple.png"
k = 16
G = compress(file, k)
plt.imshow(G)
plt.show()
