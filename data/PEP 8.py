import csv
from dictionnaire import *

#  ----- chemin des fichier.csv  ------

data_csv = "2020_installations_sportives.csv"  # fichier orginal (sujet)
"""
Fichier constitué du code de l'installation, nom de l'installation, nombre d'Equipement, de l'adresse 
et du nombre de place de parking handicaper ou pas.
"""
installations_uniques_csv = "data/IntallationsUniques.csv"

# Fichier constituer du code INSEE de la commune, du nom de la commune, du code du department et du nom du département.
communes_uniques_csv = "data/CommunesUniques.csv"
"""
Fichier constituer du code de l'installation, du code INSEE de la commune, du libelle, des different moyen de transport
(Metro,Bus,Tram,Train,Bateau ou autre voir pas) et des la date de mise à jour et de création
"""
admissions_par_formation_detaillee_csv = "data/AdmissionParFormationDetaillee.csv"


# ----- Fonction esthétique / grap -----
# fonction espace


def space_graph(valeur):
    for i in range(valeur):
        print("")


# fonction chargment

def chargment_graph(valeur, condition):
    print("")
    print(valeur)
    print("")
    if condition != 1:
        print(input("Appuyer sur Entrait pour continer :"))

# ----  Fonction fonctionnelle -----


"""
# Fonction : exemple de fonction
# parametre : nom_fichier_csv, str
# retourne : S
"""

# Script 1 : Etape 1

"""
- Fonction : Lecture_csv
- Parametre : nom d'un fichier csv 
- Retourne : rien vu qu'il y a un print mais on pourrais stocker dans un variable 
"""


def lecture_csv(nom_fichier_csv):
    # Ouverture d'un fichier csv avec en paramètres un mode "r" read = lecture
    with open(nom_fichier_csv, errors="ignore") as csv_file:
        # Lecture du fichier csv
        csv_reader = csv.reader(csv_file)
        # Boucle pour lire le fichier csv
        for line in csv_reader:
            # Affichage de la ligne lu
            print(line)


# Script 1 : Etape 2


"""
- Fonction : lecture et écriture de fichier CSV 
- Paramètre : le nom d'un fichier CSV entrant et d'autre fichier CSV sortant, le nombre de colonne 
              et le nombre de linge a recuper 
- Retourne : ecriture dans le fichier CSV sortant   
"""


def lire_et_ecrire_csv(nom_fichier_entree, nom_fichier_sortie, colonnes_a_recuperer, nombre_ligne):
    """
    Ici on lit le fichier csv et on rentre les donn""ées dans une liste
    """

    donnees = []
    with open(nom_fichier_entree, 'r', encoding='ISO-8859-1') as fichier_entree:
        reader = csv.reader(fichier_entree, delimiter=';')
        for ligne in reader:
            donnees.append(ligne)

    """
    ici la fonction crée un nouveau fichier avec le nom en paramètre et avec une double boucle une qui récuperer 
    les ligne et l'autre les colonnes la fonction recupére les données de la liste et les ecrit dans 
    le nouveau fichier csv
    """
    with open(nom_fichier_sortie, 'w', newline='') as fichier_sortie:
        writer = csv.writer(fichier_sortie, delimiter=';')
        ligne_max = 0
        for ligne in donnees:
            if ligne_max <= nombre_ligne:
                colonnes_selectionnees = [ligne[colonne] for colonne in colonnes_a_recuperer]
                ligne_max += 1
                writer.writerow(colonnes_selectionnees)


# Script 2 : Etape 3

"""
- Fonction : Chargement des données d'un fichier CSV et un fonction qui recupere les données d'un fichier CSV 
            et les stocks dans une liste 
- Paramètre : Le nom d'un fichier CSV 
- Retourne : une liste
"""


def chargement_de_donnees(nom_fichier_entree):
    s = []
    with open(nom_fichier_entree, 'r', encoding="ISO-8859-1") as fichier_entree:
        reader = csv.reader(fichier_entree, delimiter=';')
        for ligne in reader:
            s.append(ligne)
        return s


s1 = chargement_de_donnees(admissions_par_formation_detaillee_csv)
s2 = chargement_de_donnees(communes_uniques_csv)
s3 = chargement_de_donnees(installations_uniques_csv)

# Script 2 : Etape 4

"""
- Fonction : projection_simple
- Parametre : une liste contenant les donnèes d'un fichier csv 
- Retourne : rien vu qu'il y a un print  
"""


