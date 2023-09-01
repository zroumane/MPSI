n = 2
M = [[1,2], [3,4]]

def replace(N, i, a):
    N[i] = [c*a for c in N[i]]
    return N

def switch(N, i, ii):
    t = N[i]
    N[i] = N[ii]
    N[ii] = t
    return N

def switch_replace(N, i, ii, a):
    N[i] = [N[i][j] + a * N[ii][j] for j in range(n)]
    return N


# Algorithme de Gauss Jordan
def inverse():
    global M
    global n
    I = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    d = 0
    while d < n:
        if M[d][d] == 0:
            for i in range(d+1, n):
                if M[i][d] != 0:
                    I = switch(I, d, i)
                    M = switch(M, d, i)
                else:
                    if i == n - 1:
                        raise Exception("Matrice non inversible")
            continue
        elif M[d][d] != 1:
            I = replace(I, d, 1/M[d][d])
            M = replace(M, d, 1/M[d][d])
        for i in range(n):
            if i != d and M[i][d] != 0:
                I = switch_replace(I, i, d, -M[i][d])
                M = switch_replace(M, i, d, -M[i][d])
        d+=1
    
    return I


# Cas particulier des matrices d'odre 2
def odre2():
    global M
    global n
    d = M[0][0]*M[1][1] - M[0][1]*M[1][0]
    if d == 0:
        raise Exception("Matrice non inversible")
    t = M[0][0]
    M[0][0] = M[1][1]
    M[1][1] = t
    M[1][0] = - M[1][0]
    M[0][1] = - M[0][1]
    return [(1/d * c for c in L) for L in M]


def show(N):
    print("\n".join(['| ' + " ".join([str(c) for c in L]) + ' |' for L in N]))


if M != []:
    try:
        if len(M) != n:
            raise Exception("Nombre de ligne invalide")
        for i in range(n):
            if len(M[i]) != n:
                raise Exception(f"Nombre d'élements ligne {i+1} invalide")
    except Exception as t:
        print(str(t))
        input()
        exit()
else:
    n = int(input("Ordre : "))
    for i in range(n):
        M.append([])
        for j in range(n):
            M[i].append(input(f"L{i+1} C{j+1}: "))
  
  
try:
    M = [[float(M[i][j]) for j in range(n)] for i in range(n)]
except:
    print("Type invalide")
    input()
    exit()

print("Matrice :")
show(M)

I = []

try:
    if n == 2:
        I = odre2()
    else :
        I = inverse()
    print("Inverse :")
    show(I)
except Exception as t:
    print(str(t))