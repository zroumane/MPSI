import csv

f=open("F:\\TP inp\\groupes.csv", mode="r")

def trinome():
    lecteur = csv.reader(f, delimiter=";")
    lignes = list(lecteur)
    R = []
    t = 1
    L = []
    for eleve in lignes:
        if eleve[4] != t:
            a = True
            for i in L:
                for j in L:
                    if j[3] != i[3]:
                        if a:
                            R.append(t)
                            a = False
            t = eleve[4]
            L = []
        L.append(eleve)
    return R



def occurences(L):
    d = {}
    for i in L:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    return [(i, d[i]) for i in d.keys()]


def inverse(L):
    d = {}
    for i in L:
        if i[1] not in d:
            d[i[1]] = [i[0]]
        else:
            d[i[1]].append(i[0])
    return d