def projection_simple(liste_entree, nom_de_colonne):
    s = []
    """
    on parcourt les ligne de la liste puis les colonnes,aprés on recupére
    l'indexe de colonne et on le stock dans une variable pour garder l'index de colonne
    puis on va integrer les valeurs à une nouvelle liste
    """
    for ligne in range(len(liste_entree)):
        for colonne in range(len(liste_entree[ligne])):
            if liste_entree[ligne][colonne] == nom_de_colonne:
                index_colonne = colonne
        s.append(liste_entree[ligne][index_colonne])
    return s


"""
- Fonction : projection_simple
- Parametre : une liste contenant les donnèes d'un fichier csv 
- Retourne : rien vu qu'il y a un print  
"""


def projection_simple_distinct(liste_entree, nom_de_colonne):
    s = []
    """
    on parcourt les ligne de la liste puis les colonnes,aprés on recupére
    l'indexe de colonne et on le stock dans une variable pour garder l'index de colonne
    puis on va integrer les valeurs à une nouvelle liste sans prendre les doublons =  
    """
    for ligne in range(len(liste_entree)):
        for colonne in range(len(liste_entree[ligne])):
            if liste_entree[ligne][colonne] == nom_de_colonne:
                index_colonne = colonne
        if liste_entree[ligne][index_colonne] not in s:
            s.append(liste_entree[ligne][index_colonne])
    return s


"""
    - Fonction : projection_multiple
    - Parametre :listes contenant les donnèes du fichier csv 
    - return une matrice contenant les colonnes selon les id mis en paramètres 
    """


def projection_multiple(liste_entree, liste_nom_colonnes):
    s = [[0] * len(liste_nom_colonnes)] * len(liste_entree)
    for i in range(len(liste_nom_colonnes)):
        liste = projection_simple(liste_entree, liste_nom_colonnes[i])
        for j in range(len(liste)):
            s[j][i] = liste[j]
    return s


"""
projection_multiple(S2, ["codeInseeCommune","nomCommune"])
"""

"""
- Fonction : projection_multiple_disctinct
- Parametres : listes contenant les donnèes du fichier csv 
- return une matrice contenant les colonnes selon les id mis en     
    paramètres en évitant les doublons sur la deuxième colonne
"""


def projection_multiple_distinct(liste_entree, liste_nom_colonnes):
    s = [[0] * len(liste_nom_colonnes)] * len(liste_entree)
    for i in range(len(liste_nom_colonnes)):
        liste = projection_simple_distinct(liste_entree, liste_nom_colonnes[i])
        for j in range(len(liste)):
            s[j][i] = liste[j]
    return s


# Script 2 : Etape 5


def selection_simple(liste_entree, nom_de_colonne, operateur, valeur):

    if not (operateur == '=' or operateur == '>' or operateur == '>=' or operateur == '<=' or operateur == '<>'):
        print("la valeur :", operateur, " est incorrect !")
    else:
        s = []
        ...
        return s, liste_entree, nom_de_colonne, valeur


def selection_multiple(liste_entree, operateurbooleen):
    if not (operateurbooleen == 'AND' or operateurbooleen == 'OR'):
        print("la valeur de l'operateur :", operateurbooleen, "est incorrect !")
    else:
        s = []
        ...
        return s, liste_entree


# Script 2 : Etape 6

"""
- Fonction : min
- Parametre : une liste contenant les donnèes d'un fichier csv et l'en tête d'une colonne 
- Retourne : la plus petite valeur de la colonne  
"""


def minimum(liste_entree, nom_de_colonne):
    s = []
    for ligne in range(len(liste_entree)):
        for colonne in range(len(liste_entree[ligne])):
            if liste_entree[ligne][colonne] == nom_de_colonne:
                index_colonne = colonne
        s.append(liste_entree[ligne][index_colonne])

        """
        on stock la premiere valeur dans la variable min et avec une boucle on va passer
        sur toute les valeurs de la colonne et si y'a une valeur plus petite que min, on ecrase
        l'ancienne valeure de min par la nouvelle 
        """
    minimum_s = s[1]
    for elem in s:
        if isinstance(elem, str):
            print("veuillez selectionner une colonne avec des valeurs numerique")
            return None
        if minimum_s >= elem:
            minimum_s = elem
    return minimum_s


"""
- Fonction : max
- Parametre : une liste contenant les donnèes d'un fichier csv et l'en tête d'une colonne
- Retourne : la plus grande valeur de la colonne  
"""


