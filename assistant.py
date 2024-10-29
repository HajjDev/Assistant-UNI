import os
# Ceci importe le module pour pouvoir changer le directory

def file_exists(filename):
    """
    @ pre : `filename` représente le nom d'un fichier.
    @ post : Retourne True si le fichier est présent dans le directory, False sinon.
    
    Cette fonction permet de vérifier si un fichier est présent dans la directory de l'ordinateur.
    """
    try:
        with open(filename, 'r') as file: # Essaye d'ouvrir le fichier donné
            file.close()
            return True
    except:
        raise FileNotFoundError("Error, the file's name is invalid.")

def info_file(filename):
    """
    @ pre : `filename` représente le nom d'un fichier.
    @ post : Retourne le nombre de lignes et de caractères du fichier.
    
    Cette fonction permet de compter le nombre de lignes et de caractères q'un fichier contient.
    """
    count_lines = 0
    count_characters = 0
    
    try:
        with open(filename, 'r') as file:
            characters = file.read()
            count_characters = len(characters) # Stock le compte des caractères
            lines = characters.split('\n') # Split où les lignes se terminent
            count_lines = len(lines)
            
            file.close()
            if count_characters == 0 and count_lines == 0: # Vérifie si le fichier est vide
                return 'Your file is empty, Make sure to add some things to it :)'
            else:
                return 'Your file contains:\n' + str(count_lines) + ' lines\n' + str(count_characters) + ' caracters'
    except:
        raise NameError 
      

