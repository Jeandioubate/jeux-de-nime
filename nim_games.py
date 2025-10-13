#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeux  de Nim (variante simple et de Marienbad)
"""

def nim_game(): # C'est la fonction principale qui contient tout le jeu.

    # Jeu des allumettes

    print("Bienvenue au jeu du Nim !")
    print("Il y a 21 allumettes. Chaque joueur peut retirer entre 1 et 4 allumettes par tour.")
    print("Celui qui prend la dernière allumette perd !\n")

    pile_of_matches = 21  # Nombre initial d'allumettes

    # Demander le nom de chaque joueur
    player_01 = input("Veuillez saisir votre nom: ") # Ces variables demandent et stockent les noms des joueurs.
    player_02 = input("Veuillez saisir votre nom: ")

    # Choix du joueur qui commence
    first = input(f"Qui commence ({player_01} ou {player_02}) ?").strip() # j'enlève les espaces superflus.
    if first.lower() == player_01.lower():
        current_player = player_01
        other_player = player_02
    else:
        current_player = player_02
        other_player = player_01
    # Déroulement du jeu
    while pile_of_matches > 0: # La boucle continue tant qu'il reste des allumettes.
        print(f"\nIl reste {pile_of_matches} allumettes.") # J'affiche le nombre d'allumettes restantes.
        print(f"C'est à {current_player} de jouer") # J'affiche le joueur dont c'est le tour.

    # Saisie et validation du choix du joueur
        """ Le programme demande au joueur le nombre d'allumettes à retirer, la boucle valide l'entrée:
    . doit être entre 1 et 4
    . ne peut pas dépasser le nombre d'allumettes restantes
    . si saisie invalide, redemander jusqu'à obtenir une valeur correcte"""

        remove = int(input(f"{current_player}, combien d'allumettes voulez-vous retirer (1-4) ? "))
        while remove < 1 or remove > 4 or remove > pile_of_matches:
            print("Choix invalide. Vous devez retirer entre 1 et 4 allumettes, sans dépasser le nombre restant.")
            remove = int(input(f"{current_player}, combien d'allumettes voulez-vous retirer (1-4) ? "))
    # Mise à jour de la pile
        pile_of_matches -= remove # Je soustrais le nombre d'allumettes retirées du total.

    # Je vérifie si la partie est terminée
        if pile_of_matches == 0: # Si la pile est vide.
            print(f"\n{current_player} a pris la dernière allumette") # J'affiche le joueur qui a pris la dernière
            print(f"{other_player} a gagné") # J'affiche le joueur gagnant
            break # Je sors de la boucle.

    # Je procède au changement de joueur
        current_player, other_player = other_player, current_player

# Je lance la partie

if __name__ == "__main__":
    nim_game()

