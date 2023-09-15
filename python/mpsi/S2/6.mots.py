def liste():
    mots = open("D:\mpsi\info\python\doc\dico_AZ.txt").readlines()
    l = len(mots)

    MDL = [[] for i in range(26)]
    for m in mots:
        m = m[:-1]
        n = len(m)
        if n < 26:
            MDL[n].append(m)

    return MDL


def voisins(MDL, m):
    V = []
    voisins_n = MDL[len(m)]
    N = len(voisins_n)
    for i in range(len(m)):
        for h in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            r = m[0:i] + h + m[i+1:len(m)]
            if r == m:
                continue
            a = 0
            b = N
            c = (a+b) // 2
            while abs(a-b) > 1:
                if voisins_n[c] < r:
                    a = c
                elif voisins_n[c] > r:
                    b = c
                else:
                    V.append(r)
                    break
                c = (a+b)//2
    return V



def adj(MDL):
    adj = {}
    for i in range(len(MDL)):
        print(i)
        for j in MDL[i]:
            adj[j] = voisins(MDL, j)
    return adj


def parcours(depart):
    provenance = {depart: depart}
    Last = [depart]

    while len(Last) != 0:
        G = []
        for l in Last:
            for c in adjacence[l]:
                if c not in provenance:
                    provenance[c] = l
                    G.append(c)
        Last = G
    return provenance


def chemin(depart, arrive):
    p = parcours(depart)
    if arrive not in p:
        return 'IMPOSSIBLE'
    else:
        C = [arrive]
        while True:
            arrive = p[arrive]
            C.append(arrive)
            if arrive == depart:
                break
        return C

#MDL = liste()
#adjacence = adj(MDL)



