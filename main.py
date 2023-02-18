import csv
from dictionnaire import *

#  ----- chemin des fichier.csv  ------

data_csv = "data/2020_installations_sportives.csv"  # fichier orginal (sujet)
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


import time


def chargment_graph(valeur, temps):
    print(valeur)
    time.sleep(temps)
    print("")

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
    with open(nom_fichier_entree, 'r', encoding="ISO-8859-1") as fichier_entree:
        reader = csv.reader(fichier_entree, delimiter=';')
        for ligne in reader:
            donnees.append(ligne)

        """
        ici la fonction crée un nouveau fichier avec le nom en paramètre 
        et avec une double boucle une qui récuperer les ligne 
        et l'autre les colonnes la fonction recupére les données de la liste et les ecrit dans le nouveau fichier csv
        """
    with open(nom_fichier_sortie, 'w', newline='') as fichier_sortie:
        writer = csv.writer(fichier_sortie, delimiter=';')
        ligne_max = 0
        for ligne in donnees:
            if ligne_max <= nombre_ligne:
                colonnes_selectionnees = [
                    ligne[colonne] for colonne in colonnes_a_recuperer
                ]
                ligne_max += 1
                writer.writerow(colonnes_selectionnees)

              
# Script 2 : Etape 3

"""
- Fonction : Chargement des données d'un fichier CSV et un fonction qui recupere les données d'un fichier CSV 
            et les stocks dans une liste 
- Paramètre : Le nom d'un fichier CSV 
- Retourne : une liste
"""


def chargement_de_données (nom_fichier_entree) :
    S = []
    with open(nom_fichier_entree, 'r', encoding="ISO-8859-1") as fichier_entree:
        reader = csv.reader(fichier_entree, delimiter=';')
        for ligne in reader:
            S.append(ligne)
        return S
      
S1=chargement_de_données(admissions_par_formation_detaillee_csv)
S2=chargement_de_données(communes_uniques_csv)
S3=chargement_de_données(installations_uniques_csv)

      
# Script 2 : Etape 4

"""
- Fonction : projection_simple
- Parametre : une liste contenant les donnèes d'un fichier csv 
- Retourne : rien vu qu'il y a un print  
"""


def projection_simple(liste_entrée, nomDeColonne):
    S = []
    """
    on parcourt les ligne de la liste puis les colonnes,aprés on recupére
    l'indexe de colonne et on le stock dans une variable pour garder l'index de colonne
    puis on va integrer les valeurs à une nouvelle liste
    """
    for ligne in range(len(liste_entrée)):
        for colonne in range(len(liste_entrée[ligne])):
            if liste_entrée[ligne][colonne] == nomDeColonne:
                index_colonne = colonne
        S.append(liste_entrée[ligne][index_colonne])
    print(S)
    return S


"""
- Fonction : projection_simple
- Parametre : une liste contenant les donnèes d'un fichier csv 
- Retourne : rien vu qu'il y a un print  
"""


def projection_simple_distinct(liste_entrée, nomDeColonne):
    S = []
    """
    on parcourt les ligne de la liste puis les colonnes,aprés on recupére
    l'indexe de colonne et on le stock dans une variable pour garder l'index de colonne
    puis on va integrer les valeurs à une nouvelle liste sans prendre les doublons =  
    """
    for ligne in range(len(liste_entrée)):
        for colonne in range(len(liste_entrée[ligne])):
            if liste_entrée[ligne][colonne] == nomDeColonne:
                index_colonne = colonne
        if liste_entrée[ligne][index_colonne] not in S:
            S.append(liste_entrée[ligne][index_colonne])
    return S

    """
    - Fonction : projection_multiple
    - Parametre :listes contenant les donnèes du fichier csv 
    - return une matrice contenant les colonnes selon les id mis en paramètres 
    """


def projection_multiple(liste_entrée, liste_nom_colonnes):
    S = [[0] * len(liste_nom_colonnes)] * len(liste_entrée)
    for i in range(len(liste_nom_colonnes)):
        liste = projection_simple(liste_entrée, liste_nom_colonnes[i])
        for j in range(len(liste)):
            S[j][i] = liste[j]
    print(S)

"""
projection_multiple(S2, ["codeInseeCommune","nomCommune"])
"""


"""
- Fonction : projection_multiple_disctinct
- Parametres : listes contenant les donnèes du fichier csv 
- return une matrice contenant les colonnes selon les id mis en     
    paramètres en évitant les doublons sur la deuxième colonne
  """

