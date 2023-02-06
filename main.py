import csv

 ------ chemin des fichier.csv  ------
data_csv = "2020_installations_sportives.csv"  # fichier orginal (sujet)

# Fichier constituer du code de l'installation, nom de l'installation, nombre d'Equipement, de l'adresse et du nombre de place de parking handicaper ou pas.
data_installations_uniques_csv = "data/IntallationsUniques.csv"

# Fichier constituer du code INSEE de la commune, du nom de la commune, du code du department et du nom du département.
data_communes_uniques_csv = "data/CommunesUniques.csv"

# Fichier constituer du code de l'installation, du code INSEE de la commune, du libelle, des different moyen de transport(Metro,Bus,Tram,Train,Bateau ou autre voir pas) et des la date de mise à jour et de création
data_admissions_par_formation_detaillee_csv = "data/AdmissionParFormationDetaillee.csv"

#  ------ Diconnaire de recherche ------

dico = {
  "a": 0,
  "b": 1,
  "c": 2,
  "d": 3,
  "e": 4,
  "f": 5,
  "g": 6,
  "h": 7,
  "i": 8,
  "j": 9,
  "k": 10,
  "l": 11,
  "m": 12,
  "n": 13,
  "o": 14,
  "p": 15,
  "q": 16,
  "r": 17,
  "s": 18,
  "t": 19,
  "u": 20,
  "v": 21,
  "w": 22,
  "x": 23,
  "y": 24,
  "z": 25,
  "aa": 26,
  "ab": 27,
  "ac": 28
}

# ---- requete de recherche dans le dico ----

codeDepartement = dico.get("a")
nomDepartement = dico.get("b")
codeInseeCommune = dico.get("c")
nomCommune = dico.get("d")
codeInstallation = dico.get("e")
nomInstallation = dico.get("f")
adresse = dico.get("g")
codePostal = dico.get("h")
arrondissement = dico.get("i")
libelle = dico.get("j")
multiCommune = dico.get("k")
accessibilite = dico.get("l")
accessibiliteHandiMoteur = dico.get("m")
accessibiliteHandiSens = dico.get("n")
internat = dico.get("o")
nbLits = dico.get("p")
nbParking = dico.get("q")
nbParkingHandi = dico.get("r")
gardien = dico.get("s")
metro = dico.get("t")
bus = dico.get("u")
tram = dico.get("v")
train = dico.get("w")
bateau = dico.get("x")
autreTransport = dico.get("y")
aucunTransport = dico.get("z")
dateMAJ = dico.get("aa")
dateCreation = dico.get("ab")
nbEquipements = dico.get("ac")

# ------ Fonction -------

# ----- Fonction esthétique / grap -----


# fonction espace
def space_graph(valeur):
  for i in range(valeur):
    print("")

