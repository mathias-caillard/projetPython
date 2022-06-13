"""


J'ai réalisé ce projet durant l'été 2021 quelques jours après avoir voyagé en avion et joué au célèbre jeu 2048 sur l'ordinateur de bord du siège en face de moi.

comment y jouer :

- exécuter le fichier
- Appeler la fonction partie()
- utiliser le terminal comme interface
- suivre les instructions
- have fun !
"""

import random as rd
import copy
import numpy as np

def grilleSetup(n) :
    Grille = np.zeros((n,n))

    for p in range(0,2) :
        i = rd.randint(0,n-1)
        j = rd.randint(0,n-1)
        k = rd.randint(0,1)
        if k == 0 :
            variable = 2
        else :
            variable = 4
        Grille[i][j] = variable
    return(Grille)

def coupSuivant(Grille,n) :
    x = input()
    if x == "e" :
        print("Fin de la partie.")
        return np.full(n,None)
    if x == "z" :
        Grille = Haut(Grille)
    elif x == "s" :
        Grille = Bas(Grille)
    elif x == "d" :
        Grille = Droite(Grille)
    elif x == "q":
        Grille = Gauche(Grille)
    return(Grille)


def valide(i,j,n) :
    return not(i >= n or j >= n or i < 0 or j < 0)

def Haut(G) :
    Grille = copy.deepcopy(G)
    n = len(G)
    Fusion = np.full((n,n),False)

    compteur = -1
    while compteur != 0 :
        compteur = 0
        for i in range(n) :
            for j in range(n) :
                case = Grille[i][j]
                if case != 0 and valide(i-1,j,n) and Grille[i-1][j] == 0 :
                    Grille[i-1][j] = case
                    Grille[i][j] = 0
                    compteur += 1

                elif case != 0 and valide(i-1,j,n) and Grille[i-1][j] == case and Fusion[i-1][j] == False and Fusion[i][j] == False :
                    Grille[i-1][j] = 2*case
                    Fusion[i-1][j] = True
                    Grille[i][j] = 0
                    compteur += 1

    return(Grille)

def Bas(G) :
    Grille = copy.deepcopy(G)
    n = len(G)
    Fusion = np.full((n,n),False)

    compteur = -1
    while compteur != 0 :
        compteur = 0
        for i in range(n) :
            for j in range(n) :
                case = Grille[n-1-i][j]
                if case != 0 and valide(n-i,j,n) and Grille[n-i][j] == 0 :
                    Grille[n-i][j] = case
                    Grille[n-i-1][j] = 0
                    compteur += 1

                elif case != 0 and valide(n-i,j,n) and Grille[n-i][j] == case and Fusion[n-i][j] == False and Fusion[n-i-1][j] == False :
                    Grille[n-i][j] = 2*case
                    Fusion[n-i][j] = True
                    Grille[n-i-1][j] = 0
                    compteur += 1

    return(Grille)

def Gauche(G) :
    Grille = copy.deepcopy(G)
    n = len(G)
    Fusion = np.full((n,n),False)

    compteur = -1
    while compteur != 0 :
        compteur = 0
        for j in range(n) :
            for i in range(n) :
                case = Grille[i][j]
                if case != 0 and valide(i,j-1,n) and Grille[i][j-1] == 0 :
                    Grille[i][j-1] = case
                    Grille[i][j] = 0
                    compteur += 1

                elif case != 0 and valide(i,j-1,n) and Grille[i][j-1] == case and Fusion[i][j-1] == False and Fusion[i][j] == False :
                    Grille[i][j-1] = 2*case
                    Fusion[i][j-1] = True
                    Grille[i][j] = 0
                    compteur += 1
    return(Grille)

def Droite(G) :
    Grille = copy.deepcopy(G)
    n = len(Grille)
    Fusion = np.full((n,n),False)

    compteur = -1
    while compteur != 0 :
        compteur = 0
        for j in range(n) :
            for i in range(n) :
                case = Grille[i][n-j-1]
                if case != 0 and valide(i,n-j,n) and Grille[i][n-j] == 0 :
                    Grille[i][n-j] = case
                    Grille[i][n-j-1] = 0
                    compteur += 1

                elif case != 0 and valide(i,n-j,n) and Grille[i][n-j] == case and Fusion[i][n-j] == False and Fusion[i][n-j-1] == False :
                    Grille[i][n-j] = 2*case
                    Fusion[i][n-j] = True
                    Grille[i][n-j-1] = 0
                    compteur += 1
    return(Grille)


def transpose(Grille) :
    G = copy.deepcopy(Grille)
    n = len(G)
    for i in range(n) :
        for j in range(n) :
            if i < j :
                G[j][i],G[i][j] = G[i][j], G[j][i]
    return(G)

def coup_possible(Grille) :
    n = len(Grille)
    drapeau = False
    for i in range(n) :
        for j in range(n) :
            case = Grille[i][j]
            if (valide(i-1,j,n) and case == Grille[i-1][j]) or (valide(i+1,j,n) and case == Grille[i+1][j]) or (valide(i,j+1,n) and case == Grille[i][j+1]) or (valide(i-1,j-1,n) and case == Grille[i][j-1]):
                drapeau = True
    return(drapeau)

def existence_zero(Grille) :
    n = len(Grille)
    drapeau = False
    for i in range(n) :
        for j in range(n) :
            if Grille[i][j] == 0 :
                drapeau = True
    return(drapeau)

def grille_gagnante(Grille) :
    n = len(Grille)
    drapeau = False
    for i in range(n) :
        for j in range(n) :
            if Grille[i][j] == 2048 :
                drapeau = True
    return(drapeau)

def partie_termine(Grille) :
    return(not coup_possible(Grille) and not existence_zero(Grille))

def ajout_case(Grille) :
    G = copy.deepcopy(Grille)
    n = len(G)
    liste_zero = []
    for i in range(n) :
        for j in range(n) :
            if G[i][j] == 0 :
                liste_zero.append([i,j])
    p = len(liste_zero)
    k = rd.randint(0,p-1)
    [i,j] = liste_zero[k]
    a = rd.randint(0,1)
    if a == 0 :
        G[i][j] = 2
    else :
        G[i][j] = 4
    return(G)

def partie() :
    print("Selectionner la taille de la grille (taille 4 recommandée).")
    n = int(input())
    G = grilleSetup(n)
    print(G)
    print("Sélectionner une direction (z --> haut ; s --> bas ; d --> droite ; q --> gauche). Entrer e pour quitter.")
    while not partie_termine(G) :
        if grille_gagnante(G) :
            return("Gagné !")
        G_suivant = coupSuivant(G,n)
        if (G_suivant == None).all() :
            return None
        if not (G_suivant==G).all() :
            G_suivant = ajout_case(G_suivant)
        print(G_suivant)
        G = G_suivant
    print("Perdu ...")
    print("Recommencer ? (o/n)")
    c = input()
    while c != "o" and c != "n" :
        print("Recommencer ? (o/n)")
        c = input()

    if c == "n" :
        print("Fin de la partie.")
    elif c == "o" :
        partie()

