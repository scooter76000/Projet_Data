import csv
from dictionnaire import *
from data.test_sujet_annexe import *

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


def lire_et_ecrire_csv(nom_fichier_entree, nom_fichier_sortie,
                       colonnes_a_recuperer, nombre_ligne):
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


def chargement_de_données(nom_fichier_entree):
  S = []
  with open(nom_fichier_entree, 'r', encoding="ISO-8859-1") as fichier_entree:
    reader = csv.reader(fichier_entree, delimiter=';')
    for ligne in reader:
      S.append(ligne)
    return S


S1 = chargement_de_données(admissions_par_formation_detaillee_csv)
S2 = chargement_de_données(communes_uniques_csv)
S3 = chargement_de_données(installations_uniques_csv)


def chargement_de_données_bis(tableau, headers):
  result = []
  header_row = tableau[0]
  header_indexes = [
    i for i in range(len(header_row)) if header_row[i] in headers
  ]
  result.append(header_row)

  for row in tableau[1:]:
    converted_row = []
    for i, item in enumerate(row):
      if i in header_indexes:
        if item == '':
          converted_row.append(0)
        else:
          converted_row.append(int(item))
      else:
        converted_row.append(item)
    result.append(converted_row)

  return result


S1_bis = chargement_de_données_bis(
  S1, ["nbEquipements", "nbParking", "nbParkingHandi"])
S2_bis = chargement_de_données_bis(S2, ["codeInseeCommune", "codeDepartement"])
S3_bis = chargement_de_données_bis(S3, [
  "codeInseeCommune", "metro", "bus", "tram", "train", "bateau",
  "autreTransport", "aucunTransport"
])

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
  #print(S)
  return S


"""
def projection_multiple_v3(liste_entree, liste_nom_colonnes):
    s = [] 
    nom_de_colonne_1 = liste_nom_colonnes[0]
    nom_de_colonne_2 = liste_nom_colonnes[1]

    liste_nom_colonnes_1 = projection_simple(liste_entree, nom_de_colonne_1)
    liste_nom_colonnes_2 = projection_simple(liste_entree, nom_de_colonne_2)  
  
    for i in range(len(liste_nom_colonnes_1)):
        index_a = liste_nom_colonnes_1[i]
        index_b = liste_nom_colonnes_2[i]
        s.append([index_a, index_b])
    return s
"""
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
  s = []
  nombre_colonnes = len(liste_nom_colonnes)
  colonnes = [
    projection_simple(liste_entrée, colonne) for colonne in liste_nom_colonnes
  ]
  for i in range(len(colonnes[0])):
    s.append([colonnes[j][i] for j in range(nombre_colonnes)])

  return s


"""
- Fonction : projection_multiple_disctinct
- Parametres : listes contenant les donnèes du fichier csv 
- return une matrice contenant les colonnes selon les id mis en     
    paramètres en évitant les doublons sur la deuxième colonne
"""


def projection_multiple_distinct(liste_entrée, liste_nom_colonnes):
  s = []
  nombre_colonnes = len(liste_nom_colonnes)
  colonnes = [
    projection_simple_distinct(liste_entrée, colonne)
    for colonne in liste_nom_colonnes
  ]
  for i in range(len(colonnes[nombre_colonnes - 1])):
    s.append([colonnes[j][i] for j in range(nombre_colonnes)])
  return s


# projection_multiple_distinct(S1, ["codeInstallation", "codeInseeCommune"])

# Script 2 : Etape 5
"""
- Fonction : selection_simple
- Parametre : Une liste contenant les données d’un fichier csv, le nom
de la colonne à récupérer, un operateur de comparaison, une valeur à comparer.     
- Retourne : Une liste avec les valeurs qui ont été comparé avec une 
la valeur entré en paramètre selon l’operateur de comparaison. 
"""


