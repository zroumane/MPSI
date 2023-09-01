
def bool_progression_arithmetique(L):
    n = L[1] - L[0]
    for i in range(len(L)-1):
        if L[i + 1] - L[i] != n:
            return False
    return True
    
print(bool_progression_arithmetique([10,14,18,22]))

def concate_list(A, B):
    L = []
    for i in range(len(A)):
        L.append([ A[i], B[i] ])
    return L
    
    
print(concate_list([1, 2, 3, 4], [1, 2, 3, 4]))
    
    
def reverse_between(a, b, L):
    G = []
    for i in range(len(L)):
        if i >= a and i <= b :
            G.append(L[b + a - i ])
        else:
            G.append(L[i])
    return G
    
print(reverse_between(1,3,[78,10,69,43,8,32,24,83,71,94]))


def factorielle(n):
    s = 1
    for i in range (1, n + 1):
        s*=i
    return s
    
print(factorielle(4))

def produit_list(A, B):
    L = []
    for i in range(len(A)):
        L.append(A[i]*B[i])
    return L
    
print(produit_list([3,0,6,2,-7], [2,10,-2,8,12]))


def same_position(A, B):
    s=0
    for i in range(len(A)):
        if A[i] == B[i]:
            s+=1
    return s
    
print(same_position([6,0,2,8,-7], [5,0,8,6,-7]))



def find():
    for i in range(1000):
        for j in range(1000):
            for k in range(1000):
                if i + j + k == 1000 and i**2 + j**2 == k**2:
                    return [i,j,k]

print(find())



u=[5]
for n in range(1, 100):
    u.append((3*u[n-1]-1)/4)
print(u)



def est_premier(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
    


s = 0
for i in range(100):
    s+=i
print(s)




















