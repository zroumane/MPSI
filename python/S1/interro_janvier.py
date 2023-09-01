# Ce fichier sera votre copie.
# Enregistrez-le dans "Ma classe / Restitution de devoirs / NOM_Prenom.py " avant 16h25.

"""
Trouver le pic :
On a en entrée une liste L donnant la population d'un village pays année après année.
On sait la chose suivante :
Au début de la liste, la population augmente. Elle atteint un maximum puis se met à diminuer jusqu'à la fin de la liste.

Définir une fonction  pic(L)  qui renvoie la plus grande valeur de la liste, en utilisant une recherche dichotomique pour trouver l'endroit où l'augmentation finit et la diminution commence.

Exemples :
pic([3,9,17,31,38,29,21,15]) renvoie 38
pic([11, 15, 16, 24, 25, 27])=27
pic([26, 25, 24, 24, 19, 16, 12])=26
"""

"""
Énumération de combinaisons :
On noter P(n,p) l'ensemble des parties à p éléments de l'ensemble [1,2,.... n]
Écrire une fonction  combinaisons(n,p) qui énumère ces parties.
Conseil : utiliser une fonction récursive, en remarquant que :
 Si n=0 ou p=0, P(n,p)={ ∅ }
 P(n,p) = P(n-1,p) U { S U {n} | S ∈ P(n-1,p-1) }

Exemple :
 P(2,0)=[ [] ]
 P(5,3) renvoie : [ [1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5] ]
"""

def P(n, p):
  if n == 0 or p == 0:
   return [[]]
  elif n == p:
   return [[k for k in range(1, n + 1)]]
  else:
   L = []
   for i in P(n-1, p-1):
    L += [n] + i
   L += [P(n-1, p)]
   return L



"""
On a deux images "Avant.png" et "Apres.png" dans le dossier de la classe.

Copier l'image "Apres.png", identifier quels pixels ont été modifiés et changer ces pixels en rouge.
Enfin, afficher cette image.

"""

"""
La fonction atan2(y,x) du module math calcule l'angle (en radians) entre le vecteur (1,0) et le vecteur (x,y).
Attention à l'ordre de ses deux arguments.

On a en entrée une liste de vecteurs [(x1,y1), (x2,y2), .... (xn,yn)]

Trier cette liste par angle croissant

Exemple :
tri([ (2,2),(4,1),(4,3)] )  renvoie [(4,1),(4,3),(2,2)]
"""




