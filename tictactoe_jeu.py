"""
Projet Tic-Tac-Toe réalisé durant l'été 2021.

Il y a deux niveaux de difficultés.

- Niveau 1 : l'adversaire joue aléatoirement : vous jouez contre un singe.

- Niveau 2 : Dès que l'adversaire peut jouer un coup gagnant à son prochain tour, il le fait (profondeur d'un coup). Dès que vous pourrez jouer un coup gagnant à votre prochain tour, l'adversaire va vous bloquer (profondeur de deux coups). Dans les autres cas, l'adversaire joue aléatoirement. Lorsque vous jouez un coup qui vous donne l'opportunité de jouer deux coups gagnants à votre prochain coups, l'adversaire vous fait un gentil commentaire...

Comment jouer ?
- exécuter le fichier.
- appeller la fonction partie()
- utiliser le terminal comme interface graphique
- suivre les instructions
- enjoy !



Certaines fonctions sont redondantes et j'aurai pu factoriser du code, ou encore compacter les enchainements de "elif" par des 'switch case', mais mon objectif était de produire ma propre version du jeu Tic-Tac-Toe fonctionnel sans pour autant obtenir une solution optimale et compacte.
"""

import random as rd
import numpy as np

def estDans(x,L) :
    for k in L :
        if k == x :
            return True
    return False

def caseVide(G,i,j) :
    return(G[i][j] == "_")

def coupAdversaire_1(G,joueur1) :
    emplacement_vide = []
    if joueur1 == "X" :
        joueur2 = "O"
    else :
        joueur2 = "X"

    for i in range(3) :
        for j in range(3) :
            if G[i][j] == "_" :
                emplacement_vide.append([i,j])

    p = len(emplacement_vide)
    k = rd.randint(0,p-1)
    [i,j] = emplacement_vide[k]
    G[i][j] = joueur2
    return G

def coupAdversaire_2(G,joueur1) :
    emplacement_vide = []
    if joueur1 == "X" :
        joueur2 = "O"
    else :
        joueur2 = "X"

    for i in range(3) :
        for j in range(3) :
            if G[i][j] == "_" :
                emplacement_vide.append([i,j])

    coup_gagnant_pour_j1 = []
    coup_gagnant_pour_j2 = []

    for couple in emplacement_vide :
        [i,j] = couple

        G[i][j] = joueur1
        if partie_gagnante(G,joueur1) :
            coup_gagnant_pour_j1.append([i,j])

        G[i][j] = joueur2
        if partie_gagnante(G,joueur2) :
            coup_gagnant_pour_j2.append([i,j])

        G[i][j] = "_"

    print(coup_gagnant_pour_j1)
    print(coup_gagnant_pour_j2)
    if len(coup_gagnant_pour_j1) > 1 and coup_gagnant_pour_j2 == [] :
        print("Gros malin !")

    if coup_gagnant_pour_j2 != [] :
        p = len(coup_gagnant_pour_j2)
        k = rd.randint(0,p-1)
        [i,j] = coup_gagnant_pour_j2[k]
        G[i][j] = joueur2
        return(G)

    elif coup_gagnant_pour_j1 != [] :

        p = len(coup_gagnant_pour_j1)
        k = rd.randint(0,p-1)
        [i,j] = coup_gagnant_pour_j1[k]
        G[i][j] = joueur2
        return(G)

    return coupAdversaire_1(G,joueur1)

def partie_gagnante(G,joueur1) :
    x = joueur1
    return((G[0][0] == G[0][1] == G[0][2] and G[0][0] == x) or
    (G[1][0] == G[1][1] == G[1][2] and G[1][0] == x) or
    (G[2][0] == G[2][1] == G[2][2] and G[2][0] == x) or
    (G[0][0] == G[1][0] == G[2][0] and G[0][0] == x) or
    (G[0][1] == G[1][1] == G[2][1] and G[0][1] == x) or
    (G[0][2] == G[1][2] == G[2][2] and G[0][2] == x) or
    (G[0][0] == G[1][1] == G[2][2] and G[0][0] == x) or
    (G[2][0] == G[1][1] == G[0][2] and G[2][0] == x))

def partie_perdante(G,joueur1) :
    x = joueur1
    if x == "X" :
        y = "O"
    else :
        y = "X"
    return(partie_gagnante(G,y))

def grille_remplie(G) :
    drapeau = True
    for i in range(3) :
        for j in range(3) :
            if G[i][j] == "_" :
                drapeau = False
    return(drapeau)

def partie_nulle(G,x) :
    return (grille_remplie(G) and not partie_gagnante(G,x) and not partie_perdante(G,x))

def partie_terminer(G,x) :
    return(partie_nulle(G,x) or partie_gagnante(G,x) or partie_perdante(G,x))


def partie() :
    chiffres = ["1","2","3","4","5","6","7","8","9"]
    print("Jouer avec quel symbole ? (X/O)")
    joueur1 = input()

    while joueur1 != "X" and joueur1 != "O" :
        print("Symbole invalide. Entrer X ou O.")
        joueur1 = input()

    if joueur1 == "X" :
        joueur2 = "O"

    else :
        joueur2 = "X"

    print("Sélectionner un niveau de difficulté. (1/2)")
    d = input()
    while d != "1" and d != "2" :
        d = input()
    if d == "1" :
        coupAdversaire = coupAdversaire_1
    else :
        coupAdversaire = coupAdversaire_2

    print("La partie va commencer. Entrer des chiffres de 1 à 9 puis valider avec entrée pour placer un symbole, en s'aidant de l'ordre des cases prédéfini :")

    print(np.full((3,3),[[1,2,3],[4,5,6],[7,8,9]]))
    G = np.full((3,3),"_")
    print(G)

    drapeau = False

    while not partie_terminer(G,joueur1) :
        c = input()
        while not estDans(c,chiffres) :
            print("Entrer un chiffre entre 1 et 9.")
            c = input()

        if c == "1" :
            [i,j] = [0,0]
        elif c == "2" :
            [i,j] = [0,1]
        elif c == "3" :
            [i,j] = [0,2]
        elif c == "4" :
            [i,j] = [1,0]
        elif c == "5" :
            [i,j] = [1,1]
        elif c == "6" :
            [i,j] = [1,2]
        elif c == "7" :
            [i,j] = [2,0]
        elif c == "8" :
            [i,j] = [2,1]
        elif c == "9" :
            [i,j] = [2,2]

        if caseVide(G,i,j) :
            G[i][j] = joueur1
            if not grille_remplie(G) :
                G = coupAdversaire(G,joueur1)
        print(G)

    if partie_nulle(G,joueur1) :
        print("Partie nulle.")
    elif partie_gagnante(G,joueur1) :
        print("Tu as gagné!")
    else :
        print("Tu as perdu...")
    print("Réessayer ? (o/n)")
    r = input()
    while r != "o" and r != "n" :
        r = input()
    if r == "o" :
        partie()
    else :
        print("Fin.")