def projection_multiple_distinct(liste_entrée, liste_nom_colonnes):
    S = [[0] * len(liste_nom_colonnes)] * len(liste_entrée)
    for i in range(len(liste_nom_colonnes)):
        liste = projection_simple_distinct(liste_entrée, liste_nom_colonnes[i])
        for j in range(len(liste)):
            S[j][i] = liste[j]
    print(S)


projection_multiple_distinct(S1, ["codeInstallation", "codeInseeCommune"])


#Script 2 : Etape 5


def sélection_simple(liste_entrée, nomDeColonne, opérateur, valeur):
    if not (opérateur == '=' or opérateur == '>' or opérateur == '>=' or opérateur == '<=' or opérateur == '<>'):
        print("la valeur :", opérateur, " est incorrect !")
    else:
        S = []
        ...
        return S


def sélection_multiple(liste_entrée, operateurbooléen):
    if not (operateurbooléen == 'AND' or operateurbooléen == 'OR'):
        print("la valeur de l'operateur :", operateurbooléen, "est incorrect !")
    else:
        S = []
        ...
        return S


#Script 2 : Etape 6

"""
- Fonction : min
- Parametre : une liste contenant les donnèes d'un fichier csv et l'en tête d'une colonne 
- Retourne : la plus petite valeur de la colonne  
"""


def min (liste_entrée, nomDeColonne) :
  S = []
  for ligne in range(len(liste_entrée)) :
    for colonne in range (len(liste_entrée[ligne])) :
      if liste_entrée[ligne][colonne] == nomDeColonne :
        index_colonne = colonne
    S.append(liste_entrée[ligne][index_colonne]) 
    """on stock la premiere valeur dans la variable min et avec une boucle on va passer
    sur toute les valeurs de la colonne et si y'a une valeur plus petite que min, on ecrase
    l'ancienne valeure de min par la nouvelle """
  min = S[1] 
  for elem in S :
    if isinstance(elem, str): 
      print("veuillez selectionner une colonne avec des valeurs numerique")
      return None
    if min >= elem :
      min = elem 
  return min
    


"""
- Fonction : max
- Parametre : une liste contenant les donnèes d'un fichier csv et l'en tête d'une colonne
- Retourne : la plus grande valeur de la colonne  
"""


def max (liste_entrée, nomDeColonne) :
  S = []
  for ligne in range(len(liste_entrée)) :
    for colonne in range (len(liste_entrée[ligne])) :
      if liste_entrée[ligne][colonne] == nomDeColonne :
        index_colonne = colonne
    S.append(liste_entrée[ligne][index_colonne]) 
  """on stock la premiere valeur dans la variable max et avec une boucle on va passer
    sur toute les valeurs de la colonne et si y'a une valeur plus grnade que max, on ecrase
    l'ancienne valeure de max par la nouvelle """
  max = S[1]
  for elem in range(1, len(S)):
    if isinstance(S[elem], str): 
      print("veuillez selectionner une colonne avec des valeurs numerique")
      return None
    if max <= S[elem] :
      max = S[elem]
  return max



"""
- Fonction : compte
- Parametre : une liste contenant les donnèes d'un fichier csv et l'en tête d'une colonne
- Retourne : le nombre de valeur non nul d'une colonne  
"""


def compte (liste_entrée, nomDeColonne) :
  S = []
  for ligne in range(len(liste_entrée)) :
    for colonne in range (len(liste_entrée[ligne])) :
      if liste_entrée[ligne][colonne] == nomDeColonne :
        index_colonne = colonne
    S.append(liste_entrée[ligne][index_colonne]) 
  """à l'aide d'une boucle on passe par toutes les valeurs de la colonne
  et si la valeur est non nul on rajoute +1 au compteur """
  Compteur = 0
  for elem in range(1, len(S)):
    if isinstance(S[elem], str): 
      print("veuillez selectionner une colonne avec des valeurs numerique")
      return None
    if S[elem] != 0 :
      Compteur += 1
  return Compteur
  

"""
- Fonction : somme
- Parametre : une liste contenant les donnèes d'un fichier csv et l'en tête d'une colonne
- Retourne : la somme des valeurs d'une colonne   
"""


def somme (liste_entrée, nomDeColonne) :
  S = []
  for ligne in range(len(liste_entrée)) :
    for colonne in range (len(liste_entrée[ligne])) :
      if liste_entrée[ligne][colonne] == nomDeColonne :
        index_colonne = colonne
    S.append(liste_entrée[ligne][index_colonne]) 
  """à l'aide d'une boucle on passe par toutes les valeurs de la colonne
  et on l'adissionne à la variable somme """  
  Somme = 0
  for elem in range(1, len(S)):
    Somme += int(S[elem])
  return Somme