def maximum(liste_entree, nom_de_colonne):
    s = []
    for ligne in range(len(liste_entree)):
        for colonne in range(len(liste_entree[ligne])):
            if liste_entree[ligne][colonne] == nom_de_colonne:
                index_colonne = colonne
        s.append(liste_entree[ligne][index_colonne])

    """
    on stock la premiere valeur dans la variable max et avec une boucle on va passer
      sur toute les valeurs de la colonne et si y'a une valeur plus grnade que max, on ecrase
      l'ancienne valeure de max par la nouvelle
      """
    maximum_s = s[1]
    for elem in range(1, len(s)):
        if isinstance(s[elem], str):
            print("veuillez selectionner une colonne avec des valeurs numerique")
            return None
        if maximum_s <= s[elem]:
            maximum_s = s[elem]
    return maximum_s


"""
- Fonction : compte
- Parametre : une liste contenant les donnèes d'un fichier csv et l'en tête d'une colonne
- Retourne : le nombre de valeur non nul d'une colonne  
"""


def compte(liste_entree, nom_de_colonne):
    s = []
    for ligne in range(len(liste_entree)):
        for colonne in range(len(liste_entree[ligne])):
            if liste_entree[ligne][colonne] == nom_de_colonne:
                index_colonne = colonne
        s.append(liste_entree[ligne][index_colonne])

    """
    à l'aide d'une boucle on passe par toutes les valeurs de la colonne
    et si la valeur est non nul on rajoute +1 au compteur 
    """
    compteur = 0
    for elem in range(1, len(s)):
        if isinstance(s[elem], str):
            print("veuillez selectionner une colonne avec des valeurs numerique")
            return None
        if s[elem] != 0:
            compteur += 1
    return compteur


"""
- Fonction : somme
- Parametre : une liste contenant les donnèes d'un fichier csv et l'en tête d'une colonne
- Retourne : la somme des valeurs d'une colonne   
"""


def somme(liste_entree, nom_de_colonne):
    s = []
    for ligne in range(len(liste_entree)):
        for colonne in range(len(liste_entree[ligne])):
            if liste_entree[ligne][colonne] == nom_de_colonne:
                index_colonne = colonne
        s.append(liste_entree[ligne][index_colonne])

    """
    à l'aide d'une boucle on passe par toutes les valeurs de la colonne
    et on l'adissionne à la variable somme 
    """
    somme_s = 0
    for elem in range(1, len(s)):
        somme_s += int(s[elem])
    return somme_s


"""
- Fonction : moyenne
- Parametre : une liste contenant les donnèes d'un fichier csv et l'en tête d'une colonne
- Retourne : la moyenne des valeurs d'une colonne   
"""


def moyenne(liste_entree, nom_de_colonne):
    s = []
    for ligne in range(len(liste_entree)):
        for colonne in range(len(liste_entree[ligne])):
            if liste_entree[ligne][colonne] == nom_de_colonne:
                index_colonne = colonne
        s.append(liste_entree[ligne][index_colonne])

    """ 
    on fait appel à la fonction somme pour calculer la somme des valeurs
    puis on la devise sur le nombre de valeur de la colonne
    """
    moyenne_s = int(somme(liste_entree, nom_de_colonne)) / (len(s) - 1)
    return moyenne_s


# Script 2 : Etape 7

"""
- Fonction : ordonne 
- Parametre : une liste contenant les donnèes d'un fichier csv et l'en tête d'une colonne 
                et le sens croissant ou decroissant
- Retourne : la liste d'entrée avec le sens donnée en paramètre
"""


def ordonne(liste_entree, nom_de_colonne, sens):
    s = []
    for ligne in range(len(liste_entree)):
        for colonne in range(len(liste_entree[ligne])):
            if liste_entree[ligne][colonne] == nom_de_colonne:
                index_colonne = colonne
        s.append(liste_entree[ligne][index_colonne])

    """
    on recupére l'en tête pour pas qu'il le déplace et on le met dans une
    variable et les valeurs dans une autre si le sens et croissant on utilise la
    methode sort() pour la variable contenant les valeurs, et si c'est decroissant
    on fait pareil sauf qu'en paramètre de la methode on fait un reverse=True
    """
    if sens == "croissant":
        tete = s[0]
        reste = s[1:]
        reste.sort()
    elif sens == "decroissant":
        tete = s[0]
        reste = s[1:]
        reste.sort(reverse=True)

    return [tete] + reste