def sélection_simple(liste_entrée, nomDeColonne, operateur, valeur):
  s = projection_simple(liste_entrée, nomDeColonne)
  """Ici on vérifie si l’opérateur entré en paramètre n’est pas dans la liste, on affiche un message d’erreur. """
  if not (operateur == '=' or operateur == '>' or operateur == '>='
          or operateur == '<=' or operateur == '<>'):
    print("L'opérateur '", operateur, "' est incorrect !")
    return None
  selection_Simple = [s[0]]
  """On parcourt la liste et si les éléments sont des valeurs numérique "int" on les compare à la valeur en
    paramètre selon l’opérateur choisi et on ajoute la valeur dans la liste (exemple les valeurs qui sont
    strictement plus grande que 2)."""
  for elem in s:
    if isinstance(elem, int):
      if operateur == "<=":
        if elem <= valeur:
          selection_Simple.append(elem)
      elif operateur == ">":
        if elem > valeur:
          selection_Simple.append(elem)
      elif operateur == ">=":
        if elem >= valeur:
          selection_Simple.append(elem)
      elif operateur == "=":
        if elem == valeur:
          selection_Simple.append(elem)
      elif operateur == "<>":
        if elem != valeur:
          selection_Simple.append(elem)
      """si les valeurs sont des chaines de caractère "str"le processus est le même sauf que les
        operateurs qu’on peut utiliser sont moins nombreux """
    elif isinstance(elem, str):
      if operateur == "=":
        if elem == valeur:
          selection_Simple.append(elem)
      elif operateur == "<>":
        if elem != valeur:
          selection_Simple.append(elem)
  return selection_Simple


def sélection_multiple(liste_entrée, operateurbooléen):
  if not (operateurbooléen == 'AND' or operateurbooléen == 'OR'):
    print("la valeur de l'operateur :", operateurbooléen, "est incorrect !")
  else:
    S = []
    ...
    return S


# Script 2 : Etape 6
"""
- Fonction : min
- Parametre : une liste contenant les donnèes d'un fichier csv et l'en tête d'une colonne 
- Retourne : la plus petite valeure de la colonne  
"""


def min(liste_entrée, nomDeColonne):
  s = projection_simple(liste_entrée, nomDeColonne)
  """
  on stock la premiere valeur dans la variable min et avec une boucle on va passer
    sur toute les valeurs de la colonne et si y'a une valeur plus petite que min, on ecrase
    l'ancienne valeure de min par la nouvelle 
    """
  min = s[1]
  for elem in s:
    if isinstance(elem, str):
      print("veuillez selectionner une colonne avec des valeurs numerique")
      return None
    if min >= elem:
      min = elem
  return min


"""
- Fonction : max
- Parametre : une liste contenant les donnèes d'un fichier csv et l'en tête d'une colonne
- Retourne : la plus grande valeure de la colonne  
"""


def max(liste_entrée, nomDeColonne):
  s = projection_simple(liste_entrée, nomDeColonne)
  """
  on stock la premiere valeur dans la variable max et avec une boucle on va passer
    sur toute les valeurs de la colonne et si y'a une valeur plus grnade que max, on ecrase
    l'ancienne valeure de max par la nouvelle
    """
  max = s[1]
  for elem in range(1, len(s)):
    if isinstance(s[elem], str):
      print("veuillez selectionner une colonne avec des valeurs numerique")
      return None
    if max <= s[elem]:
      max = s[elem]
  return max


"""
- Fonction : compte
- Parametre : une liste contenant les donnèes d'un fichier csv et l'en tête d'une colonne
- Retourne : le nombre de valeur non nul d'une colonne  
"""


def compte(liste_entrée, nomDeColonne):
  s = projection_simple(liste_entrée, nomDeColonne)
  """
  à l'aide d'une boucle on passe par toutes les valeurs de la colonne
  et si la valeur est non nul on rajoute +1 au compteur
  """
  Compteur = 0
  for elem in range(1, len(s)):
    if isinstance(s[elem], str):
      print("veuillez selectionner une colonne avec des valeurs numerique")
      return None
    if s[elem] != 0:
      Compteur += 1
  return Compteur


"""
- Fonction : somme
- Parametre : une liste contenant les donnèes d'un fichier csv et l'en tête d'une colonne
- Retourne : la somme des valeures d'une colonne   
"""