"""
# ------ Fonction Lecture du fichier.csv ------


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


# ------   Fontion Écriture du fichier.csv   -------

# fonction écriture de fichier CSV avec en paramètre le nom du fichier.cvs et l'en tête


def ecriture_csv(nom_fichier_csv, header, data):
  # Ouverutre d'un fichier csv en mode 'w" write = écriture et un saut de ligne
  with open(nom_fichier_csv, "w", newline="") as csv_file:
    # Écriture du fichier csv avec un paramètre un delimitation par le ";"
    writer = csv.writer(csv_file, delimiter=";")
    # Écriture de l'en tête du fichier csv
    writer.writerow(header)
    # Écriture du fichier.csv
    writer.writerow(data)  # test ecriture dans le fichier csv


# ----   fichier.csv en liste  --------


def csv_en_liste_v2(nom_fichier_csv, valeur_ligne, valeur_valeur):
  with open(nom_fichier_csv, errors="ignore") as f:
    lecture = csv.reader(f, delimiter=";")
    lignes = list(lecture)

  return lignes[valeur_ligne][valeur_valeur]


# -----  Test des Fontion et Affichage ----

# Test de la fonction lecutre_csv
lecture_csv(data_csv)
space_graph(4)

######   Test des nouveau fichier csv cree   #####

#Position des en-tête codeInstallation = 4, nomInstallation = 5, nbEquipements = 28, adresse = 6, nbParking = 16, nbParkingHandi = 17

# --- En-tête ---
header_admissions_par_formation_detaillee_csv_v2_2 = [
  (csv_en_liste_v2(data_csv, 0, codeInstallation)),
  (csv_en_liste_v2(data_csv, 0,
                   codeInseeCommune)), (csv_en_liste_v2(data_csv, 0, libelle)),
  (csv_en_liste_v2(data_csv, 0, metro)), (csv_en_liste_v2(data_csv, 0, bus)),
  (csv_en_liste_v2(data_csv, 0, tram)), (csv_en_liste_v2(data_csv, 0, train)),
  (csv_en_liste_v2(data_csv, 0, bateau)),
  (csv_en_liste_v2(data_csv, 0, autreTransport)),
  (csv_en_liste_v2(data_csv, 0, aucunTransport)),
  (csv_en_liste_v2(data_csv, 0, dateMAJ)),
  (csv_en_liste_v2(data_csv, 0, dateCreation))
]

header_communes_uniques_csv_v2_2 = [(csv_en_liste_v2(data_csv, 0, codeInseeCommune)),(csv_en_liste_v2(data_csv, 0, nomCommune)), (csv_en_liste_v2(data_csv, 0, codeDepartement)), (csv_en_liste_v2(data_csv, 0, nomDepartement))]

header_installations_uniques_csv_v2_2 = [
  (csv_en_liste_v2(data_csv, 0, codeInstallation)),
  (csv_en_liste_v2(data_csv, 0, nomInstallation)),
  (csv_en_liste_v2(data_csv, 0, nbEquipements)),
  (csv_en_liste_v2(data_csv, 0, adresse)),
  (csv_en_liste_v2(data_csv, 0, nbParking)),
  (csv_en_liste_v2(data_csv, 0, nbParkingHandi))
]

# ---- Data ----
data_admissions_par_formation_detaillee_csv_v2_2 = [
  (csv_en_liste_v2(data_csv, 1, codeInstallation)),
  (csv_en_liste_v2(data_csv, 1,
                   codeInseeCommune)), (csv_en_liste_v2(data_csv, 1, libelle)),
  (csv_en_liste_v2(data_csv, 1, metro)), (csv_en_liste_v2(data_csv, 1, bus)),
  (csv_en_liste_v2(data_csv, 1, tram)), (csv_en_liste_v2(data_csv, 1, train)),
  (csv_en_liste_v2(data_csv, 1, bateau)),
  (csv_en_liste_v2(data_csv, 1, autreTransport)),
  (csv_en_liste_v2(data_csv, 1, aucunTransport)),
  (csv_en_liste_v2(data_csv, 1, dateMAJ)),
  (csv_en_liste_v2(data_csv, 1, dateCreation))
]

data_communes_uniques_csv_v2_2 = [(csv_en_liste_v2(data_csv, 1,
                                                   codeInseeCommune)),
                                  (csv_en_liste_v2(data_csv, 1, nomCommune)),
                                  (csv_en_liste_v2(data_csv, 1,
                                                   codeDepartement)),
                                  (csv_en_liste_v2(data_csv, 1,
                                                   nomDepartement))]

data_installations_uniques_csv_v2_2 = [
  (csv_en_liste_v2(data_csv, 1, codeInstallation)),
  (csv_en_liste_v2(data_csv, 1, nomInstallation)),
  (csv_en_liste_v2(data_csv, 1, nbEquipements)),
  (csv_en_liste_v2(data_csv, 1, adresse)),
  (csv_en_liste_v2(data_csv, 1, nbParking)),
  (csv_en_liste_v2(data_csv, 1, nbParkingHandi))
]

# -----  test écriture puis lecture  ------

ecriture_csv(data_installations_uniques_csv,
             header_installations_uniques_csv_v2_2,
             data_installations_uniques_csv_v2_2)
lecture_csv(data_installations_uniques_csv)
space_graph(2)

ecriture_csv(data_communes_uniques_csv, header_communes_uniques_csv_v2_2,
             data_communes_uniques_csv_v2_2)
lecture_csv(data_communes_uniques_csv)
space_graph(2)

ecriture_csv(data_admissions_par_formation_detaillee_csv,
             header_admissions_par_formation_detaillee_csv_v2_2,
             data_admissions_par_formation_detaillee_csv_v2_2)
lecture_csv(data_admissions_par_formation_detaillee_csv)
space_graph(4)

# ----  Test de la fonction fichier.csv en liste ----

ligne = 1  # ligne 0 = en-tête
valeur = 0  # valeur = A sur le execel
print("la valeur de la colone", valeur, "est:",
      csv_en_liste_v2(data_csv, 0, valeur))
print("la valeur de la ligne", ligne, "est :",
      csv_en_liste_v2(data_csv, ligne, valeur))
print("la valeur de", csv_en_liste_v2(data_csv, 0, valeur), "est :",
      csv_en_liste_v2(data_csv, ligne, valeur))
space_graph(1)
"""


simple_csv = "2020_installations_sportives.csv"

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
            
lire_et_ecrire_csv(simple_csv, "Installations_uniques.csv",[4, 5, 6, 16, 17, 28])
lire_et_ecrire_csv(simple_csv, "Communes_uniques.csv",[0, 1, 2, 3 ])
lire_et_ecrire_csv(simple_csv, "Admissions_par_formation_détaillée.csv",[2, 4, 9, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27 ])