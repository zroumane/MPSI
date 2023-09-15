print('ROUMANE Zephyr MPSI')


print('\nEX 1')

import random

# print([random.randrange(0, 100) for i in range(100)])


print('\nEX 2')

def randlist(N, M):
    return [random.randrange(0, M) for i in range(N)]


print('\nEX 3')

import time

s = time.time() 
l = randlist(10000, 500)
t1 = time.time() - s
print(f'10 000 nombres entre 0 et 500 : : {str(round(t1 * 1000))} ms')

s = time.time()
l = randlist(20000, 100)
t2 = time.time() - s
print(f'20 000 nombres entre 0 et 100 : : {str(round(t2 * 1000))} ms')

s = time.time()
l = randlist(30000, 10000)
t3 = time.time() - s
print(f'30 000 nombres entre 0 et 10000 : {str(round(t3 * 1000))} ms')


print('\nEX 4')

print('''
    Le paramètre M n'a pas d'influence sur la durée d'exécution car il n'ajoute pas d'operation
    ''')


print('\nEX 5')

print('''
    Si le paramètre N augmente la durée d'exécution augmente car la boucle est exécutée N fois
    ''')


print('\nEX 6')
print(f'''
    Si la durée d'exécution est proportionnel a N, 
    la génération de 60000 nombres devrait prendre environ {str(round(t3 * 60000 / 30000 * 1000))} ms
    ''')

s = time.time()
l = randlist(60000, 2000)
t4 = time.time() - s
print(f'60 000 nombres entre 0 et 2000 : : {str(round(t4 * 1000))} ms')


print('\nEX 7')

def indice_min(L):
    m = 0
    for i in range(len(L)):
        if L[i] < L[m]:
            m = i
    return m

print('\nEX 8')

L = randlist(10000,100)
s = time.time()
l = indice_min(L)
t5 = time.time() - s
print(f'indice_min sur une liste de 10000 nombres : {str(round(t5 * 1000))} ms')

print(f'''
    Si la durée d'exécution est proportionnel a la taille de la liste en paramètre, 
    indice_min sur 30000 nombres devrait prendre environ {str(round(t5 * 30000 / 10000 * 1000))} ms
    ''')

L = randlist(30000,100)
s = time.time()
l = indice_min(L)
t6 = time.time() - s
print(f'indice_min sur une liste de 30000 nombres : {str(round(t6 * 1000))} ms')


print('\nEX 9')

def supprime(L, i):
    G = []
    for j in range(len(L)):
        if i != j:
            G.append(L[j])
    return G



print('\nEX 10')

print('''
    Si le paramètre N augmente la durée d'exécution car la boucle est exécutée len(L) fois,
    le paramètre i n'a donc pas d'influence
    ''')


print('\nEX 11')

L = randlist(10000, 100)
s = time.time()
supprime(L, 2000)
t7 = time.time() - s
print(f'supprime sur une liste de 10000 nombres avec i = 2000: {str(round(t7 * 1000))} ms')

L = randlist(10000, 100)
s = time.time()
supprime(L, 8000)
t8 = time.time() - s
print(f'supprime sur une liste de 10000 nombres avec i = 8000: {str(round(t8 * 1000))} ms')

L = randlist(30000, 100)
s = time.time()
supprime(L, 10000)
t9 = time.time() - s
print(f'supprime sur une liste de 30000 nombres avec i = 10000 : {str(round(t9 * 1000))} ms')

L = randlist(30000, 100)
s = time.time()
supprime(L, 20000)
t9 = time.time() - s
print(f'supprime sur une liste de 30000 nombres avec i = 20000 : {str(round(t9 * 1000))} ms')


print('\nEX 12')

def trie_insertion(L):
    R = []
    while len(L) != 0:
        m = indice_min(L)
        R.append(L[m])
        L = supprime(L, m)
    return R


print('\nEX 13')

L = randlist(1000, 10000)
s = time.time()
trie_insertion(L)
t10 = time.time() - s
print(f'trie_insertion sur une liste de 1000 nombres : {str(round(t10 * 1000))} ms')

L = randlist(2000, 10000)
s = time.time()
trie_insertion(L)
t11 = time.time() - s
print(f'trie_insertion sur une liste de 2000 nombres : {str(round(t11 * 1000))} ms')

L = randlist(3000, 10000)
s = time.time()
trie_insertion(L)
t12 = time.time() - s
print(f'trie_insertion sur une liste de 3000 nombres : {str(round(t12 * 1000))} ms')



print('\nEX 14')

print(f'''
    Si la durée d'exécution est proportionnel a la taille de la liste en paramètre, 
    trie_insertion sur 4000 nombres devrait prendre environ {str(round(t12 * 4000 / 3000 * 1000))} ms
    ''')

L = randlist(4000, 10000)
s = time.time()
trie_insertion(L)
t13 = time.time() - s
print(f'trie_insertion sur une liste de 3000 nombres : {str(round(t13 * 1000))} ms')

































































