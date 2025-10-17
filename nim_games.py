#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeux  de Nim (variante simple et de Marienbad)
"""
import random


def nim_game(): # C'est la fonction principale qui contient tout le jeu.

    # Jeu des allumettes

    print("Bienvenue au jeu du Nim !")
    print("Il y a 21 allumettes. Chaque joueur peut retirer entre 1 et 4 allumettes par tour.")
    print("Celui qui prend la dernière allumette perd !\n")

    pile_of_matches = 21  # Nombre initial d'allumettes

    # Choix du mode de jeu
    print("Choisissez le mode de jeu :")
    print("1. Joueur contre Joueur")
    print("2. Joueur contre Ordinateur")
    mode = input("Votre choix (1 ou 2) : ").strip()

    # Déclaration de la variable nombre d'allumettes que le joueur vient de retirer
    last_player_move = 0 # Initialisation

    if mode == "1":
        # Mode Joueur contre Joueur
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

    else:
        # Mode Joueur contre Ordinateur
        player_01 = input("Veuillez saisir votre nom : ")
        player_02 = "Ordinateur"

        # Choix du joueur qui commence
        print("Qui commence ?")
        print(f"1. {player_01}")
        print("2. Ordinateur")
        first_choice = input("Votre choix (1 ou 2) : ").strip()

        if first_choice == "1":
            current_player = player_01
            other_player = player_02
            print(f"{player_01} commence la partie !")
        else:
            current_player = player_02
            other_player = player_01
            print("L'ordinateur commence la partie !")

    # Déroulement du jeu
    while pile_of_matches > 0: # La boucle continue tant qu'il reste des allumettes.
        print(f"\nIl reste {pile_of_matches} allumettes.") # J'affiche le nombre d'allumettes restantes.
        print(f"C'est à {current_player} de jouer") # J'affiche le joueur dont c'est le tour.

        if current_player == "Ordinateur":
            # Tour de l'ordinateur
            if other_player == player_01:  # Cas 1 : L'ordinateur joue en second
                # L'ordinateur applique la stratégie : retire 5 - k
                # Pour forcer le joueur à prendre la dernière allumette
                remove = 5 - last_player_move
                # Vérification que le coup est valide
                if remove < 1:
                    remove = 1
                elif remove > 4:
                    remove = 4
                if remove > pile_of_matches:
                    remove = pile_of_matches

                print(f"L'ordinateur retire {remove} allumettes.")

            else:  # Cas 2 : L'ordinateur commence
                # Stratégie : se ramener au cas précédent dès que possible
                # L'objectif est de laisser un multiple de 5 + 1 allumettes
                target_position = (pile_of_matches - 1) % 5
                if target_position == 0:
                    # Position gagnante, on peut appliquer la stratégie normale
                    remove = 1  # On commence par un coup sûr
                else:
                    # On essaie d'atteindre une position gagnante
                    remove = target_position
                    if remove == 0:
                        remove = 1

                # Vérification que le coup est valide
                if remove > pile_of_matches:
                    remove = pile_of_matches

                print(f"L'ordinateur retire {remove} allumettes.")
        else:
            # Saisie et validation du choix du joueur
            remove = int(input(f"{current_player}, combien d'allumettes voulez-vous retirer (1-4) ? "))
            while remove < 1 or remove > 4 or remove > pile_of_matches:
                print("Choix invalide. Vous devez retirer entre 1 et 4 allumettes, sans dépasser le nombre restant.")
                remove = int(input(f"{current_player}, combien d'allumettes voulez-vous retirer (1-4) ? "))

                # Sauvegarde du coup du joueur pour la stratégie de l'ordinateur
            if mode == "2" and current_player != "Ordinateur":
                last_player_move = remove

        """ Le programme demande au joueur le nombre d'allumettes à retirer, la boucle valide l'entrée:
    . doit être entre 1 et 4
    . ne peut pas dépasser le nombre d'allumettes restantes
    . si saisie invalide, redemander jusqu'à obtenir une valeur correcte    """

    # Mise à jour de la pile
        pile_of_matches -= remove # Je soustrais le nombre d'allumettes retirées du total.

    # Je vérifie si la partie est terminée
        if pile_of_matches == 0: # Si la pile est vide.
            print(f"\n{current_player} a pris la dernière allumette") # J'affiche le joueur qui a pris la dernière
            print(f"{other_player} a gagné") # J'affiche le joueur gagnant
            break # Je sors de la boucle.

    # Je procède au changement de joueur
        current_player, other_player = other_player, current_player


