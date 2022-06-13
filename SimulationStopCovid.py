"""
Le programme suivant est un modèle Python réalisé durant un confinement due à la pandémie de COVID-19.

L'objectif est double :

- Être capable de générer des simulations de cas-contacts au sein d'une population et d'observer l'évolution de la propagation du virus;

- quantifier l'efficacité de l'application StopCovid (qui s'appelle désormais TousAntiCovid) qui permettait de se déclarer malade sur l'application dans le but de casser les chaînes de transmission ud virus. (Avec l'aide d'un modèle simplificateur).


Principe du protocole :

Chaque individu entre en contact avec un certain nombre de personnes. Parmi ces personnes, il y a des individus sains, et d'autres malades.

Lors d'un contact, des messages sous forme d'identifiant générés pseudo-aléatoirement (appelés des ephIDs) sont échangés entre les individus entrés en contact, à l'image de ce qui s'échange réellement lorsque l'on utilise l'application StopCovid sur nos téléphones. Chacun stocke à la fois les ephIDs qu'il a lui-même envoyés et également les ephIDs qu'il a reçu. l'ensemble des ephIDs reçu par un individu "n" est appelé le 'répertoire de n'. Les individus qui s'autodiagnostiquent malade ou se jugent malade le signalent à l'application gérant le protocole. Tous les ephIDs qu'ils ont envoyés sont envoyés et mutualisés dans une base de données appelée 'hospital', sans que l'hospital connaisse l'identité de l'envoyeur.

Un individu n est notifié à risque par le protocole dès que n a reçu plus d'un certain nombre d'ephIDs provenant d'individus notifiés malades. Ce certain nombre, je l'appelle le seuil. En d'autres termes, un individu est notifié à risque par le protocole dès que le cardinal de l'intersection du répertoire de n avec l'hosptial contient au moins (seuil) élément(s). J'ai estimé que seuil = 3 ou est raisonnable.

Ainsi, un individu peut être notifié à risque sans même savoir l'identité des individus avec qui il est entré en contact.

Je suppose qu'un individu est réellement à risque s'il a été en contact avec au moins 2 malades. Ainsi, la comparaison du nombre d'individus notifiés cas contact par le protocole avec celui du nombre d'individus réellement à risque permet de conclure quant à la pertinence et à l'efficacité du protocole :  Plus le rapport entre ces deux nombres est proche de 1, plus le protocole est proche de la 'réalité' et donc pertient.


Dans toute la suite :

- Je note N le nombre total d'individus considérés.

- Les individus sont représentés par des entiers compris entre 0 et N-1.

- 'EphID' signifie 'identifiant éphémère', une chaîne de caractère générée pseudo aléatoirement.

- Une personne est dite à risque si elle est cas contact.

paramètres raisonnables :
N = 100
m = 0.10
d = 0.10
p = 6
taille_id = 7
seuil = 3
s = 20 (nombre de simulation)

Pour obtenir la liste des individus qui doivent s'isoler car ils ont été jugés cas-contacts par le protocole StopCovid, appeler la fonction simulation.

Pour obtenir des graphes quantifiant l'efficacité de l'application StopCovid à l'aide d'un modèle simplifié, appeler les fonctions graphe1 ou graphe2.

"""

## Initialisation
import random as rd
import math
from matplotlib import pyplot as plt

alphabetMin = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","k","r","s","t","u","v","w","x","y","z"]

alphabetMaj = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","K","R","S","T","U","V","W","X","Y","Z"]

nombres = ["0","1","2","3","4","5","6","7","8","9"]

caractere = [alphabetMin, alphabetMaj, nombres]

envois = []
""" envois[n] : liste des ephIDs envoyés par n"""

repertoire = []
""" repertoire[n] :  liste des ephIDs reçus par n"""

malade = []
""" liste des malades"""

hospital = []
""" hospital : liste des ephIDs envoyés par les malades"""

contact = []
""" contact[n] : liste des individus ayant été en contact avec n"""

resultat = []
""" resultat[k] :  k doit s'autoconfiner, d'après le protocole"""

## Fonctions auxiliaires
def estDans(x,L) :
    """
    L (liste)

    Indique si x est dans L.
    """
    for k in L :
        if x == k :
            return True
    return False


def moyenne(L) :
    """
    L (liste d'entiers)

    Renvoie la moyenne arithmétique des valeurs des éléments de L.
    """
    S = 0
    n = len(L)
    for k in L :
        S = S + k
    return(S/n)


def p_parmi_elts_de_L(L) :
    """
    L (liste)

    Sélectionne aléatoirement k éléments dans L avec k entre 0 et len(L).
    """
    n = len(L)
    k = rd.randint(0,n)
    Res = []

    for i in range(k) : # Pour chaque élément à sélectionner,
        j = rd.randint(0,n-1) # on prend un élément L[j] dans L.
        while estDans(L[j],Res) : # Tant que cet élément est déjà pris,
            j = rd.randint(0,n-1) # on en prend un autre.

        Res.append(L[j]) # Sinon, on ajoute l'élément L[j] dans le résultat.
    return(Res)


