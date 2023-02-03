import csv

# ------ chemin des fichier.csv  ------
data_csv = "2020_installations_sportives.csv"  # fichier orginal (sujet)

# Fichier constituer du code de l'installation, nom de l'installation, nombre d'Equipement, de l'adresse et du nombre de place de parking handicaper ou pas.
data_installations_uniques_csv = "data/IntallationsUniques.csv"

# Fichier constituer du code INSEE de la commune, du nom de la commune, du code du department et du nom du département.
data_communes_uniques_csv = "data/CommunesUniques.csv"

# Fichier constituer du code de l'installation, du code INSEE de la commune, du libelle, des different moyen de transport(Metro,Bus,Tram,Train,Bateau ou autre voir pas) et des la date de mise à jour et de création
data_admissions_par_formation_detaillee_csv = "data/AdmissionParFormationDetaillee.csv"


# ------ Fonction -------

# ----- Fonction esthétique / grap -----

def space_graph(valeur):
    for i in range(valeur):
        print("")


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

def csv_en_liste(nom_fichier_csv, valeur_ligne, valeur_valeur):
    with open(nom_fichier_csv, errors="ignore") as f:
        lecture = csv.reader(f, delimiter=";")
        lignes = list(lecture)

    print(f"La ligne", valeur_ligne, "du fichier qui donne", lignes[0][valeur_valeur], ":",
          lignes[valeur_ligne][valeur_valeur])

    # ---- Test interne de la fonction ----
    # print(f"La ligne 0 du fichier: {lignes[0]}.")
    # print(f"La ligne 1 du fichier: {lignes[1]}.")
    # print(f"Le nombre de lignes du fichier: {len(lignes)}.")

def csv_en_liste_v2(nom_fichier_csv, valeur_ligne, valeur_valeur):
    with open(nom_fichier_csv, errors="ignore") as f:
        lecture = csv.reader(f, delimiter=";")
        lignes = list(lecture)

    return (lignes[valeur_ligne][valeur_valeur])


# -----  Test des Fontion et Affichage ----

# Test de la fonction lecutre_csv
lecture_csv(data_csv)
space_graph(4)

######   Test des nouveau fichier csv cree   #####

#Position des en-tête codeInstallation = 4, nomInstallation = 5, nbEquipements = 28, adresse = 6, nbParking = 16, nbParkingHandi = 17
header_installations_uniques_csv_v2 = [
  (csv_en_liste_v2(data_csv, 0, 4)), (csv_en_liste_v2(data_csv, 0, 5)),
  (csv_en_liste_v2(data_csv, 0, 28)), (csv_en_liste_v2(data_csv, 0, 6)),
  (csv_en_liste_v2(data_csv, 0, 16)), (csv_en_liste_v2(data_csv, 0, 17))
]
data_installations_uniques_csv_L = [
  (csv_en_liste_v2(data_csv, 1, 4)), (csv_en_liste_v2(data_csv, 1, 5)),
  (csv_en_liste_v2(data_csv, 1, 28)), (csv_en_liste_v2(data_csv, 1, 6)),
  (csv_en_liste_v2(data_csv, 1, 16)), (csv_en_liste_v2(data_csv, 1, 17))
]

ecriture_csv(data_installations_uniques_csv, header_installations_uniques_csv_v2, data_installations_uniques_csv_L)
lecture_csv(data_installations_uniques_csv)
space_graph(2)

#Position des en-tête codeInseeCommune = 2, nomCommune = 3, codeDepartement = 0, nomDepartement = 1
header_communes_uniques_csv_v2 = [
  (csv_en_liste_v2(data_csv, 0, 2)), (csv_en_liste_v2(data_csv, 0, 3)),
  (csv_en_liste_v2(data_csv, 0, 0)), (csv_en_liste_v2(data_csv, 0, 1))
]
data_installations_uniques_csv_v2 = [
  (csv_en_liste_v2(data_csv, 1, 2)), (csv_en_liste_v2(data_csv, 1, 3)),
  (csv_en_liste_v2(data_csv, 1, 0)), (csv_en_liste_v2(data_csv, 1, 1))
]

ecriture_csv(data_communes_uniques_csv, header_communes_uniques_csv_v2, data_installations_uniques_csv_v2)
lecture_csv(data_communes_uniques_csv)
space_graph(2)

#Position des en-tête codeInstallation = 4, codeInseeCommune = 2, libelle = 9, metro = 19, bus = 20, tram = 21, train = 22,
# bateau = 23, autreTransport = 24, aucunTransport = 25, dateMAJ = 26, dateCreation = 27
header_admissions_par_formation_detaillee_csv_v2 = [
  (csv_en_liste_v2(data_csv, 0, 4)), (csv_en_liste_v2(data_csv, 0, 2)),
  (csv_en_liste_v2(data_csv, 0, 9)), (csv_en_liste_v2(data_csv, 0, 19)),
  (csv_en_liste_v2(data_csv, 0, 20)), (csv_en_liste_v2(data_csv, 0, 21)),
  (csv_en_liste_v2(data_csv, 0, 22)), (csv_en_liste_v2(data_csv, 0, 23)),
  (csv_en_liste_v2(data_csv, 0, 24)), (csv_en_liste_v2(data_csv, 0, 25)),
  (csv_en_liste_v2(data_csv, 0, 26)), (csv_en_liste_v2(data_csv, 0, 27))
]
data_admissions_par_formation_detaillee_csv_v2 = [
  (csv_en_liste_v2(data_csv, 1, 4)), (csv_en_liste_v2(data_csv, 1, 2)),
  (csv_en_liste_v2(data_csv, 1, 9)), (csv_en_liste_v2(data_csv, 1, 19)),
  (csv_en_liste_v2(data_csv, 1, 20)), (csv_en_liste_v2(data_csv, 1, 21)),
  (csv_en_liste_v2(data_csv, 1, 22)), (csv_en_liste_v2(data_csv, 1, 23)),
  (csv_en_liste_v2(data_csv, 1, 24)), (csv_en_liste_v2(data_csv, 1, 25)),
  (csv_en_liste_v2(data_csv, 1, 26)), (csv_en_liste_v2(data_csv, 1, 27))
]

ecriture_csv(data_admissions_par_formation_detaillee_csv, header_admissions_par_formation_detaillee_csv_v2, data_admissions_par_formation_detaillee_csv_v2)
lecture_csv(data_admissions_par_formation_detaillee_csv)
space_graph(4)

# ----  Test de la fonction fichier.csv en liste ----

ligne = 5  # ligne 0 = en-tête
valeur = 3  # valeur = A sur le execel
csv_en_liste(data_csv, ligne, valeur)
space_graph(4)
