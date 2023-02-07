from fonctions.dictionnaire import *
from fonctions.manique import *
from fonctions.fonction import *



#  ----- chemin des fichier.csv  ------

data_csv = "2020_installations_sportives.csv"  # fichier orginal (sujet)

# Fichier constituer du code de l'installation, nom de l'installation, nombre d'Equipement, de l'adresse et du nombre de place de parking handicaper ou pas.
installations_uniques_csv = "data/IntallationsUniques.csv"

# Fichier constituer du code INSEE de la commune, du nom de la commune, du code du department et du nom du département.
communes_uniques_csv = "data/CommunesUniques.csv"

# Fichier constituer du code de l'installation, du code INSEE de la commune, du libelle, des different moyen de transport(Metro,Bus,Tram,Train,Bateau ou autre voir pas) et des la date de mise à jour et de création
admissions_par_formation_detaillee_csv = "data/AdmissionParFormationDetaillee.csv"