import csv
from fonctions.module import *

# ------ Fonction test en cours  -------
"""
def projection_simple(Si,nomDeColonne) :
  for ligne in Si:
      for colonne in Si[ligne] :
        if Si[ligne][colonne] == nomDeColonne :        
  

#projection_simple(changement_de_données(installations_uniques_csv, "S1"), nomInstallation)


def projection_multiple(Si,nomdecol):
nomdecol=[]
  for ligne in Si:
    for colonne in Si:
      if nomDeColonne == nomdecol
  return nomdecol

def projection_simple_distinct(Si, nomDeColonne):
  print("en cours")
  
  return Si
"""


# --------------   Test ecriture -------


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

# ------ Test Lecture  -------------

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
space_graph(4)
print("Chargement des fichiers csv terminer")


#changement_de_données(installations_uniques_csv, S1))

