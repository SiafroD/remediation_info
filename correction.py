from random import *
from math import *

#Exercice 0
"""
Stockage de variable
"""

'''
On nous fournit deux variables (a et b),
et on souhaite inverser leurs valeurs (a devient b et b devient a)
'''
a = randint(1, 10)
b = randint(11, 20)
print(a,b) #valeurs initiales de a,b
#écrire le programme ici
a,b = b,a
'''On peut aussi faire ça sous la forme de [a,b] = [b,a] ou (a,b)=(b,a), le tout est de faire l'inversion en même temps pour éviter d'écraser une variable avant de l'avoir échangée
'''
print(a, b) #valeurs de a,b après l'inversion

#Exercice 1

'''
Stockage de variable
Changement de types
Incrémentation de variables
'''

'''
On nous fournit un nombre de type chaine de caractère, 
et on souhaite l'incrémenter de n (nombre aléatoire), 
en ayant tout de même notre nombre sous la forme d'une 
chaine de caractère à la fin de l'exécution
'''

n = str(randint(1,10)) #nombre auquel on souhaite ajouter une valeur
a = randint(1,10) #valeur que l'on souhaite ajouter

#écrire le programme ici
n = str(int(n) + a)
'''
Ici, on convertit n en entier, auquel on ajoute ensuite a, pour de nouveau le convertir en chaine de caractères
'''




#Exercice 2

'''
Stockage de variable
Incrémentation de variables
Fonctions
Listes
Boucles
'''

'''
Ici, on veut sommer tous les entiers d'une liste et renvoyer cette somme à l'aide d'une fonction (que l'on définira)
Il faut donc faire :
- La fonction
- L'appel de fonction
'''

liste = [i for i in range(0,10)]

#écrire le programme ici
def somme(l):
  s = 0
  for a in l:
    s+=a
  return s

print(somme(liste))
'''
Ici, on crée une variable à laquelle on additionnera chaque élément "a" lorsqu'on parcourra la liste (grâce à la boucle for)
'''

#Exercice 3
'''
Stockage de variable
Changement types
Fonctions
Listes
Boucles
'''

'''
Ici, on va définir une fonction permettant de mélanger deux chaines de caractères

Exemple :

mot 1 : o u i
mot 2 :  n o n

Résultat après appel de la fonction : onuoin

Il faudra donc faire :

- La définition de la fonction
- L'appel de la fonction
'''

mot1 = "fcceu"
mot2 = "ukrgt"

#écrire le programme ici
def merge(un,deux):
  a = 0
  b = 0
  res = ""
  while a < len(un) and b < len(deux):
    res += un[a]
    res += deux[b]
    a += 1
    b += 1
  if a == len(un):
    res += deux[a:]
  elif b == len(deux):
    res += un[b:]
  return res

print(merge(mot1,mot2))
    

'''
Le programme au-dessus peut être raccourci, seulement j'ai choisi de programmer l'éventualité où les deux chaines seraient de longeurs différentes. Dans ce cas-là, le reste de la chaine la plus longue, qui n'a pas été fusionné, sera ajouté à la fin de la chaine de caractère.
'''






#Exercice 4


'''
Stockage de variable
Boucles
Conditions
'''
'''
Maintenant, on va essayer de créer une sorte d'interface utilisateur, afin de :
- Lire les données d'une liste
- Editer les données d'une liste

Pour cela, on utilisera la fonction input() qui, lors de la lecture de la ligne, demandera à l'utilisateur de saisir une donnée
Celle ci peut être récupérée par le programme en stockant le résultat de l'input dans une variable
On basera ensuite nos conditions dessus
'''


#Exemple d'utilisation de input():
#nom = input("Veuillez saisir votre nom :") #Stocke le nom donné par l'utilisateur dans la variable nom
#print(nom)

#écrire le programme ici
def interface(liste):
  q = input("Voulez-vous : Lire ou éditer la liste? [l/e]") #demande du choix de l'utilisateur
  while q not in ["l","e"]: #tant que l'utilisateur ne rentre pas de valeur permise
    q = input("Voulez-vous : Lire ou éditer la liste? [l/e]") #on redemande
  if q == "l": #cas où l'utilisateur souhaite juste voir la liste
    print(liste)
  else:
    q2 = input("Voulez-vous ajouter,supprimer,editer ou echanger une variable? [aj/sup/edi/ech]")
    while q2 not in ["aj","sup","edi","ech"]:
      q2 = input("Voulez-vous ajouter,supprimer,editer ou echanger une variable? [aj/sup/edi/ech]")
    if q2 == "aj":
      q3 = input("Que voulez vous ajouter?")
      liste.append(q3)
    elif q2 == "sup":
      q3 = input("Quel est l'indice de l'élément que vous souhaitez supprimer?")
      while q3 >= len(liste):
        q3 = input("Quel est l'indice de l'élément que vous souhaitez supprimer? (Indice précédent non valide)")
      del liste[q3]
    elif q2 == "edi":
      q3 = input("Quel est l'indice de l'élément que vous souhaitez éditer?")
      while q3 >= len(liste):
        q3 = input("Quel est l'indice de l'élément que vous souhaitez éditer? (Indice précédent non valide)")
      q4 = input("Que voulez-vous mettre à la place ?")
      liste[q3] = q4
    else:
      q3 = input("Quel est l'indice de l'élément que vous souhaitez échanger?")
      while q3 >= len(liste):
        q3 = input("Quel est l'indice de l'élément que vous souhaitez échanger? (Indice précédent non valide)")
      q4 = input("Quel est l'indice du second élément que vous souhaitez échanger?")
      while q4 >= len(liste):
        q4 = input("Quel est l'indice du second élément que vous souhaitez échanger? (Indice précédent non valide)")
  return None


    
