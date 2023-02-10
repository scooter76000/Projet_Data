import csv
from dictionnaire import *

#  ----- chemin des fichier.csv  ------

data_csv = "2020_installations_sportives.csv"  # fichier orginal (sujet)

# Fichier constitué du code de l'installation, nom de l'installation, nombre d'Equipement, de l'adresse et du nombre de place de parking handicaper ou pas.
installations_uniques_csv = "data/IntallationsUniques.csv"

# Fichier constituer du code INSEE de la commune, du nom de la commune, du code du department et du nom du département.
communes_uniques_csv = "data/CommunesUniques.csv"

# Fichier constituer du code de l'installation, du code INSEE de la commune, du libelle, des different moyen de transport(Metro,Bus,Tram,Train,Bateau ou autre voir pas) et des la date de mise à jour et de création
admissions_par_formation_detaillee_csv = "data/AdmissionParFormationDetaillee.csv"

# ----- Fonction esthétique / grap -----
# fonction espace
def space_graph(valeur):
  for i in range(valeur):
    print("")

# fonction chargment
import time
def chargment(valeur, temps):
  print(valeur)
  time.sleep(temps)

# ----  Fonction fonctionnelle ----- 

"""
# Fonction : exemple de fonction
# parametre : nom_fichier_csv, str
# retourne : S
"""


# Script 1 : Etape 1


# fonction lecture de fichier CSV avec en paramètres le nom du fichier.csv
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
fonction lecture et ecriture de fichier CSV qui prend en paramètre le nom du fichier en entrée et celui en sortie une liste d'Index des colonnes qu'on veut recuperer
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
        ici la fonction crée un nouveau fichier avec le nom en paramètre et avec une double boucle une qui récuperer les ligne et l'autre les colonnes la fonction recupére les données de la liste et les ecrit dans le nouveau fichier csv
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
Fonction qui recupére les données d'un fichier csv et les stocks dans une liste avec en paramètre le nom du fichier et le nom de la liste qu'on veut creer
"""
def chargement_de_données (nom_fichier_entree) :
    S = []
    with open(nom_fichier_entree, 'r', encoding="ISO-8859-1") as fichier_entree:
        reader = csv.reader(fichier_entree, delimiter=';')
        for ligne in reader:
            S.append(ligne)
        return S

      
# Script 2 : Etape 4

def projection_simple (liste_entrée, nomDeColonne) :
  S = []
  for ligne in range(len(liste_entrée)) :
    for colonne in range (len(liste_entrée[ligne])) :
      if liste_entrée[ligne][colonne] == nomDeColonne :
        index_colonne = colonne
    S.append(liste_entrée[ligne][index_colonne])      
  print (S)
  return(S)


def projection_simple_distinct(liste_entrée, nomDeColonne) :
  S = []
  for ligne in range(len(liste_entrée)) :
    for colonne in range (len(liste_entrée[ligne])) :
      if liste_entrée[ligne][colonne] == nomDeColonne :
        index_colonne = colonne
    if liste_entrée[ligne][index_colonne] not in S :
      S.append(liste_entrée[ligne][index_colonne])      
  print (S)
  return(S)  
  

def projection_multiple(liste_entrée,liste_nom_colonnes):
  S=[[0]*len(liste_nom_colonnes)]*len(liste_entrée)
  for i in range(len(liste_nom_colonnes)):
    liste=projection_simple(liste_entrée, liste_nom_colonnes[i])
    for j in range(len(liste)):
      S[j][i]=liste[j]
  print (S)


def projection_multiple_distinct(liste_entrée,liste_nom_colonnes):
  S=[[0]*len(liste_nom_colonnes)]*len(liste_entrée)
  for i in range(len(liste_nom_colonnes)):
    liste=projection_simple_distinct(liste_entrée, liste_nom_colonnes[i])
    for j in range(len(liste)):
      S[j][i]=liste[j]
  print (S)


    
S1=chargement_de_données(installations_uniques_csv)
S2=chargement_de_données(communes_uniques_csv)
S3=chargement_de_données(admissions_par_formation_detaillee_csv)


#Script 2 : Etape 5


def sélection_simple(liste_entrée, nomDeColonne, opérateur, valeur):
  S = []
  ...
  return S


def sélection_multiple (liste_entrée, operateurbooléen):
  S = []
  ...
  return S


#Script 2 : Etape 6


def min (liste_entrée, nomDeColonne) :
  S = []
  for ligne in range(len(liste_entrée)) :
    for colonne in range (len(liste_entrée[ligne])) :
      if liste_entrée[ligne][colonne] == nomDeColonne :
        index_colonne = colonne
    S.append(liste_entrée[ligne][index_colonne]) 
  min = S[1] 
  for elem in S :
    if min >= elem :
      min = elem 
  return min


def max (liste_entrée, nomDeColonne) :
  S = []
  for ligne in range(len(liste_entrée)) :
    for colonne in range (len(liste_entrée[ligne])) :
      if liste_entrée[ligne][colonne] == nomDeColonne :
        index_colonne = colonne
    S.append(liste_entrée[ligne][index_colonne]) 
  max = S[1]
  for elem in range(1, len(S)):
    if max <= S[elem] :
      max = S[elem]
  return max


def compte (liste_entrée, nomDeColonne) :
  S = []
  for ligne in range(len(liste_entrée)) :
    for colonne in range (len(liste_entrée[ligne])) :
      if liste_entrée[ligne][colonne] == nomDeColonne :
        index_colonne = colonne
    S.append(liste_entrée[ligne][index_colonne]) 
  Compteur = 0
  for elem in range(1, len(S)-1):
    if S[elem] != 0 :
      Compteur += 1
  return Compteur


def somme (liste_entrée, nomDeColonne) :
  S = []
  for ligne in range(len(liste_entrée)) :
    for colonne in range (len(liste_entrée[ligne])) :
      if liste_entrée[ligne][colonne] == nomDeColonne :
        index_colonne = colonne
    S.append(liste_entrée[ligne][index_colonne]) 
  Somme = 0
  for elem in range(1, len(S)):
    Somme += int(S[elem])
  return Somme


def moyenne (liste_entrée, nomDeColonne) :
  S = []
  for ligne in range(len(liste_entrée)) :
    for colonne in range (len(liste_entrée[ligne])) :
      if liste_entrée[ligne][colonne] == nomDeColonne :
        index_colonne = colonne
    S.append(liste_entrée[ligne][index_colonne]) 
  Somme = 0
  for elem in range(1, len(S)):
    Somme += int(S[elem])
  Moyenne = Somme/(len(S)-1)
  return Moyenne

  
#Script 2 : Etape 7

def ordonne(liste_entrée, nomDeColonne, sens):
  S = []
  ...
  return S


def ordonne_multiple(liste_entrée, liste_nom_colonnes, sens):
  S = []
  ...
  return S


#Script 2 : Etape 8 

def jointure(liste_entrée, liste_sortie, nomDeColonne):
  S = []
  ...
  return S
  
  
# --------------   Test ecriture -------

"""
#Position des en-tête codeInstallation = 4, nomInstallation = 5, nbEquipements = 28, adresse = 6, nbParking = 16, nbParkingHandi = 17
lire_et_ecrire_csv(data_csv, installations_uniques_csv, [
  codeInstallation, nomInstallation, nbEquipements, adresse, nbParking,
  nbParkingHandi
], 444)

