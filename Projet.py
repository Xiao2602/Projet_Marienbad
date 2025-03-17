allumettes = [1,2,3,4,5,6] #Tas et allumettes du jeu

#Message de bienvenue au jeu
print("========================================================================")
print("Bienvenue dans le jeu Marienbad.")
print("Le but est de prendre un certain nombre d'allumettes d'un tas.")
print("Cependant, si vous voulez prendre un nombre < que ce qui est disponible dans le tas, cela vous fera rejouer pour donner une valeur valide.")
print("========================================================================\n")

#Insertion du nom des joueurs
nom1 = input("Entrez le nom du joueur 1 : ")
nom2 = input("Entrez le nom du joueur 2 : ")

print("\nJoueurs enregistrés :", nom1, "et", nom2,"\n")

joueurs = [nom1,nom2] #Liste des noms de joueurs
tour = 0 #Echange entre les deux joueurs pour faire le tour de role, initialisé à 0

#Déroulement de la partie
while sum(allumettes) >0: #calcule la somme des éléments de la liste des allumettes (remplace la boucle pour créer la liste)
    print(allumettes,"\n")
    print("Joueur", joueurs[tour], "joue.\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    joueur_tas = int(input("Nombre du tas choisi (de 1 à 6): "))-1 #-1 car nous utilisons cette variable en tant qu'indice: le premier élément d'une liste est 0, pas 1
    allumette_tas = int(input("Nombre d'allumette(s) à retirer dans le tas: "))
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if 0 <= joueur_tas < len(allumettes) and 0 < allumette_tas <= allumettes[joueur_tas]: #Si le nombre du tas est => 0 (indice) et allumettes_tas[joueurs_tas] > 0
        allumettes[joueur_tas] -= allumette_tas
        tour =1-tour #Tour prend en compte l'indice de la liste de joueurs (joueur 1 = 0 et joueur 2 = 1)
    else:
        print("Le tas et les allumettes choisi ne sont pas disponibles, veuillez réessayer.")

if sum(allumettes) == 0:
    print(allumettes) #pour afficher tous les 0 de la liste des allumettes une fois vidée
    print("Le joueur", joueurs[tour],"a gagné vu que le joueur", joueurs[1-tour], "a retiré la dernière allumette.")