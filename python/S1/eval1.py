# Ce fichier est votre copie. Vous pouvez y écrire vos programmes et l'enregistrer avant la fin de la séance, en faisant par exemple [CTRL + S], sans modifier son emplacement
# Vous trouverez plus bas le détail des fonctions à définir.
# Pour faire vérifier vos fonctions, taper test() dans le shell.

'''
Fonction cube(x):
 Renvoie le cube du nombre réel x
Exemples :
cube(2) doit renvoyer 8
cube(-3) doit renvoyer -27
'''

def cube(x):
  return x**3



'''
Fonction arrondi_log(n, k):
 Renvoie le logarithme DECIMAL (en base 10) de l'entier naturel n, arrondi k chifres après la virgule. On pourra se servir du module math et/ou de la fonction round.
Exemples :
arrondi_log(30,1) doit renvoyer 1.5
arrondi_log(46,3) doit renvoyer 1.663
'''
import math

def arrondi_log(n, k):
 return round(math.log10(n)*10**k)/(10**k)



'''
Fonction echange(L):
 La liste L est de longueur paire (inutile de le vérifier). Renvoyer une liste où on a échangé les moitiés gauche et droite de L
Exemples :
echange([10, 3, 7, 4]) doit renvoyer [7, 4, 10, 3]
echange([1, 12, 15, 5, 2, 5]) doit renvoyer [5, 2, 5, 1, 12, 15]
echange([]) doit renvoyer []
'''

def echange(L):
 G = []
 m = int(len(L)/2)
 for i in range(m, len(L)):
  G.append(L[i])

 for i in range(0, m):
  G.append(L[i])

 return G



'''
Fonction compte_vides(C):
 C est une liste qui contient des listes. Renvoyer le nombre de listes vides parmi les éléments de C
Exemples :
compte_vides([[], [5, 2], [], [14, 2], [16, 6, 19, 4], [], [4, 4, 12]]) doit renvoyer 3
compte_vides([[3, 11], [], []]) doit renvoyer 2
'''

def compte_vides(c):
 s = 0
 for l in c:
  if len(l) == 0:
   s+=1
 return s



'''
Fonction plus_proche(L, x):
 Renvoie l'élément de L qui est le plus proche de x.
Exemples :
plus_proche([3, 18, 9, 17, 11, 20, 13, 6],7) doit renvoyer 6
plus_proche([1, 3, 11, 9, 15],7) doit renvoyer 9
'''

def plus_proche(L, x):
 c = L[0]
 for i in range(len(L)):
  if abs(L[i])-x < abs(c-x):
   c = L[i]
 return c


'''
Fonction diagonale(R):
 R est une liste qui contient plusieurs listes, toutes de même longueurs. Renvoyer une liste contenant : le premier élément de la première liste, le deuxième élément de la deuxième liste, le troisième élément de la troisième liste, etc.
Exemples :
diagonale([]) doit renvoyer []
diagonale([[16, 12, 4, 12], [18, 19, 7, 1]]) doit renvoyer [16, 19]
diagonale([[1, 12], [9, 2], [3, 11]]) doit renvoyer [1, 2]
diagonale([[7, 20, 3], [11, 11, 19], [11, 16, 14]]) doit renvoyer [7, 11, 14]
'''

def diagonale(R):
 G = []
 s = 0
 for l in R:
  if len(l) <= s:
   continue
  G.append(l[s])
  s+=1
 return G




'''
Fonction superieur(A, B):
 A et B sont deux listes de même taille (inutile de le vérifier). Renvoyer True si chaque élément de A est supérieur à l'élément correspondant de B, et renvoyer False sinon.
Exemples :
superieur([3, 2, 7],[1, 1, 5]) doit renvoyer True
superieur([5, 2, 10, 3],[2, -2, 12, 8]) doit renvoyer False
'''


def superieur(A, B):
 b = True
 for i in range(len(A)):
  if A[i] < B[i]:
   b = False
 return b
















