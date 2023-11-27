from html.parser import HTMLParser
import requests



def grille(str):
    M = []
    for i in range(9):
        M.append([])
        for j in range(9):
            M[-1].append(int(str[9*i+j]))
    return M



def convert(cheat, editmask):
    str = ""
    for i in range(len(cheat)):
        str += cheat[i] if editmask[i] == '0' else '0'
    return grille(str)


def candidat(M):
    for i in range(9):
        for j in range(9):
            if M[i][j] == 0:
                return (i, j)

def valeur(M, candidat):
    RM = set()
    i, j = candidat
    for k in range(9):
        RM.add(M[i][k])
        RM.add(M[k][j])
    bi, bj = (i // 3)*3, (j // 3)*3
    for l in range(3):
        for c in range(3):
            RM.add(M[bi + l][bj + c])
    return list(set(range(10)).difference(RM))


def resolve(M):
    c = candidat(M)
    if c == None:
        return True, M
    else:
        L = valeur(M, c)
        for l in L:
            M[c[0]][c[1]] = l
            res = resolve(M)
            M[c[0]][c[1]] = 0
            if res[0]:
                return res
        return False, []




cheat = "728316594193245876456789231982471365567923418341568729879634152215897643634152987"
editmask = "010001111111111001001110101011011010100101001010110110101011100100111111111100010"
M = convert(cheat, editmask)



