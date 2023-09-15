import csv
import matplotlib.pyplot as plt


def exo2():
    f = open("Q:\\Documents en consultation\\metro.csv")
    l = list(csv.reader(f, delimiter=';'))[1:]

    dict = {}

    for k in l:
        if k[0] in dict:
            dict[k[0]] += 1
        else:
            dict[k[0]] = 1

    L = []
    G = []
    for k in dict.keys():
        if dict[k] > 1:
            L.append(k)
        if dict[k] >= 3:
            G.append(k)

    print(len(L), len(G))


def exo3():
    f = open("F:\\mpsi\\info\\python\\S2\\traces-du-reseau-ferre-idf.csv")
    l = list(csv.reader(f, delimiter=';'))[1:]

    for k in l:
        if k[11] == '1.0':
            d = eval(k[1])
            X = [i[0] for i in d["coordinates"]]
            Y = [i[1] for i in d["coordinates"]]
            c = k[19].upper()
            if len(c) != 6:
                c = 'AAAAAA'
            plt.plot(X, Y, '-', color = '#' + c)

    plt.xlim(2.241892, 2.433588)
    plt.ylim(48.811180, 48.903683)
    plt.show()