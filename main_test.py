import csv


""" ------------------ V1 ---------------- """


"""data_csv = "/home/runner/Projet-Data-Groupe-G/fichier1.csv" #chemin fichier selon le pwd


pwd est un commande linux/Unix pour avoir le nom complet de l'arborescence d'un fichier


with open(data_csv, errors="ignore") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)
"""

"""
simple_csv = "fichier1.csv"
#def fichier_1 ():
fichier_sortie1 = "installations_uniques.csv"
colonnes = ["codeInstallation","nomInstallation","adresse","nbParking","nbParkingHand","nbEquipements"]
with open (simple_csv, 'r') as csv_file :
    reader = csv.DictReader(csv_file)
    headers = reader.fieldnames 
    if not all(col in headers for col in colonnes):
        raise Exception("Les colonnes spécifiées ne sont pas toutes présentes dans le fichier d'entrée")
    with open (fichier_sortie1, 'w') as csv_sortie : 
        writer = csv.DictWriter(csv_sortie)
        writer.writeheader()
        for row in reader:
            data = {col: row[col] for col in colonnes}
            writer.writerow(data)
"""
"""
simple_csv = "fichier1.csv"


def creation_fichier(fichier_entre, nom_fichier, colonnes):
    liste_fichier = []
    with open(fichier_entre, 'r', errors="ignore", newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
        for ligne in reader:
            liste_fichier.append(', '.join(ligne))
    fich_sortie = nom_fichier
    with open(fich_sortie, 'w', newline='') as csv_sortie:
        writer = csv.writer(csv_sortie)
        writer.writerow([liste_fichier[i][j] for j in colonnes] for i in range(len(liste_fichier)))


creation_fichier(simple_csv, [2], "installations_uniques.csv")

"""
"""
######    Lecture / Ecriture : ok    ###### début 

data_csv = "/home/runner/Projet-Data-Groupe-G/fichier1.csv" #chemin fichier selon le pwd

# pwd est un commande linux/Unix pour avoir le nom complet de l'arborescence d'un fichier


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

# Fichier constituer du code de l'installation, nom de l'installation, nombre d'Equipement, de l'adresse et du nombre de place de parking handicaper ou pas.
data_installations_uniques_csv = "/home/runner/Projet-Data-Groupe-G/data/IntallationsUniques.csv"

#Fichier constituer du code INSEE de la commune, du nom de la commune, du code du department et du nom du département.
data_communes_uniques_csv = "/home/runner/Projet-Data-Groupe-G/data/CommunesUniques.csv"

# Fichier constituer du code de l'installation, du code INSEE de la commune, du libelle, des different moyen de transport(Metro,Bus,Tram,Train,Bateau ou autre voir pas) et des la date de mise à jour et de création
data_admissions_par_formation_detaillee_csv = "/home/runner/Projet-Data-Groupe-G/data/AdmissionParFormationDetaillee.csv"


# fonction écriture de fichier CSV avec en paramètre le nom du fichier.cvs et l'en tête
def ecriture_csv(nom_fichier_csv, header):
    # Ouverutre d'un fichier csv en mode 'w" write = écriture et un saut de ligne
    with open(nom_fichier_csv, "w", newline="") as csv_file:
        # Écriture du fichier csv avec un paramètre un delimitation par le ";"
        writer = csv.writer(csv_file, delimiter=";")
        # Écriture de l'en tête du fichier csv
        writer.writerow(header)
        # Écriture du fichier.csv
        writer.writerow(["31", "Haute-Garonne"]) # test ecriture dans le fichier csv

header_installations_uniques_csv =["codeInstallation", "nomInstallation", "nbEquipements", "adresse", "nbParking", "nbParkingHandi"]
ecriture_csv(data_installations_uniques_csv, header_installations_uniques_csv)

header_communes_uniques_csv = ["codeInseeCommune", "nomCommune", "codeDepartement", "nomDepartement"]
ecriture_csv(data_communes_uniques_csv, header_communes_uniques_csv)

header_admissions_par_formation_detaillee_csv = ["codeInstallation", "codeInseeCommune", "libelle", "metro", "bus", "tram", "train", "bateau", "autreTransport", "aucunTransport", "dateMAJ", "dateCreation"]
ecriture_csv(data_admissions_par_formation_detaillee_csv, header_admissions_par_formation_detaillee_csv)

######   Test des nouveau fichier csv cree   #####

lecture_csv(data_installations_uniques_csv)
print("")
lecture_csv(data_communes_uniques_csv)
print("")
lecture_csv(data_admissions_par_formation_detaillee_csv)


##### csv to liste  ####
def csv_en_liste(nom_fichier_csv, valeur_ligne, valeur_valeur):
    with open(nom_fichier_csv, errors="ignore") as f:
        lecture = csv.reader(f, delimiter=";")
        lignes = list(lecture)

    print(f"La ligne", valeur_ligne, "du fichier qui donne", lignes[0][valeur_valeur], ":", lignes[valeur_ligne][valeur_valeur])

    # ---- Test interne de la fonction ----
    #print(f"La ligne 0 du fichier: {lignes[0]}.")
    #print(f"La ligne 1 du fichier: {lignes[1]}.")
    #print(f"Le nombre de lignes du fichier: {len(lignes)}.")

#### test csv en liste ###
ligne = 2 # ligne 0 = en-tête 
valeur = 3 # valeur = A sur le execel 
csv_en_liste(data_csv, ligne, valeur)

######    Lecture / Ecriture / csv->liste : ok    ######

"""
"""
simple_csv = "2020_installations_sportives.csv"

def lire_et_ecrire_csv(nom_fichier_entree, nom_fichier_sortie, colonnes_a_recuperer):
    donnees = []
    with open(nom_fichier_entree, 'r', errors="ignore") as fichier_entree:
        reader = csv.reader(fichier_entree)
        for ligne in reader:
            donnees.append(ligne)

    with open(nom_fichier_sortie, 'w', newline='') as fichier_sortie:
        writer = csv.writer(fichier_sortie)
        for ligne in donnees:
            colonnes_selectionnees = [ligne[colonne] for colonne in colonnes_a_recuperer]
            writer.writerow(colonnes_selectionnees)


lire_et_ecrire_csv(simple_csv, "installations_uniques.csv", [1])

"""




