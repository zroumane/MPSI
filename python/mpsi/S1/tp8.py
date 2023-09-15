print('\nQ2')

def triangle(n):
    if n != 1:
        triangle(n-1)
    print('A'*(n))

triangle(3)

print('\nQ3')

def triangle_bas(n):
    print('A'*n)
    if n != 0:
        return triangle_bas(n-1)

triangle_bas(3)


print('\nQ4')

def recrange(n):
    L = []
    if n == 0:
        return L
    else:
        L = recrange(n-1)
        L.append(n)
        return L

print('\nQ4')
print(recrange(10))



print('\nQ5')

def fact(n):
    if n == 1:
        return n
    return n * fact(n-1)

print(fact(3))


print('\nQ6')

def ecriture(s):
    s = str(s)
    L = [s[0]]
    if len(s) == 1:
        return L
    else :
        return L + ecriture(s[1:len(s)])

print(ecriture(1739))


print('\nQ7')

def permutation(L):
    if len(L) == 1:
        return [L]

    R = []
    for l in L:
        G = [x for x in L if x != l]
        Z = permutation(G)

        for z in Z:
            R.append([l] + z)

    return R


print(permutation([1,2,3]))


