def ordonne_multiple(liste_entree, liste_nom_colonnes, sens):
    s = []
    ...
    return s, liste_entree, liste_nom_colonnes, sens


# Script 2 : Etape 8

def jointure(liste_entree, liste_sortie, nom_de_colonne):
    s = []
    ...
    return s, liste_entree, liste_sortie, nom_de_colonne


# ----------  Test des script / Fonction ----------

chargment_graph("début de test de fonction ...", 0)

# ------ Test Script 1 : Etape 1 ------
chargment_graph("Scripte 1 : Etape 1", 1)

lecture_csv(data_csv)

# ------ Test Script 1 : Etape 2 ------
chargment_graph("Scripte 1 : Etape 2", 1)

"""
#Position des en-tête codeInstallation = 4, nomInstallation = 5, nbEquipements = 28, adresse = 6, nbParking = 16,
#nbParkingHandi = 17
"""
lire_et_ecrire_csv(data_csv, installations_uniques_csv,
                   [codeInstallation, nomInstallation, nbEquipements, adresse, nbParking, nbParkingHandi], 444)

"""
#Position des en-tête codeInseeCommune = 2, nomComune = 3, codeDepartement = 0, nomDepartement = 1
"""
lire_et_ecrire_csv(data_csv, communes_uniques_csv, [codeInseeCommune, nomCommune, codeDepartement, nomDepartement], 146)

"""
#Position des en-tête codeInstallation = 4, codeInseeCommune = 2, libelle = 9, metro = 19, bus = 20, tram = 21,
#train = 22, bateau = 23, autreTransport = 24, aucunTransport = 25, dateMAJ = 26, dateCreation = 27
"""
lire_et_ecrire_csv(data_csv, admissions_par_formation_detaillee_csv, [codeInstallation, codeInseeCommune, libelle,
                                                                      metro, bus, tram, train, bateau, autreTransport,
                                                                      aucunTransport, dateMAJ, dateCreation], 444)

# ---- lecture du test script 1 : etape 2 ----

chargment_graph("Chargement de fichier csv Admission", 1)
lecture_csv(admissions_par_formation_detaillee_csv)
space_graph(4)

chargment_graph("Chargement de fichier csv Communes", 1)
lecture_csv(communes_uniques_csv)
space_graph(4)

chargment_graph("Chargement de fichier csv Installations", 1)
lecture_csv(installations_uniques_csv)

space_graph(2)
print("Chargement des fichiers csv terminer")
space_graph(4)


# ------ Test Script 2 : Etape 3 ------
chargment_graph("Scripte 2 : Etape 3", 1)

chargment_graph("Fichier S1", 1)
print("test S1 : ", s1)
chargment_graph("Fichier S2", 1)
print("test S2 : ", s2)
chargment_graph("Fichier S3", 1)
print("test S3 : ", s3)

# ------ Test Script 2 : Etape 4 ------
chargment_graph("Scripte 2 : Etape 4", 1)

print("Projection Simple : ", projection_simple(s1, 'libelle'))
print("Projection Multiple : ", projection_multiple(s2, ["codeInseeCommune", "nomCommune"]))
print("Projection Simple Distinct : ")
print("Projoection Multiple Distinct : ", projection_multiple_distinct(s2, ["codeInstallation", "codeInseeCommune"]))

# ------ Test Script 2 : Etape 5 ------
chargment_graph("Scripte 2 : Etape 5", 1)

print("Sélection Simple : ")
print("Sélection Multiple : ")

# ------ Test Script 2 : Etape 6 ------
chargment_graph("Scripte 2 : Etape 6", 1)

print("Le minimum est : ")
print("Le maximum est : ")
print("Le compte est : ")
print("La somme est : ")
print("La moyenne est : ")

# ------ Test Script 2 : Etape 7 ------
chargment_graph("Scripte 2 : Etape 7", 1)

print("Ordonne : ")
print("Ordonne Multiple : ")

# ------ Test Script 2 : Etape 8 ------
chargment_graph("Scripte 2 : Etape 8", 1)

print("Jointure : ")

# ------ Test Script 3 : Etape 9 ------
chargment_graph("Scripte 3 : Etape 9", 1)

# ------ Test Script 4 : Etape 10 -----
chargment_graph("Scripte 4 : Etape 10", 1)


print("The End !")