""" ---------------  V2 --------------------- """

# ------ chemin des fichier.csv  ------
data_csv = "2020_installations_sportives.csv"  # fichier orginal (sujet)

# Fichier constituer du code de l'installation, nom de l'installation, nombre d'Equipement, de l'adresse et du nombre de place de parking handicaper ou pas.
installations_uniques_csv = "data/IntallationsUniques.csv"

# Fichier constituer du code INSEE de la commune, du nom de la commune, du code du department et du nom du département.
communes_uniques_csv = "data/CommunesUniques.csv"

# Fichier constituer du code de l'installation, du code INSEE de la commune, du libelle, des different moyen de transport(Metro,Bus,Tram,Train,Bateau ou autre voir pas) et des la date de mise à jour et de création
admissions_par_formation_detaillee_csv = "data/AdmissionParFormationDetaillee.csv"

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


"""
simple_csv = "2020_installations_sportives.csv"


def lire_et_ecrire_csv(nom_fichier_entree, nom_fichier_sortie, colonnes_a_recuperer):
    donnees = []
    with open(nom_fichier_entree, encoding="ISO-8859-1") as fichier_entree: 
        reader = csv.reader(fichier_entree, delimiter=';')
        for ligne in reader:
            donnees.append(ligne)

    with open(nom_fichier_sortie, 'w', newline='') as fichier_sortie:
        writer = csv.writer(fichier_sortie)
        for ligne in donnees:
            colonnes_selectionnees = [ligne[colonne] for colonne in colonnes_a_recuperer]
            writer.writerow(colonnes_selectionnees)

#Position des en-tête codeInstallation = 4, nomInstallation = 5, nbEquipements = 28, adresse = 6, nbParking = 16, nbParkingHandi = 17
lire_et_ecrire_csv(simple_csv, "Installations_uniques.csv", [4, 5, 6, 16, 17, 28])
#Position des en-tête codeInseeCommune = 2, nomComune = 3, codeDepartement = 0, nomDepartement = 1
lire_et_ecrire_csv(simple_csv, "Communes_uniques.csv", [0, 1, 2, 3])
#Position des en-tête codeInstallation = 4, codeInseeCommune = 2, libelle = 9, metro = 19, bus = 20, tram = 21,train = 22, bateau = 23, autreTransport = 24, aucunTransport = 25, dateMAJ = 26, dateCreation = 27
lire_et_ecrire_csv(simple_csv, "Admissions_par_formation_détaillée.csv", [2, 4, 9, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27])
"""

def lire_et_ecrire_csv(nom_fichier_entree, nom_fichier_sortie, colonnes_a_recuperer):
    donnees = []
    with open(nom_fichier_entree, errors="ignore") as fichier_entree: #encoding="ISO-8859-1"
        reader = csv.reader(fichier_entree, delimiter=';')
        for ligne in reader:
            donnees.append(ligne)

    with open(nom_fichier_sortie, 'w', newline='') as fichier_sortie:
        writer = csv.writer(fichier_sortie)
        for ligne in donnees:
            colonnes_selectionnees = [ligne[colonne] for colonne in colonnes_a_recuperer]
            writer.writerow(colonnes_selectionnees)

#Position des en-tête codeInstallation = 4, nomInstallation = 5, nbEquipements = 28, adresse = 6, nbParking = 16, nbParkingHandi = 17
lire_et_ecrire_csv(data_csv, installations_uniques_csv, [codeInstallation, nomInstallation, nbEquipements, adresse, nbParking, nbParkingHandi])
#Position des en-tête codeInseeCommune = 2, nomComune = 3, codeDepartement = 0, nomDepartement = 1
lire_et_ecrire_csv(data_csv, communes_uniques_csv, [codeInseeCommune, nomCommune, codeDepartement, nomDepartement])
#Position des en-tête codeInstallation = 4, codeInseeCommune = 2, libelle = 9, metro = 19, bus = 20, tram = 21,train = 22, bateau = 23, autreTransport = 24, aucunTransport = 25, dateMAJ = 26, dateCreation = 27
lire_et_ecrire_csv(data_csv, admissions_par_formation_detaillee_csv, [codeInstallation, codeInseeCommune, libelle, metro, bus, tram, train, bateau, autreTransport, aucunTransport, dateMAJ, dateCreation])

