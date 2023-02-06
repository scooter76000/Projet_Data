import csv
from fonctions.dictionnaire import *

#  ----- chemin des fichier.csv  ------ 

data_csv = "2020_installations_sportives.csv"  # fichier orginal (sujet)

# Fichier constituer du code de l'installation, nom de l'installation, nombre d'Equipement, de l'adresse et du nombre de place de parking handicaper ou pas.
installations_uniques_csv = "data/IntallationsUniques.csv"

# Fichier constituer du code INSEE de la commune, du nom de la commune, du code du department et du nom du département.
communes_uniques_csv = "data/CommunesUniques.csv"

# Fichier constituer du code de l'installation, du code INSEE de la commune, du libelle, des different moyen de transport(Metro,Bus,Tram,Train,Bateau ou autre voir pas) et des la date de mise à jour et de création
admissions_par_formation_detaillee_csv = "data/AdmissionParFormationDetaillee.csv"


# ------ Fonction -------
# ----- Fonction esthétique / grap -----

# fonction espace
def space_graph(valeur):
  for i in range(valeur):
    print("")


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



#fonction ecriture de fichier CSV 
def lire_et_ecrire_csv(nom_fichier_entree, nom_fichier_sortie, colonnes_a_recuperer):
    donnees = []
    with open(nom_fichier_entree, 'r', encoding = "ISO-8859-1") as fichier_entree:
        reader = csv.reader(fichier_entree, delimiter = ';')
        for ligne in reader:
            donnees.append(ligne)

    with open(nom_fichier_sortie, 'w', newline='') as fichier_sortie:
        writer = csv.writer(fichier_sortie)
        for ligne in donnees:
            colonnes_selectionnees = [ligne[colonne] for colonne in colonnes_a_recuperer]
            writer.writerow(colonnes_selectionnees)
          
            
#Position des en-tête codeInstallation = 4, nomInstallation = 5, nbEquipements = 28, adresse = 6, nbParking = 16, nbParkingHandi = 17


# --------------   Test ecriture -------   
          
lire_et_ecrire_csv(data_csv, installations_uniques_csv, [codeInstallation, nomInstallation, nbEquipements, adresse, nbParking, nbParkingHandi])
#Position des en-tête codeInseeCommune = 2, nomComune = 3, codeDepartement = 0, nomDepartement = 1
lire_et_ecrire_csv(data_csv, communes_uniques_csv, [codeInseeCommune, nomCommune, codeDepartement, nomDepartement])
#Position des en-tête codeInstallation = 4, codeInseeCommune = 2, libelle = 9, metro = 19, bus = 20, tram = 21,train = 22, bateau = 23, autreTransport = 24, aucunTransport = 25, dateMAJ = 26, dateCreation = 27
lire_et_ecrire_csv(data_csv, admissions_par_formation_detaillee_csv, [codeInstallation, codeInseeCommune, libelle, metro, bus, tram, train, bateau, autreTransport, aucunTransport, dateMAJ, dateCreation])


# ------ Test Lecture  -------------
"""
lecture_csv(admissions_par_formation_detaillee_csv)
space_graph(4)
lecture_csv(communes_uniques_csv)
space_graph(4)
lecture_csv(installations_uniques_csv)
"""