#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeux  de Nim (variante simple et de Marienbad)
"""
import random

import random


def nim_game():
    # Jeu des allumettes

    print("Bienvenue au jeu du Nim !")
    print("Il y a 21 allumettes. Chaque joueur peut retirer entre 1 et 4 allumettes par tour.")
    print("Celui qui prend la dernière allumette perd !\n")

    pile_of_matches = 21  # Nombre initial d'allumettes

    # Demander le nom de chaque joueur
    player_01 = input("Veuillez saisir votre nom: ")
    player_02 = input("Veuillez saisir votre nom: ")

    # Choix du joueur qui commence
    first = input(f"Qui commence ({player_01} ou {player_02}) ?").strip()
    if first.lower() == player_01.lower():
        current_player = player_01
        other_player = player_02
    else:
        current_player = player_02
        other_player = player_01
    # Déroulement du jeu
    while pile_of_matches > 0:
        print(f"\nIl reste {pile_of_matches} allumettes.")
        print(f"C'est à {current_player} de jouer")
        remove = int(input(f"{current_player}, combien d'allumettes voulez-vous retirer (1-4) ? "))
        while remove < 1 or remove > 4 or remove > pile_of_matches:
            print("Choix invalide. Vous devez retirer entre 1 et 4 allumettes, sans dépasser le nombre restant.")
            remove = int(input(f"{current_player}, combien d'allumettes voulez-vous retirer (1-4) ? "))
    # Je retire des allumettes après chaque tour
        pile_of_matches -= remove

    # Je vérifie si la partie est terminée
        if pile_of_matches == 0:
            print(f"\n{current_player} a pris la dernière allumette")
            print(f"{other_player} a gagné")
            break

    # Je procède au changement de joueur
        current_player, other_player = other_player, current_player

# Je lance la partie

if __name__ == "__main__":
    nim_game()

