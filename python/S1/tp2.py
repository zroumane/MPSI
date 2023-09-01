print("EX 1 :")

def somme(L):
    s=0
    for i in range(len(L)):
      s+=L[i]
    return s
    
def somme_entiers(n):
    s = 0
    for i in range(n + 1):
        s+=i
    return s
    
    
print(somme_entiers(3))

def carres(n):
    L=[]
    for i in range(n):
      L.append(i**2)
    return L  
    
    
print(carres(10))

def somme_carres(n):
    return somme(carres(n))
    
    
print(somme_carres(10))

def reverse(L):
    LL=[]
    for i in range(len(L)):
        LL.append(L[len(L)-i-1])
    return LL
    
print(reverse([10,2,3]))


print("--------------------")
print("EX 3 :")

def dernier_7(L):
    n=0
    for i in range(len(L)):
        if L[i] == 7:
            n = i
    return n
    
print(dernier_7([0,0,7,0,0]))


def tous_les_7(L):
    G = []
    for i in range(len(L)):
        if L[i] == 7:
            G.append(i)
    return G
    

print(tous_les_7([7,0,7,0,0]))


def que_des_7(L):
    n = 0
    for i in range(len(L)):
        if L[i] == 7:
            n += 1
    return n == len(L)
    

print(que_des_7([0,7]))


print("--------------------")
print("EX 5 :")


def position_max(L):
    max = L[0]
    p = 0
    for i in range(len(L)):
        if L[i] > max:
            max = L[i]
            p = i
    return p
    

print(position_max([1,2,3,4,5,4,3,12,1]))


















