def convert_file_to_words(filename):
    """
    @pre : `filename` représente le nom d'un fichier. Ce fichier doit etre une liste de mots.
    @post : Retourne une liste contenant tout les mots présent dans la liste de mots.
            Si le fichier n'est pas une liste de mots, la foncton retourne -1.
    
    Cette fonction permet de décomposer un fichier en une liste de mots. Ce qui permet de chercher plus facilement
    un mot.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split('\n') # Split où la ligne se finit.
            
            for list in words:
                if ' ' in list: # Vérifie si le fichier est une list de mots, si pas, retourne -1
                    return -1
            file.close()
            return words # La liste de mots
    except:
        raise NameError
    
def find_word(list, word):
    """
    @pre : `list` représente une liste de mots.
           `word` représenre le mot que l'ont veut rechercher.
    @post : Retourne True si `word` est présent dans la liste, sinon False.
    
    Cette fonction permet de voir si un mot précis est présent dans une liste de mots précise.
    """
    if ',' in list[0]: # On check si il y'a une virgule et split à cet endroit.
        for lists in list:
            if word == lists.split(',')[0]:
                return True
    else:
        if word in list:
            return True
        
    return False

def word_occurence(list, word):
    """
    @pre : `list` représente une liste de mots.
           `word` représenre le mot que l'ont veut rechercher.
    @post : Retourne le nombre d'occurrence du mots si mis dans le fichier.
    
    Cette fonction permet d'obtenir l'occurrence dun mot.
    """
    if ',' in list[0]: # On check si il y'a une virgule et split à cet endroit.
        for lists in list:
            if word == lists.split(',')[0]:
                if len(lists.split(',')) == 2:
                    return lists.split(',')[1] # Retourne le nombre d'occurence
                else:
                    return 0

def sum(l):
    """
    @ pre : `l` représente une liste non vide composée uniquement de nombres.
    @ post : Retourne la somme de tout ces nombres.
    
    Cette fonction permet d'additionner des nombres présents dans une liste.
    """
    result = 0
    
    for number in l: # Pour chaque nombre dans la liste
        result += number
    
    return result

def avg(l):
    """
    @ pre : `l` représente une liste non vide composée uniquement de nombres.
    @ post : Retourne la moyenne des nombres présents dans la liste.
    
    Cette fonction permet de calculer la moyenne de nombres présents dans une liste.
    """
    result = sum(l) / len(l) # On divise la somme par le nombre de numéros pour obtenir la moyenne
    
    return result

# Début du code concernant le programme.

print( '\n' + 'The current directory used is: ' + os.getcwd() + '\n') # Affiche le directory actif

finished = False
converted_to_words = False

print('Welcome to your personalized tool!')
    
while not finished: # Une boucle qui va continuer a tourner jusqu'a ce que l'utilisateur utilise la méthode exit
    answer = input('> ').lower()
    
    parameters = answer.split() # On split la réponse où on a des espaces
    if len(parameters) == 0: # Pour que le programme ne s'arrète pas si l'utilisateur n'écrit rien
        pass
    else:
        if parameters[0] == 'file':
            try:
                if len(parameters) == 2: # On check si l'utilisateur à écrit 1 nom de fichier et non 2.
                    if file_exists(parameters[1]):
                        filename = parameters[1] # filename devient le nom du fichier
                        print('loaded', filename)
                else:
                    print('Enter a valid file name.')
            except FileNotFoundError as error: # Si les conditions ne sont pas respecter, on affiche un message
                print(error)
                
        elif parameters[0] == 'info':
            try:
                print(info_file(filename)) # Appel de la fonction qui nous donne les infos
            except NameError:
                print('You did not choose a file with the command `file <name>` !')
        
        elif parameters[0] == 'words':
            try:
                words = convert_file_to_words(filename) # On convert le fichier en une liste de mots
                if words == -1:
                    print('Please provide a file that is a valid list of words.') # Affiche le message si ce n'est pas une liste de mots valide
                else:
                    converted_to_words = True # Assure que la convertion a été faite.
                    print('The file has been converted to a list of words.')
            except NameError:
                print('You did not choose a file with the command `file <name>` !')
                
        elif parameters[0] == 'search':
            if not len(parameters) == 1:
                wanted_word = '' # La variable qui représente le mots qui va etre rechercher
                for index in range(1, len(parameters)): # check si le mot est composé de plusieurs mots ou pas
                    if not index == len(parameters) - 1:
                        wanted_word += parameters[index] + ' '
                    else: # Pour ne pas avoir d'espaces en plus à la fin du dernier mot
                        wanted_word += parameters[index]
                try:
                    if converted_to_words:
                        found = find_word(convert_file_to_words(filename), wanted_word) # On stock dans cette variable si il est dans la liste ou pas
                        
                        if found:
                            print(str(wanted_word) + ' is in the list of words.')
                        else:
                            print(str(wanted_word) + ' is not in the list of words.')
                    else:
                        print('Make sure you use the `words` command before using this one.')
                            
                            
                except NameError:
                    print('Make sure you use the `words` command before using this one.')
            else:
                print('Choose a word.')
                
        elif parameters[0] == 'occurence':
            if not len(parameters) == 1:
                wanted_word = '' # La variable qui représente le mots qui va etre rechercher
                for index in range(1, len(parameters)): # check si le mot est composé de plusieurs mots ou pas
                    if not index == len(parameters) - 1:
                        wanted_word += parameters[index] + ' '
                    else: # Pour ne pas avoir d'espaces en plus à la fin du dernier mot
                        wanted_word += parameters[index]
                
                try:
                    if converted_to_words: # Check si l'utilisateur a utilisé la commande words avant
                        if find_word(convert_file_to_words(filename), wanted_word): # Check si le mot est dans le fichier
                            occurrence = word_occurence(convert_file_to_words(filename), wanted_word)
                            print("The number of occurence of the word you chose is: " + str(occurrence))
                        else:
                            print("The word you provided is not in the list.")
                    else:
                        print("Make sure you use the `words` command before using this one.")
                
                except NameError:
                    print('Make sure you use the `words` command before using this one.')
            else:
                print('Choose a word.')
            
        elif parameters[0] == 'sum':
            numbers_list = [] # On crée une liste pour stocker les nombres à l'interieur et appelé une fonction
            
            for index in range(1, len(parameters)):
                    if '.' in parameters[index]: # Pour savoir convertir les chaines en int ou en float si la contient un .
                        numbers_list.append(float(parameters[index]))
                    else:
                        numbers_list.append(int(parameters[index]))       
            
            result = sum(numbers_list) # Appel de la fonction et stock du résultat dans result
            print('The sum of the numbers you provided is: ' + str(result))
        
        elif parameters[0] == 'avg':
            numbers_list = [] 
            
            for index in range(1, len(parameters)):
                    if '.' in parameters[index]:
                        numbers_list.append(float(parameters[index]))
                    else:
                        numbers_list.append(int(parameters[index]))       
            
            result = avg(numbers_list) # Appel de la fonction et stock du résultat dans result
            print('The average of the numbers you provided is: ' + str(result))
            
        elif parameters[0] == 'help':
            print('''
    Welcome to your personalized tool, here you will find all the commands
    available with a small explanation of what's their effect.

    Here is the list of the commands available:

    1 - file <name> : This command specifies the name of a file that the tool should work on
    from the moment you execute it.

    2 - info : This command shows how many lines and caracters your file has.

    3 - words : Converts the file to a list of words.

    4 - search : Lets you search a word in the file you provided.
    Attention, the file must be a list of words.

    5 - sum : This command will add all the numbers you provide.
    The format is with spaces.
    Ex. sum 2 7 10 9 8
        output = 36

    6 - avg : This command will calculate the average of the numbers you provide.
    Same format as sum.
    Ex. avg 5 10 2 4 10
        output = 6.2

    7 - help : This command gives you some info and shows you all the commands available.

    8 - modify <directory> : This command lets you modify the directory.

    9 - directory : This command shows which directory you are in now.

    10 - exit : This command will exit the program.
    ''')
        
        elif parameters[0] == 'modify': # Permet de modifier le directory dans lequel on se trouver
            try:
                new_directory = ''
                for index in range(1, len(parameters)):
                    if not index == len(parameters) - 1: # Pour éviter les espaces en fin de phrases
                        new_directory += parameters[index] + ' '
                    else:
                        new_directory += parameters[index]
                        
                os.chdir(new_directory) # Fonction pour changer le directory
                
                print('The directory has been changed. You are working now in :' + os.getcwd())
            
            except FileNotFoundError:
                print('Please choose a valid directory.')
        
        elif parameters[0] == 'directory': # Permet d'afficher le directory dans lequel on est
            print('You are now in: ' + os.getcwd())
            
        elif parameters[0] == 'exit': # Permet d'arreter le programme
            finished = True
            print('Thank you for using this tool.') # Message de remerciement
        
        else:
            print("I do not recognize this command, please type `help` if you need help finding some commands.")
            # Affiche ce message lorsque l'utilisateur écrit n'importe quoi / une commande non disponible.