def somme(liste_entrée, nomDeColonne):
  s = projection_simple(liste_entrée, nomDeColonne)
  """
  à l'aide d'une boucle on passe par toutes les valeurs de la colonne
  et on l'adissionne à la variable somme
  """
  Somme = 0
  for elem in range(1, len(s)):
    if isinstance(s[elem], str):
      print("veuillez selectionner une colonne avec des valeurs numerique")
      return None
    Somme += int(s[elem])
  return Somme


"""
- Fonction : moyenne
- Parametre : une liste contenant les donnèes d'un fichier csv et l'en tête d'une colonne
- Retourne : la moyenne des valeures d'une colonne   
"""


def moyenne(liste_entrée, nomDeColonne):
  s = projection_simple(liste_entrée, nomDeColonne)
  """ 
  on fait appel à la fonction somme pour calculer la somme des valeurs
  puis on la devise sur le nombre de valeur de la colonne
  """
  Moyenne = int(somme(liste_entrée, nomDeColonne)) / (len(s) - 1)
  return Moyenne


# Script 2 : Etape 7
def ordonne(liste_entrée, nomDeColonne, sens):
  entetes = liste_entrée[0]
  colonne = entetes.index(nomDeColonne)
  if sens == 'croissant':
    tri = sorted(liste_entrée[1:], key=lambda x: x[colonne])
  elif sens == 'decroissant':
    tri = sorted(liste_entrée[1:], key=lambda x: x[colonne], reverse=True)
  else:
    raise ValueError("L'ordre doit être 'croissant' ou 'decroissant'.")

  liste_trié = entetes + tri
  return liste_trié


def ordonne_multiple(liste_entrée, liste_nom_colonnes, sens):
  for nomDeColonne in liste_nom_colonnes:
    liste_trié = (ordonne(liste_entrée, nomDeColonne, sens))
  return liste_trié


# Script 2 : Etape 8
"""
def jointure(S1, S2 , nomDeColonne):
  
    S1_dict = [dict(colonne) for colonne in S1]
    S2_dict = [dict(colonne) for colonne in S2]
    
    result_dict = []
    for colonne1 in S1_dict:
        for colonne2 in S2_dict:
            if colonne1[nomDeColonne] == colonne2[nomDeColonne]:
                result_colonne = {}
                for clé in colonne1:
                    result_colonne[clé] = colonne1[clé]
                for clé in colonne2:
                    if clé != nomDeColonne:
                        result_colonne[clé] = colonne2[clé]
                result_dict.append(result_colonne)
    
  

"""
# ----------  Test des script / Fonction ----------

# ------ Test Script 1 : Etape 1 ------

# lecture_csv(data_csv)

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
"""
print("Projection Simple : ", projection_simple(s2, 'nomCommune'))
space_graph(2)
print("Projection Multiple : ", projection_multiple_v3(s2, ['nomCommune', 'codeInseeCommune']))
"""
"""
print("Projection Simple Distinct : \n", projection_simple_distinct(s2, 'nomCommune'))
space_graph(2)
print("Projection Multiple Distinct : \n", projection_multiple_distinct_v2(s2, ['codeInseeCommune', 'nomCommune']))
"""
"""
print("Projection Simple : ", projection_simple(s2_Si, 'copro'))
space_graph(2)
print("Projection Multiple : ", projection_multiple(s2_Si, ['nufact', 'copro']))
space_graph(2)
print("Projection Simple Distinct : ", projection_simple_distinct(s2_Si, 'copro'))
space_graph(2)
print("Projection Multiple Distinct : ", projection_multiple_distinct(s2_Si, ['copro', 'qte']))
"""
# ------ Test Script 2 : Etape 5 ------

#print(sélection_simple(s2_Si, 'qte', '>', 2))
print(sélection_simple(S3_bis, "nbParking", '>', 2))
#print(S3_bis)

# ------ Test Script 2 : Etape 6 ------

# ------ Test Script 2 : Etape 7 ------

#print(ordonne(S3_bis, "nbEquipements", 'decroissant'))

# ------ Test Script 2 : Etape 8 ------

# ------ Test Script 3 : Etape 9 ------

# ------ Test Script 4 : Etape 10 -----
