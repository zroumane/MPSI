def nouvelle_grille():
    return [['.' for _ in range(7)] for _ in range(6)]


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
                        print(t, p)
                    else:
                        break
        if t >= 4:
            return True
    return False

def pleine(G):
    for l in G:
        for c in l:
            if c == '.':
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
    mark = ['X', 'O']
    i = 0
    G = nouvelle_grille()
    while True:
        afficher(G)
        i = 0 if i == 1 else 1
        c = demande_colonne(G, mark[i])
        l = jouer_coup(G, c, mark[i])
        if gain(G, l, c):
            afficher(G)
            print(mark[i], 'win')
            break
        if pleine(G):
            afficher(G)
            print('draw')
            break




partie()
input()














