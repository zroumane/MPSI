
def dist(A, B):
    return sum([(B[i] - A[i])**2 for i in range(len(A))])

def indice_min(L):
    m = 0
    for i in range(len(L)):
        if L[i] < L[m]:
            m = i
    return m

import csv
D_E_str = list(csv.reader(open("E:\mp\info\python\doc\donnees_entrainement.csv")))
D_E = [[int(x) for x in l] for l in D_E_str]
D_T_str = list(csv.reader(open("E:\mp\info\python\doc\donnees_test.csv")))
D_T = [[int(x) for x in l] for l in D_T_str]


import matplotlib.pyplot as plt

def cut(L):
    G = []
    for i in range(8):
        G.append([L[i*8 + k] for k in range(8)])
    return G

def show(L):
    plt.imshow(cut(L), cmap="gray_r", interpolation="None")

def toutes_distances(L):
    return [dist(L, G) for G in D_E]

C_E_str = list(open("E:\mp\info\python\doc\chiffres_entrainement.txt"))
C_E = [int(x) for x in C_E_str]


import time

def predict(k):
    G = []
    I = []
    D = toutes_distances(D_T[k])
    for i in range(len(D_T)):
        if i != k:
            G.append(D[i])
            I.append(i)
    return C_E[I[indice_min(G)]]


def test(s):
    P = []
    t = 0
    for i in range(s):
        st = time.time()
        P.append(predict(i))
        t += time.time() - st
    return t/s, P


C_T_str = list(open("E:\mp\info\python\doc\chiffres_test.txt"))
C_T = [int(x) for x in C_T_str]

def matrice(P):
    M = [[0 for i in range(10)] for k in range(10)]
    for k in range(len(P)):
        M[P[k]][C_T[k]] += 1
    return M

def show_matrice(M):
    for m in M:
        print(m)

#P = test(100)[1]
P = [predict(i) for i in range(len(D_T))]
show_matrice(matrice(P))


#[178, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#[0, 180, 1, 1, 6, 0, 0, 0, 9, 0]
#[0, 0, 176, 0, 0, 0, 0, 0, 0, 0]
#[0, 0, 0, 179, 0, 0, 0, 0, 1, 5]
#[0, 0, 0, 0, 173, 1, 0, 1, 0, 3]
#[0, 0, 0, 0, 0, 178, 0, 0, 0, 7]
#[0, 2, 0, 0, 0, 1, 181, 0, 1, 0]
#[0, 0, 0, 0, 0, 0, 0, 172, 0, 0]
#[0, 0, 0, 2, 2, 0, 0, 1, 160, 2]
#[0, 0, 0, 1, 0, 2, 0, 5, 3, 163]