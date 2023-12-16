import matplotlib.pyplot as plt

path1 = "F:\mp\info\python\doc\pendule.png"
path2 = "F:\mp\info\python\doc\cachee.png"
    
def barycentre(x):  
    abscisse = []
    ordonnees = []
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j][1] <= 0.45*(x[i][j][0] + x[i][j][2]):
                abscisse.append(i)
                ordonnees.append(j)
    return (round(sum(abscisse)/len(abscisse)), round(sum(ordonnees)/len(ordonnees)))


def hide(x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            for k in range(4):
                c = int(x[i][j][k]*255)
                x[i][j][k] = ((c % (2**4))*2**4)/255
    return x
    

def _1_():
    x1 = plt.imread(path1).tolist()
    i, j = barycentre(x1)
    x1[i][j] = [1,0,0]
    plt.imshow(x1)

def _2_():
    x2 = plt.imread(path2).tolist()
    plt.imshow(hide(x2))

_1_()
plt.show()