def marienbad_game():
    """Jeu de Marienbad - Variante avec 4 tas"""
    # Cette fonction implémente la variante Marienbad du jeu de Nim
    # Le jeu se joue avec 4 tas de tailles différentes : 1, 3, 5 et 7 allumettes
    # Les règles sont similaires, mais avec plusieurs tas au lieu d'un seul.

    print("Bienvenue au jeu de Marienbad !")
    print("Il y a 4 tas avec respectivement 1, 3, 5 et 7 allumettes.")
    print("À chaque tour, vous pouvez prendre autant d'allumettes que vous voulez d'un SEUL tas.")
    print("Celui qui prend la dernière allumette perd !\n")

    # Initialisation des tas — configuration classique du jeu de Marienbad
    piles = [1, 3, 5, 7]

    # Choix du mode de jeu
    print("Choisissez le mode de jeu :")
    print("1. Joueur contre Joueur")
    print("2. Joueur contre Ordinateur")
    mode = input("Votre choix (1 ou 2) : ").strip()

    if mode == "1":
        # Mode Joueur contre Joueur
        player_01 = input("Veuillez saisir le nom du premier joueur : ")
        player_02 = input("Veuillez saisir le nom du deuxième joueur : ")

        first = input(f"Qui commence ({player_01} ou {player_02}) ? ").strip()
        if first.lower() == player_01.lower():
            current_player = player_01
            other_player = player_02
        else:
            current_player = player_02
            other_player = player_01
    else:
        # Mode Joueur contre Ordinateur
        player_01 = input("Veuillez saisir votre nom : ")
        player_02 = "Ordinateur"

        print("Qui commence ?")
        print(f"1. {player_01}")
        print("2. Ordinateur")
        first_choice = input("Votre choix (1 ou 2) : ").strip()

        if first_choice == "1":
            current_player = player_01
            other_player = player_02
            print(f"{player_01} commence la partie !")
        else:
            current_player = player_02
            other_player = player_01
            print("L'ordinateur commence la partie !")

    # Déroulement du jeu — la boucle continue tant qu'il reste des allumettes dans au moins un tas
    while sum(piles) > 0:
        print(f"\nÉtat des tas :")
        for i, pile in enumerate(piles, 1):
            print(f"Tas {i}: {pile} allumette{'s' if pile > 1 else ''}")

        print(f"\nC'est à {current_player} de jouer")

        if current_player == "Ordinateur":
            # Tour de l'ordinateur : utilisation de la stratégie définie séparément
            remove, pile_index = computer_strategy_marienbad(piles)
            piles[pile_index] -= remove
            print(f"L'ordinateur retire {remove} allumette{'s' if remove > 1 else ''} du tas {pile_index + 1}")

        else:
            # Tour du joueur humain
            print("Choisissez un tas et le nombre d'allumettes à retirer.")
            pile_index = int(input("Numéro du tas (1-4) : ")) - 1

            # Validation du tas choisi : doit être entre 1 et 4 et contenir des allumettes
            while pile_index < 0 or pile_index > 3 or piles[pile_index] == 0:
                print("Tas invalide. Choisissez un tas entre 1 et 4 qui contient des allumettes.")
                pile_index = int(input("Numéro du tas (1-4) : ")) - 1

            max_take = piles[pile_index]
            remove = int(input(f"Nombre d'allumettes à retirer (1-{max_take}) : "))

            # Validation du nombre d'allumettes à retirer
            while remove < 1 or remove > max_take:
                print(f"Nombre invalide. Vous devez retirer entre 1 et {max_take} allumettes.")
                remove = int(input(f"Nombre d'allumettes à retirer (1-{max_take}) : "))

            # Mise à jour du tas après retrait des allumettes
            piles[pile_index] -= remove

        # Vérification si la partie est terminée (plus d'allumettes dans aucun tas)
        if sum(piles) == 0:
            print(f"\n{current_player} a pris la dernière allumette !")
            print(f"{other_player} a gagné !")
            break

        # Changement de joueur pour le tour suivant
        current_player, other_player = other_player, current_player


def computer_strategy_marienbad(piles):
    """Stratégie simple pour l'ordinateur au jeu de Marienbad"""
    # Cette fonction détermine le coup de l'ordinateur.
    # Elle utilise une stratégie basique.

    # Stratégie 1 : Prendre toutes les allumettes d'un tas s'il n'en reste qu'un
    for i, pile in enumerate(piles):
        if pile == 1:
            return 1, i

    # Stratégie 2 : Prendre aléatoirement d'un tas non vide
    non_empty_piles = [i for i, pile in enumerate(piles) if pile > 0]
    pile_index = random.choice(non_empty_piles)

    # Prendre entre 1 et la moitié des allumettes du tas (ou 1 si le tas est petit)
    max_take = piles[pile_index]
    if max_take == 1:
        remove = 1
    else:
        remove = random.randint(1, max(1, max_take // 2))

    return remove, pile_index


def main():
    """Fonction principale pour choisir le jeu et gérer les multiples parties"""
    # Cette fonction orchestre le déroulement global du programme
    # Elle permet de choisir le jeu et de rejouer sans relancer le programme

    while True:  # Boucle principale pour permettre de jouer plusieurs parties
        print("\n" + "="*50)
        print("         MENU PRINCIPAL DES JEUX")
        print("="*50)
        print("Choisissez le jeu :")
        print("1. Jeu du Nim classique (21 allumettes)")
        print("2. Jeu de Marienbad (4 tas)")
        print("3. Quitter")

        choice = input("Votre choix (1, 2 ou 3) : ").strip()

        if choice == "1":
            nim_game()
        elif choice == "2":
            marienbad_game()
        elif choice == "3":
            print("Merci d'avoir joué ! À bientôt !")
            break  # Sort de la boucle while pour terminer le programme
        else:
            print("Choix invalide. Veuillez choisir 1, 2 ou 3.")

        # Après chaque partie, proposer de rejouer ou de changer de jeu
        if choice in ["1", "2"]:
            replay = input("\nVoulez-vous jouer une autre partie ? (o/n) : ").strip().lower()
            if replay != 'o' and replay != 'oui':
                print("Merci d'avoir joué ! À bientôt !")
                break


# Point d'entrée du programme
if __name__ == "__main__":
    main()
