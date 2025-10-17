# Jeux de Nim et Marienbad

Un programme Python implémentant deux variantes classiques du jeu de Nim : le Nim classique et le Marienbad.

## 1- Description
Ce projet propose deux jeux stratégiques où les joueurs retirent des allumettes suivant des règles spécifiques. Le perdant est celui qui prend la dernière allumette.

### Jeu du Nim Classique
- 21 allumettes dans une seule pile
- Chaque joueur retire 1 à 4 allumettes par tour
- Celui qui prend la dernière allumette perd
### Jeu de Marienbad
- 4 tas avec respectivement 1, 3, 5 et 7 allumettes
- Chaque joueur retire autant d'allumettes qu'il veut d'un SEUL tas par tour
- Celui qui prend la dernière allumette perd
## 2- Fonctionnalités
- Deux modes de jeu :
  - Joueur contre Joueur
  - Joueur contre Ordinateur
- IA avec stratégie pour les deux jeux
- Système de rejouabilité sans redémarrer le programme
- Gestion des noms des joueurs
- Validation robuste des entrées utilisateur
## 3- Installation et Exécution
### Prérequis
- Python 3.6 ou supérieur
### Lancement
python nim_games.py
## 4- Comment jouer
### Démarrage
- Lancez le programme

- Choisissez entre :

1 : Jeu du Nim classique

2 : Jeu de Marienbad

3 : Quitter

### Configuration de la partie
- Sélection du mode (Joueur vs Joueur ou Joueur vs Ordinateur)

- Saisie des noms des joueurs

- Choix du premier joueur

### Pendant la partie
- Suivez les instructions à l'écran

- Entrez le nombre d'allumettes à retirer

- Respectez les limites imposées par le jeu

## 5- Stratégies de l'IA
### Nim Classique
- L'ordinateur utilise une stratégie gagnante basée sur :

- Calcul du coup optimal pour forcer l'adversaire à prendre la dernière allumette

- Adaptation selon qu'il commence ou joue en second

### Marienbad
- L'IA utilise une approche simple mais efficace :

- Prise d'allumettes d'un tas contenant une seule allumette

- Retrait aléatoire d'entre 1 et la moitié des allumettes d'un tas

## 6- Structure du Code
### Les principales fonctions
|--- main()--------------------------------------------# Point d'entrée principal

├── nim_game()----------------------------------# Jeu du Nim classique

├── marienbad_game()-------------------------# Jeu de Marienbad

└── computer_strategy_marienbad(piles)--------# Stratégie IA Marienbad

## 7- Règles Détaillées
### Nim Classique
- 21 allumettes au départ

- Retrait de 1 à 4 allumettes par tour

- Impossible de passer son tour

- La partie se termine quand un joueur prend la dernière allumette

### Marienbad
- Configuration initiale : tas de 1, 3, 5 et 7 allumettes

- Un seul tas modifié par tour

- Nombre d'allumettes retirées libre (1 à taille du tas)

- Victoire en forçant l'adversaire à prendre la dernière allumette


