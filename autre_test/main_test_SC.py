import csv

"""# ------ chemin des fichier.csv  ------
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

# ------ Fonction --------

# ----- Fonction esthétique / grap -----


# fonction espace
def space_graph(valeur):
  for i in range(valeur):
    print("")


######    Lecutre fichier CSV    ######


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


lecture_csv(data_csv)

######    Ecriture fichier CSV    ######

# fonction écriture de fichier CSV avec en paramètre le nom du fichier.cvs et l'en tête
""" fonction écriture V1
def ecriture_csv(nom_fichier_csv, header):
    # Ouverutre d'un fichier csv en mode 'w" write = écriture et un saut de ligne
    with open(nom_fichier_csv, "w", newline="") as csv_file:
        # Écriture du fichier csv avec un paramètre un delimitation par le ";"
        writer = csv.writer(csv_file, delimiter=";")
        # Écriture de l'en tête du fichier csv
        writer.writerow(header)
        # Écriture du fichier.csv
        writer.writerow(["31", "Haute-Garonne"]) # test ecriture dans le fichier csv
"""
""" fonction écriture V2 """


def ecriture_csv(nom_fichier_csv, header, data):
  # Ouverutre d'un fichier csv en mode 'w" write = écriture et un saut de ligne
  with open(nom_fichier_csv, "w", newline="") as csv_file:
    # Écriture du fichier csv avec un paramètre un delimitation par le ";"
    writer = csv.writer(csv_file, delimiter=";")
    # Écriture de l'en tête du fichier csv
    writer.writerow(header)
    # Écriture du fichier.csv
    writer.writerow(data)  # test ecriture dans le fichier csv


# ----- Csv to Liste ------
"""  Csv to liste V1
def csv_en_liste(nom_fichier_csv, valeur_ligne, valeur_valeur):
    with open(nom_fichier_csv, errors="ignore") as f:
        lecture = csv.reader(f, delimiter=";")
        lignes = list(lecture)
    
    print(f"La ligne", valeur_ligne, "du fichier qui donne", lignes[0][valeur_valeur], ":", lignes[valeur_ligne][valeur_valeur])
    
    # ---- Test interne de la fonction ----
    #print(f"La ligne 0 du fichier: {lignes[0]}.")
    #print(f"La ligne 1 du fichier: {lignes[1]}.")
    #print(f"Le nombre de lignes du fichier: {len(lignes)}.")
"""


def csv_en_liste_v2(nom_fichier_csv, valeur_ligne, valeur_valeur):
  with open(nom_fichier_csv, errors="ignore") as f:
    lecture = csv.reader(f, delimiter=";")
    lignes = list(lecture)

  return lignes[valeur_ligne][valeur_valeur]


# ------ Appel de fonction -----
""" En-tête V1
header_installations_uniques_csv =["codeInstallation", "nomInstallation", "nbEquipements", "adresse", "nbParking", "nbParkingHandi"]
ecriture_csv(data_installations_uniques_csv, header_installations_uniques_csv)

header_communes_uniques_csv = ["codeInseeCommune", "nomCommune", "codeDepartement", "nomDepartement"]
ecriture_csv(data_communes_uniques_csv, header_communes_uniques_csv)

header_admissions_par_formation_detaillee_csv = ["codeInstallation", "codeInseeCommune", "libelle", "metro", "bus", "tram", "train", "bateau", "autreTransport", "aucunTransport", "dateMAJ", "dateCreation"]
ecriture_csv(data_admissions_par_formation_detaillee_csv, header_admissions_par_formation_detaillee_csv)
"""
""" En-tête V2
header_installations_uniques_csv_v2 = [(csv_en_liste_v2(data_csv, 0, 4)), (csv_en_liste_v2(data_csv, 0, 5)), (csv_en_liste_v2(data_csv, 0, 28)), (csv_en_liste_v2(data_csv, 0, 6)), (csv_en_liste_v2(data_csv, 0, 16)), (csv_en_liste_v2(data_csv, 0, 17))]

header_communes_uniques_csv_v2 = [(csv_en_liste_v2(data_csv, 0, 2)), (csv_en_liste_v2(data_csv, 0, 3)),  (csv_en_liste_v2(data_csv, 0, 0)), (csv_en_liste_v2(data_csv, 0, 1))]