def reinitialisation() :
    """ Réinitialise les variables globales."""

    donnee = [envois, repertoire, malade, hospital, contact, resultat]
    for k in donnee :
        n = len(k)
        for i in range(n) :
            k.pop()

## protocole
def CreationId(n) :
    """
    n (entier)

    Crée un ephID de taille n.
    """
    Id = ""
    for k in range(n) :
        typeCarac = rd.randint(0,2) # On choisit un type de caractère.
        p = len(caractere[typeCarac])
        Id = Id + caractere[typeCarac][rd.randint(0,p-1)]
        # On choisit un caractère aléatoire du type de caractère préalablement choisi, et on concatène.
    return(Id)


def ajout_id_envoi(n,taille_id) :
    """
    n (entier) : individu numéro n
    taille_id (entier)

    envois[n] : liste des ephIDs envoyés par n
    """
    envois[n].append(CreationId(taille_id))


def creation_malade(m,N) :
    """
    N (entier) : Nombre d'individus
    m (flottant) : Pourcentage de malades

    Créer la liste malade.
    """
    for k in range(N) : # Pour tous les individus k,
        if rd.random() <= m : # si k fait partie des malades,
            malade.append(k) # alors on considère que k est malade.

def id_de_malade(N) :
    """
    N (entier) : nombre d'individus

    Construit hospital.
    """
    for k in malade :
        for i in envois[k] :
            hospital.append(i)


def individu_contact(n,d,N) :
    """
    n (entier) : individu numéro n
    d (flottant) : Facteur de sociabilité (Caractérise le brassage des individus).

    Construit contact[n].
    """
    for k in range(N) : # Pour tous les individus k,
        if k != n : # si cet individu  k n'est pas n,
            if rd.random() < d : # et s'il est possible que k entre en contact avec n,
                contact[n].append(k) # alors on considère que k est entré en contact avec n,
                contact[k].append(n) # et que n est entré en contact avec k.
# La relation "entre en contact avec" est symétrique non-réflexive.

def creation_repertoire(k) :
    """
    k (entier): individu numéro k

    Construit repertoire[k].
    """
    for i in contact[k] : # Pour tous les individus i ayant été en contact avec k,
        ephIDs_recu_par_k = p_parmi_elts_de_L(envois[i])
        # on selectionne un certain nombre d'ephIDs envoyés par i.
        # On considère que ces ephIDs sont ceux reçu par k.
        for j in ephIDs_recu_par_k : # Pour tous les ephIDs j envoyés par i reçu par k,
            repertoire[k].append(j) # on ajoute ces ephIDs au répertoire de k.


def A_risque(n) :
    """
    n (entier)

    Indique si l'individu n en question est réellement à risque ou pas. Un individu
    est considéré réellement à risque s'il a été en contact avec au moins 2 malades.
    """
    compteur = 0
    for k in contact[n] :
        if estDans(k,malade) :
            compteur = compteur + 1
    # On compte le nombre de malades parmi les contacts de n.

    if compteur >= 2 :
        return True
    else :
        return False


def risque() :
    """
    resultat_risque[k] : (Booléen) si l'individu k est à risque.
    """
    N = len(contact) # Nombre d'individus.
    resultat_risque = [] # Liste de Booléens à remplir.
    for k in range(N) :
        resultat_risque.append(A_risque(k))

    return resultat_risque

def auto_confinement(n,seuil) :
    """
    n (entier) : numéro de l'individu
    seuil (entier)

    Indique si n doit s'autoconfiner, c'est-à-dire si k a été notifié à risque
    ou non par le protocole.

    n est notifié à risque par le protocole dès que n a recu plus de
    (seuil) ephID(s) provenant d'individus notifiés malades.
    """
    compteur = 0
    for i in hospital :
        if estDans(i,repertoire[n]) :
            compteur = compteur + 1
    # On compte le nombre d'ephIDs reçus par n provenant de malades.

    if compteur >= seuil :
        return True
    return False


def simulation(N,m,d,taille_id,p,seuil) :
    """
    N (entier): nombre d'individu
    m (flottant): pourcentage d'individus malades
    d (flottant): facteur de sociabilité
    taille_id (entier) : taille des ephIDs
    p (entier): nombre d'ephIDs envoyés par personne
    seuil (entier): Nombre d'ephIDs reçus à partir duquel l'individu est
    considéré en danger et doit s'autoconfiner.

    Indique qui doit s'autoconfiner en construisant la liste 'résultat'.

    résultat[k] : (booléen) doit s'autoconfiner
    """
    # Initialisation :
    reinitialisation()

    for k in range(N) :
        contact.append([])
        envois.append([])
        repertoire.append([])

    # Envoi :
    for n in range(N) :
        for i in range(p) :
            ajout_id_envoi(n,taille_id)

    # Malade :
    creation_malade(m,N)

    # Hospital :
    id_de_malade(N)

    # Répertoire et contact :
    for n in range(N) :
        individu_contact(n,d,N)
        creation_repertoire(n)

    # Résultat :
    for k in range(N) :
        resultat.append([])
        verdict = auto_confinement(k,seuil)
        resultat[k] = verdict

    return resultat


