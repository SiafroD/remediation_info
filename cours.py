'''
Sommaire :
- Stockage de variable
- Types
- Incrémentation de variables
- Fonctions
- Listes
- Commandes utiles
- Boucles
- Conditions
- Assertions
- Messages d'erreur
- Récursivité
'''


#Stockage de variable
'''
Une variable se stocke en utilisant un unique =
'''
#Exemple :
x = 1

#Types
'''
En python, on a à notre disposition plusieurs types de variables : 
- les entiers : int 
- les nombres décimaux : float (la virgule est représentée par un . en python)
- les chaines de caractères : str (contenues dans des apostrophes)
- les listes : list (contenues dans des crochets)
- les dictionnaires : dict (contenus dans des accolades)
'''
#Exemple
a = 47 #entier
b = 47.0 #flottant(nombre décimal)
c = "47" #chaine de caractères
d = [4,"7"] #liste
e = {"4" : 7} #dictionaire

#Incrémentation de variables
'''
Pour les variables de type int, on peut les incrémenter/décrémenter de façon simple
'''
#Exemple
a = 1
a += 1 #OU a = a + 1
#==> a vaut donc 2
a -= 1 #OU a = a - 1
#==> a vaut donc 1
a *= 2 #OU a = a * 2
#==> a vaut donc 2
a /= 2 #OU a = a / 2
#==> a vaut donc 1

#Opérateurs mathématiques

a%b #Modulo, renvoie le reste de la division de a par b
a//b #Division entière, renvoie le quotient de a par b (arrondi à l'unité infèrieure)


#Fonctions
'''
Sur python, on peut définir des fonctions, qui permettront de rendre le code plus visible et plus sécurisé (principe de variables locales)
Il y a une synthèse bien spéciale à respecter lors de la définition de fonctions :
'''
def fonction(argument1,argument2,argumentn):

'''
Dans une fonction, on peut utiliser plusieurs méthodes afin de renvoyer les valeurs dont on a besoin :
- print(valeur) ==> permet d'afficher directement notre réponse, mais fait que la fonction renvoie un objet de type NoneType
- return valeur ==> n'affiche pas la valeur, mais fait que la fonction renvoie la valeur
'''


#Exemple 1

def carre(x):
  print(x**2)
'''
Appels possibles :
- carre(x) ==> affichera x²
- a = carre(x) ==> a vaudra NoneType, car il n'y a aucune valeur liée à carre(x)
'''



#Exemple 2

def carre(x):
  return x**2
'''
Appels possibles :
- carre(x) ==> n'affichera rien
- a = carre(x) ==> a vaudra x²
- print(carre(x)) ==> affichera x²
'''


#Listes
'''
En python, une liste est un type très utile pour le stockage de données, car elle peut être parcourue et modifiée très facilement
'''
#Exemple
liste = [1,2,3]
'''
Pour accéder à un élément d'une liste, on effectue la commande liste[indice]
, indice étant la place de l'élément auquel on souhaite accéder (ATTENTION : le premier indice d'une liste est 0 et non 1)
'''
#Exemple
liste[1] #==> 2
liste[0] #==> 1

#Indices utiles :
liste[-1] #Renvoie le dernier élément de la liste
'''
Une liste peut aussi être parcourue dans le sens inverse, donc de droite à gauche, en utilisant des indices négatifs, partant de -1 et allant jusqu'à -len(liste)
'''
liste[i:] #Renvoie tous les éléments après l'élément d'indice i compris
liste[:i] #Renvoie tous les éléments avant l'élément d'indice i non compris

#Exemples: 
liste = [1,2,3,4,5,6]
liste[2:] #==> [3,4,5,6]
liste[:3] #==> [1,2,3] 

'''
Il est aussi possible de faire des listes de liste :
'''
liste = [[0,1],[2,3]]
liste[0] #Renvoie la liste [0,1]
liste[1][0] #Renvoie l'entier 2

'''
Lorsqu'on veut ajouter un élément à la fin de la liste, on utilise la fonction .append()
'''
#Exemple :
liste=[1,2]
liste.append(5)  #==> liste=[1,2,5]


'''
Il est aussi possible d'accéder à un indice depuis l'élément /!\ Peut malfonctionner lorsqu'on veut accéder à un élément présent en double /!\
Pour cela, on fait
'''
liste.index(elem) #Renvoie l'indice de elem dans liste

#Commandes utiles

#Changement de types :
a = int(a) #Passage en entier /!\ ne se fait que sur des chaines de caractères composées de nombres (on ne peut pas transformer directement une liste en entier)
b = float(b) #Passage en flottant /!\ même précautions que pour int + attention à utiliser le point et non la virgule comme séparateur
c = str(c) #Passage en chaine de caractères /!\ ne se fait que sur des nombres (on ne peut pas transformer directement une liste en chaine de caractères)

#nota bene : str peut être appliqué à un élément de type déjà str, ça ne fait juste aucun changement, et pareil pour int ou float 
'''
Utile :
On peut lire une chaine de caractère comme étant une liste.
'''
#Exemple

s = "Emmanuel"
s[0] #==> Renvoie "E"
s += "l" #==> Transforme "Emmanuel" en "Emmanuell"

#Longueur :
len(s) #Renvoie la longueur de la chaine de caractères/la liste/le dictionnaire s

#Boucles
'''
En python, il existe différents types de boucles :
- Les boucles while (munies d'une condition d'arrêt)
- Les boucles for
'''

#Boucles while

