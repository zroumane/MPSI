def tableau(u, p, L):
    n = len(u)
    M = []
    for t in range(L+1):
        M.append([])
        for i in range(n):
            if i == 0:
                M[t].append(0 if p[i] > t else u[i])
            else:
                M[t].append(max(M[t][i-1], 0 if t-p[i] < 0 else u[i] + M[t-p[i]][i-1]))
    return M


def solution(u, p, L):
    M = tableau(u, p, L)
    for m in M:
        print(m)
    L = []
    i, j = len(M) - 1, len(M[0]) - 1
    while i != 0 and j != 0:
        if M[i-1][j] != M[i][j]:
            j -= 1
        else:
            if len(L) == 0 or L[-1] != j:
                L.append(j)
                j -= 1
            i -= 1
    return L


u = [7, 8, 12, 10, 13, 15, 17]
p = [3, 4, 5, 5, 7, 8, 8]
L = 24
print(solution(u, p, L))
