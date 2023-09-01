from random import randint
mots = open("H:\mpsi\info\python\S2\dico_AZ.txt").readlines()
l = len(mots)

def match(filtrage):
    M = []
    m = list(filter(lambda x: len(x) - 1 == len(filtrage),  mots))
    for c in range(len(m)):
        s = True
        for i in range(len(filtrage)):
            if filtrage[i] != '-' and filtrage[i] != m[c][i]:
                s = False
        if s:
            M.append(m[c])
    return M


def choisir_lettre(filtrage, lettres):
    M = []
    if filtrage == '-'*len(filtrage):
        M = list(filter(lambda x: len(x) - 1 == len(filtrage),  mots))
    else:
        M = match(filtrage)
    dict = {}
    for i in range(len(filtrage)):
        if filtrage[i] == '-':
            for c in M:
                if c[i] not in lettres:
                    if c[i] in dict:
                        dict[c[i]] += 1
                    else:
                        dict[c[i]] = 1
    return max(dict, key=dict.get)



def filtre(mot, lettres):
    return "".join([i if i in lettres else "-" for i in mot])

def gagne(mot, lettres):
    for i in mot:
        if i not in lettres:
            return False
    return True

def demander_lettre(lettres):
    R = input('> ')
    if (len(R) != 1) or (R in lettres) or (ord(R) < 65 or ord(R) > 90):
        return demander_lettre(lettres)
    return R


def jeu(mot, bot = False, p = True):
    if bot:
        print(mot)
    lettres = []
    vies = 11
    while vies != 0:
        C = filtre(mot, lettres)
        if p:
            print(C)
            print(",".join(lettres))
            print('Vie :', vies)
        R = ""
        if bot:
            R = choisir_lettre(C, lettres)
        else:
            R = demander_lettre(lettres)
        lettres.append(R)
        if R not in mot:
            vies -= 1
        if gagne(mot, lettres):
            if p:
                print('Gagné')
            return vies
    if p:
        print("Perdu")
    return 0

def mot_alea():
    return mots[randint(0, l)][:-1]

def bot():
    return jeu(mot_alea(), True)

def play():
    jeu(mot_alea())

def test(n):
    s = 0
    for i in range(n):
        s += 11 - jeu(mot_alea(), True, False)
    print('Moyenne vies perdus :', s/n)




test(10)
input()