'''
Une boucle while est une boucle qui va s'exécuter tant qu'une certaine condition continue de se réaliser
'''

#Exemple 
while condition:
  print("oui")

#Cette fonction affichera "oui" tant que la condition est à True (précisions dans la prochaine catégorie)

#Boucles for

'''
Les boucles for se déclinent en deux styles différents (et aux utilités différentes)
'''

#Boucles for in

'''
Les boucles for in vont permettre de parcourir un à un les éléments d'une variable
Elles sont utilisées lorsqu'on a principalement besoin des éléments et non des indices
'''

#Exemple

a = [1,2,3]
for i in a:
  print(i)

#Ici, on va afficher 1, puis 2, puis 3


#Boucles for in range()

'''
Les boucles for in range() vont permettre d'incrémenter une variable entre des bornes spécifiées
Elles sont utilisées lorsqu'on a majoritairement besoin des indices et non des éléments.
'''

#Exemple

for i in range(0,10,1):
  print(i)

#Ici, on va afficher tous les entiers de 0 à 10 (exclus) avec un pas de 1
'''
Les boucles for in range n'ont pas obligatoirement besoin de la borne de départ et du pas pour fonctioner. Si ils ne sont pas spécifiés, la borne de départ sera mise à 0 et le pas à 1.

Ces boucles seront principalement utilisées pour parcourir des listes à partir des éléments. Une utilisation fréquente est :
'''
for i in range(len(liste)):
  print(liste[i])

#Affiche tous les éléments de la liste

'''
Pour sortir d'une boucle sans utiliser de condition dans la définition de la boucle, on peut utiliser break
'''

#Exemple
i = 0
while True:
  i+=1
  if i == 10:
    break

#Nous fait sortir d'une boucle infinie lorsqu'on atteint i = 10



#Conditions

#booléen

'''
Un booléen est un type de variable qui vaut soit True, soit False. 
On va pouvoir utiliser des comparaisons (égalités, inégalités), afin de les utiliser dans nos conditions
'''
#Exemples de comparaisons
== #est égal
!= #n'est pas égal
< #est strictement inférieur
> #est strictement supérieur
<= #est inférieur ou égal
>= #est supérieur ou égal
in #est dans
not() #non(condition)

"""
/!\ Les calculs étant fait en binaire par l'ordinateur, les égalités entre flottants sont périlleuses.
En effet des nombres décimaux qui semblent anodins en base 10, ont une écriture infinie en binaire, comme 1/3 pour nous (1.33333333)
"""
a = 0.3
print(a) #affiche 0.3
a = 0.2
a += 0.1
print(a) #affiche 0.300000004
print(a == 0.3) #False
	
'''
En python, les conditions sont la base des programmes avancés, car elles permettent aux programmes de s'adapter'''

#Conditions principales :

if condition:

#Passe à ce bloc seulement si condition vaut True

elif condition2:

'''
/!\ Doit être mis après un bloc if /!\
L'état de la condition n'est vérifié que si le bloc if/elif précédent n'a pas été réalisé
'''

else:

'''
/!\ Doit être mis après un bloc if /!\
Le bloc sera lu seulement si toutes les conditions précédentes ne sont pas vérifiées
'''


#Assertions

'''
Les assertions sont utilisées pour vérifier que des variables respectent une certaine condition
'''

#Exemple 
assert condition

'''
Si la condition vaut True, le programme continuera d'être exécuté
Si la condition vaut False, le programme plantera et renverra une AssertionError
'''

#Messages d'erreur

'''
Voici une liste non-exhaustive des messages d'erreurs que vous pourrez rencontrer lors de vos exécutions de programme : 
- AssertionError : une condition d'assert n'a pas été vérifiée
- TypeError : vous avez essayé d'effectuer une opération qui n'est pas compatible avec le type de la variable utilisée (par exemple, une somme sur une chaine de caractères, ou un .append() sur un entier).
- SyntaxError : Erreur de syntaxe : Il faut lire le message d'erreur plus en détail pour trouver ce qui ne fonctionne pas (peut être une erreur d'indentation, des : manquants, etc...)
- IndexError : On ne peut pas accéder à l'élément de la liste à l'indice spécifié (le plus souvent codé par un indice plus grand que le maximum de la liste)
- Maximum recursion depth exceeded: Le programme est soit trop lent, soit infini. Regarder attentivement le message permet de savoir quelle condition est à changer (dans une boucle while par exemple)
'''
#Récursivité

#Récursivité


'''
Les fonctions récursives sont des types de fonction qu'on va retrouver en python et qui ont pour particularité de s'appeler elles-même dans leur
définition
Comme pour une boucle normale (itérative), il faut cependant penser à définir une condition d'arrêt. C'est pourquoi les fonctions récursives
vont souvent avoir un de leurs arguments là afin de garantir le bon arrêt de cette fonction.
Il faudra donc aussi une condition dans la fonction qui fait rentrer en jeu l'argument d'arrêt, condition appelée "cas de base"
Par exemple, pour la fonction factorielle, la fonction s'arrête quand la valeur sur laquelle on appelle notre fonction est 1 ou 0 (car on connait
leurs valeurs). Grace à cette remarque, on a donc notre argument d'arrêt et notre cas de base (argument : n (valeur sur laquelle on appelle fact),
cas : n in [0,1])
'''

def fact(n):
    if n in [0,1]: #cas de base
        return 1
    else:
        return n * fact(n-1) #au final, n! = n*(n-1)!