header_admissions_par_formation_detaillee_csv_v2 = [(csv_en_liste_v2(data_csv, 0, 4)), (csv_en_liste_v2(data_csv, 0, 2)), (csv_en_liste_v2(data_csv, 0, 9)), (csv_en_liste_v2(data_csv, 0, 19)), (csv_en_liste_v2(data_csv, 0, 20)), (csv_en_liste_v2(data_csv, 0, 21)), (csv_en_liste_v2(data_csv, 0, 22)), (csv_en_liste_v2(data_csv, 0, 23)), (csv_en_liste_v2(data_csv, 0, 24)), (csv_en_liste_v2(data_csv, 0, 25)), (csv_en_liste_v2(data_csv, 0, 26)), (csv_en_liste_v2(data_csv, 0, 27))]
"""
""" En-tête V2.2"""
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

header_communes_uniques_csv_v2_2 = [(csv_en_liste_v2(data_csv, 0,
                                                     codeInseeCommune)),
                                    (csv_en_liste_v2(data_csv, 0, nomCommune)),
                                    (csv_en_liste_v2(data_csv, 0,
                                                     codeDepartement)),
                                    (csv_en_liste_v2(data_csv, 0,
                                                     nomDepartement))]

header_installations_uniques_csv_v2_2 = [
  (csv_en_liste_v2(data_csv, 0, codeInstallation)),
  (csv_en_liste_v2(data_csv, 0, nomInstallation)),
  (csv_en_liste_v2(data_csv, 0, nbEquipements)),
  (csv_en_liste_v2(data_csv, 0, adresse)),
  (csv_en_liste_v2(data_csv, 0, nbParking)),
  (csv_en_liste_v2(data_csv, 0, nbParkingHandi))
]
""" Data V2
data_installations_uniques_csv_v2 = [(csv_en_liste_v2(data_csv, 1, 4)), (csv_en_liste_v2(data_csv, 1, 5)), (csv_en_liste_v2(data_csv, 1, 28)), (csv_en_liste_v2(data_csv, 1, 6)), (csv_en_liste_v2(data_csv, 1, 16)), (csv_en_liste_v2(data_csv, 1, 17))]

data_communes_uniques_csv_v2 = [(csv_en_liste_v2(data_csv, 1, 2)), (csv_en_liste_v2(data_csv, 1, 3)),  (csv_en_liste_v2(data_csv, 1, 0)), (csv_en_liste_v2(data_csv, 1, 1))]

data_admissions_par_formation_detaillee_csv_v2 = [(csv_en_liste_v2(data_csv, 1, 4)), (csv_en_liste_v2(data_csv, 1, 2)), (csv_en_liste_v2(data_csv, 1, 9)), (csv_en_liste_v2(data_csv, 1, 19)), (csv_en_liste_v2(data_csv, 1, 20)), (csv_en_liste_v2(data_csv, 1, 21)), (csv_en_liste_v2(data_csv, 1, 22)), (csv_en_liste_v2(data_csv, 1, 23)), (csv_en_liste_v2(data_csv, 1, 24)), (csv_en_liste_v2(data_csv, 1, 25)), (csv_en_liste_v2(data_csv, 1, 26)), (csv_en_liste_v2(data_csv, 1, 27))]
"""
""" Data V2.2"""
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

# ------   Test des nouveau fichier csv cree  -----

# -----  test écriture puis lecture  ------
""" Test écriture/lecutre v1
lecture_csv(data_installations_uniques_csv)
print("")
lecture_csv(data_communes_uniques_csv)
print("")
lecture_csv(data_admissions_par_formation_detaillee_csv)
"""
""" test écriture/lecutre v2

ecriture_csv(data_installations_uniques_csv, header_installations_uniques_csv_v2, data_installations_uniques_csv_v2)
lecture_csv(data_installations_uniques_csv)
space_graph(2)

ecriture_csv(data_communes_uniques_csv, header_communes_uniques_csv_v2, data_communes_uniques_csv_v2)
lecture_csv(data_communes_uniques_csv)
space_graph(2)

ecriture_csv(data_admissions_par_formation_detaillee_csv, header_admissions_par_formation_detaillee_csv_v2, data_admissions_par_formation_detaillee_csv_v2)
lecture_csv(data_admissions_par_formation_detaillee_csv)
space_graph(4)
"""
""" test écriture/lecutre v2.2 """

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

#### test csv en liste ###
""" test csv to liste v1 
ligne = 2 # ligne 0 = en-tête 
valeur = 3 # valeur = A sur le execel 
csv_en_liste(data_csv, ligne, valeur)
"""
""" test csv to liste V2"""
ligne = 1  # ligne 0 = en-tête
valeur = 0  # valeur = A sur le execel
print("la valeur de la colone", valeur, "est:",
      csv_en_liste_v2(data_csv, 0, valeur))
print("la valeur de la ligne", ligne, "est :",
      csv_en_liste_v2(data_csv, ligne, valeur))
print("la valeur de", csv_en_liste_v2(data_csv, 0, valeur), "est :",
      csv_en_liste_v2(data_csv, ligne, valeur))
space_graph(1)

######    Lecture / Ecriture / csv->liste : ok  avec version  ######""""