def graphe1(N,m,taille_id,p,seuil,s) :
    """ quotient, quotient_réel = f(% de malades)
    quotient : pourcentage des individus notifiés malades (protocole)
    quotient_réel : pourcentage des individus réellement à risque (idéal)

    N (entier): nombre d'individus
    m (flottant): pourcentage d'individus malades
    d (flottant): facteur de sociabilité
    taille_id (entier): taille des ephIDs
    p (entier): nombre d'ephIDs envoyées par individu
    seuil (entier): nombre d'ephIDs reçus à partir duquel l'individu est
    considéré en danger et doit s'autoconfiner
    s (entier): nombre de simulation par quotient

    """
    X = [] # Liste des facteurs de sociabilité.
    Y = [] # Liste des pourcentages des individus notifiés malades.
    Y_bis = [] # Liste des pourcentages des individus réellement à risque.
    liste_quotient = []
    liste_quotient_bis = []

    for k in range(101) :
        X.append(0.03*(1-k/100) + 0.2*(k/100))
# Facteur de sociabilité variant de 3 à 20%.

    for d in X :
        for i in range(s) :
            r = simulation(N,m,d,taille_id,p,seuil)

            # Création quotient :
            b = 0 # Nombre d'individus notifiés malades.
            for Bool in r :
                if Bool :
                    b += 1
            quotient = b/N
            print(quotient)
            liste_quotient.append(quotient)

            # Création quotient idéal :
            r = risque()
            compteur_risque = 0
            for k in r :
                if k :
                    compteur_risque += 1

            quotient_bis = compteur_risque / N
            liste_quotient_bis.append(quotient_bis)


        Y_bis.append(moyenne(liste_quotient_bis))
        Y.append(moyenne(liste_quotient))

        liste_quotient = []
        liste_quotient_bis = []

        print("***")

    # Construction graphe :
    plt.plot(X,Y,marker = "o", markersize = "2", label = "Pourcentage d'individus notifiés (issue du protocole)", color = "red")
    plt.plot(X,Y_bis,marker = "o", markersize = "2", label = "Pourcentage de vrai cas-contacts (idéal)", color = "blue")
    plt.xlabel("Facteur de sociabilité", fontsize = 20)
    plt.ylabel("Pourcentage de cas-contacts", fontsize = 20)
    plt.title("Corrélation entre le nombre de contacts et le nombre d'individus notifiés (pourcentage de malades fixé).", fontsize = 15)

    plt.legend(fontsize = 12)
    plt.grid()
    plt.show()

    print("Done !")


def graphe2(N,d,taille_id,p,seuil,s) :
    """ quotient, quotient_réel = f(% malades)
    quotient : pourcentage des individus notifiés malades (protocole)
    quotient_réel : pourcentage des individus réellement à risque (idéal)

    N (entier): nombre d'individus
    d (flottant): facteur de sociabilisation
    taille_id (entier): taille des ephIDs
    p (entier): nombre d'ephIDs envoyés par personne
    seuil (entier): nombre d'ephIDs reçu à partir duquel l'individu est
    considéré comme cas-contact et doit s'autoconfiner
s : nombre de simulation par quotient
    """
    X = [] # Liste des pourcentages de malades.
    Y = [] # Liste des pourcentages des individus notifiés malades.
    Y_bis = [] # liste des pourcentages des individus réellement à risque.

    liste_quotient = []
    liste_quotient_bis = []

    for k in range(101) :
        X.append(0.03*(1-k/100) + 0.2*(k/100))
        # Pourcentage de malades variant entre 3 et 20%.

    for m in X :
        for i in range(s) :
            r = simulation(N,m,d,taille_id,p,seuil)

            # Création quotient :
            b = 0 # Nombre d'individus notifiés malades.
            for Bool in r :
                if Bool :
                    b += 1
            quotient = b/N
            print(quotient)
            liste_quotient.append(quotient)

            # Création quotient idéal :
            r = risque()
            compteur_risque = 0
            for k in r :
                if k :
                    compteur_risque += 1

            quotient_bis = compteur_risque / N
            liste_quotient_bis.append(quotient_bis)

        Y.append(moyenne(liste_quotient))
        Y_bis.append(moyenne(liste_quotient_bis))

        liste_quotient = []
        liste_quotient_bis = []
        print("***")

    # Construction graphe
    plt.plot(X,Y,marker = "o", markersize = "2", label = "Pourcentage d'individus notifiés (issue du protocole)", color = "red" )
    plt.plot(X,Y_bis,marker = "o", markersize = "2", label = "Pourcentage de vrai cas-contacts (idéal)", color = "blue")

    plt.xlabel("Pourcentage de malades", fontsize = 20)
    plt.ylabel("Pourcentage de cas-contacts", fontsize = 20)
    plt.title("Corrélation entre le pourcentage de malades et le nombre d'individus notifiés (facteur de sociabilité fixé).", fontsize = 15)

    plt.legend(fontsize = 12)
    plt.grid()
    plt.show()

    print("Done !")