#Position des en-tête codeInseeCommune = 2, nomComune = 3, codeDepartement = 0, nomDepartement = 1
lire_et_ecrire_csv(data_csv, communes_uniques_csv, [codeInseeCommune, nomCommune, codeDepartement, nomDepartement], 146)
#Position des en-tête codeInstallation = 4, codeInseeCommune = 2, libelle = 9, metro = 19, bus = 20, tram = 21,train = 22, bateau = 23, autreTransport = 24, aucunTransport = 25, dateMAJ = 26, dateCreation = 27
lire_et_ecrire_csv(data_csv, admissions_par_formation_detaillee_csv, [
  codeInstallation, codeInseeCommune, libelle, metro, bus, tram, train, bateau,
  autreTransport, aucunTransport, dateMAJ, dateCreation
], 444)
"""

# ------ Test Lecture -------------

"""
chargment("Chargement de fichier csv Admission", 2)
lecture_csv(admissions_par_formation_detaillee_csv)
space_graph(4)

time.sleep(2)
chargment("Chargement de fichier csv Communes", 4)
lecture_csv(communes_uniques_csv)
space_graph(4)

time.sleep(2)
chargment("Chargement de fichier csv Installations", 4)
lecture_csv(installations_uniques_csv)
space_graph(2)
print("Chargement des fichiers csv terminer")
space_graph(4)
"""

# --------------   Test changmenent des données -------

#changement_de_données(installations_uniques_csv, S1))