"""
- Fonction : moyenne
- Parametre : une liste contenant les donnèes d'un fichier csv et l'en tête d'une colonne
- Retourne : la moyenne des valeurs d'une colonne   
"""


def moyenne (liste_entrée, nomDeColonne) :
  S = []
  for ligne in range(len(liste_entrée)) :
    for colonne in range (len(liste_entrée[ligne])) :
      if liste_entrée[ligne][colonne] == nomDeColonne :
        index_colonne = colonne
    S.append(liste_entrée[ligne][index_colonne]) 
  """ on fait appel à la fonction somme pour calculer la somme des valeurs
  puis on la devise sur le nombre de valeur de la colonne"""
  Moyenne = int(somme(liste_entrée, nomDeColonne))/(len(S)-1)
  return Moyenne

#Script 2 : Etape 7

"""
- Fonction : ordonne 
- Parametre : une liste contenant les donnèes d'un fichier csv et l'en tête d'une colonne 
                et le sens croissant ou decroissant
- Retourne : la liste d'entrée avec le sens donnée en paramètre
"""


def ordonne(liste_entrée, nomDeColonne, sens):
  S = []
  for ligne in range(len(liste_entrée)) :
    for colonne in range (len(liste_entrée[ligne])) :
      if liste_entrée[ligne][colonne] == nomDeColonne :
        index_colonne = colonne
    S.append(liste_entrée[ligne][index_colonne])
  """on recupére l'en tête pour pas qu'il le déplace et on le met dans une
  variable et les valeurs dans une autre si le sens et croissant on utilise la
  methode sort() pour la variable contenant les valeurs, et si c'est decroissant
  on fait pareil sauf qu'en paramètre de la methode on fait un reverse=True"""
  if sens == "croissant" :
    tete = S[0]
    reste = S[1:]
    reste.sort()
  elif sens == "decroissant" :
    tete = S[0]
    reste = S[1:]
    reste.sort(reverse=True)
    
  return[tete]+reste


def ordonne_multiple(liste_entrée, liste_nom_colonnes, sens):
  S = []
  ...
  return S


#Script 2 : Etape 8 

def jointure(liste_entrée, liste_sortie, nomDeColonne):
  S = []
  ...
  return S


  

  
# ----------  Test des script / Fonction ----------

# ------ Test Script 1 : Etape 1 ------

#lecture_csv(data_csv)

# ------ Test Script 1 : Etape 2 ------

"""
#Position des en-tête codeInstallation = 4, nomInstallation = 5, nbEquipements = 28, adresse = 6, nbParking = 16, 
nbParkingHandi = 17
lire_et_ecrire_csv(data_csv, installations_uniques_csv, [codeInstallation, nomInstallation, nbEquipements, adresse, 
nbParking, nbParkingHandi], 444)

#Position des en-tête codeInseeCommune = 2, nomComune = 3, codeDepartement = 0, nomDepartement = 1
lire_et_ecrire_csv(data_csv, communes_uniques_csv, [codeInseeCommune, nomCommune, codeDepartement, nomDepartement], 146)

#Position des en-tête codeInstallation = 4, codeInseeCommune = 2, libelle = 9, metro = 19, bus = 20, tram = 21,
train = 22, bateau = 23, autreTransport = 24, aucunTransport = 25, dateMAJ = 26, dateCreation = 27
lire_et_ecrire_csv(data_csv, admissions_par_formation_detaillee_csv, [codeInstallation, codeInseeCommune, libelle, 
metro, bus, tram, train, bateau, autreTransport, aucunTransport, dateMAJ, dateCreation], 444)

# ---- lecture du test script 1 : etape 2 ----

chargment_graph("Chargement de fichier csv Admission", 2)
lecture_csv(admissions_par_formation_detaillee_csv)
space_graph(4)

chargment_graph("Chargement de fichier csv Communes", 4)
lecture_csv(communes_uniques_csv)
space_graph(4)

chargment_graph("Chargement de fichier csv Installations", 4)
lecture_csv(installations_uniques_csv)

space_graph(2)
print("Chargement des fichiers csv terminer")
space_graph(4)
"""

# ------ Test Script 2 : Etape 3 ------

"""
print("test S1 : ", S1)
print("test S2 : ", S2)
print("test S3 : ", S3)
"""

# ------ Test Script 2 : Etape 4 ------

# ------ Test Script 2 : Etape 5 ------

# ------ Test Script 2 : Etape 6 ------

# ------ Test Script 2 : Etape 7 ------

# ------ Test Script 2 : Etape 8 ------

# ------ Test Script 3 : Etape 9 ------

# ------ Test Script 4 : Etape 10 -----
