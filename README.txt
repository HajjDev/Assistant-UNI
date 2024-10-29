README - Mission 6 - El Hajj Charbel

Ce programme est un outil de gestion de fichiers qui permet de travailler avec des fichiers texte en vérifiant leur présence,
en affichant des informations de base, en manipulant les mots contenus dans le fichier, et en exécutant des opérations de calcul sur des listes de nombres.

Fonctionnalités:
Le programme offre plusieurs commandes qui peuvent être entrées par l'utilisateur dans une interface
en ligne de commande pour interagir avec un fichier texte :

file <nom> : Sélectionne un fichier avec lequel le programme doit travailler.

info : Affiche le nombre de lignes et de caractères présents dans le fichier.

words : Convertit le fichier en une liste de mots (chaque ligne est considérée comme un mot).

search <mot> : Recherche un mot spécifique dans la liste de mots du fichier.

occurence <mot> : Recherche l'occurence d'un mot spécifique si il est mit dans la liste de mots.

sum <nombres> : Calcule la somme des nombres fournis par l'utilisateur.

avg <nombres> : Calcule la moyenne des nombres fournis par l'utilisateur.

modify <répertoire> : Change le répertoire de travail du programme.

directory : Affiche le répertoire de travail actuel.

help : Affiche les commandes disponibles et leur usage.

exit : Quitte le programme.


Utilisation:

Exécute le programme dans un terminal Python.

Utilise les commandes décrites ci-dessus pour interagir avec les fichiers du répertoire courant ou d'un autre répertoire choisi.

Tape help pour obtenir la liste des commandes à tout moment.

Exemples de commandes
file test.txt : Sélectionne test.txt comme fichier de travail.
info : Affiche le nombre de lignes et de caractères dans le fichier test.txt.
words : Convertit le fichier en une liste de mots.
search mot : Recherche le mot "mot" dans la liste de mots.
occurence mot : Recher l'occurence du mot "mot" dans la liste.
sum 5 10 15 : Calcule la somme des nombres (sortie : 30).
avg 5 10 15 : Calcule la moyenne des nombres (sortie : 10).


Avertissements

Assurez-vous que le fichier sélectionné existe dans le répertoire de travail actuel, sinon une erreur FileNotFoundError sera levée.

Pour utiliser les fonctions words et search, le fichier doit contenir une liste de mots séparés par des retours à la ligne sans espaces.

