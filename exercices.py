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
La fonction doit donc être capable de prendre en entrée n'importe quelle liste.
Il faut donc faire :
- La fonction
- L'appel de fonction
'''

liste = [i for i in range(0,10)] #liste test

#écrire le programme ici



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

liste = [1,2,0,"oui",(4,7)]
#Exemple d'utilisation de input():
#nom = input("Veuillez saisir votre nom :") #Stocke le nom donné par l'utilisateur dans la variable nom
#print(nom)

#écrire le programme ici



#Exercice 5 : Mini projet
'''
Stockage de variable
Listes
Boucle
Conditions
Fonctions
'''

'''
Ici, pour les plus motivés, on programmera un puissance 4 fonctionnel
On représentera le tableau de jeu par une liste de listes
On définira les dimensions du tableau grace à deux variables (afin de pouvoir faire varier la taille du tableau de jeu)
On fera plusieurs fonctions qui définiront un tour de jeu:
- la fonction placer, qui gère le placement d'une nouvelle pièce
- la fonction vérifier, qui regarde si il n'y a pas de vainqueur à la fin du tour
'''



#Exercice n
'''
Stockage de variable
Incrémentation de variables
Boucles
Conditions
Récursivité
'''

'''
Ici, on va s'attaquer à une fonction mathématique connue, qui a pour caractéristique de :
- Renvoyer 3n+1 lorsque n est impair
- Renvoyer n/2 lorsque n est pair
- Ne s'arrêter que lorsque notre valeur de n vaut 1
Il va donc falloir utiliser de la récursivité afin de faire les appels de fonction, en n'oubliant pas le cas de base nous assurant que la fonction s'arrête (même si ça n'est pas prouvé mathématiquement)

On veut savoir au bout de combien d'exécutions la fonction est arrivée à 1
'''








