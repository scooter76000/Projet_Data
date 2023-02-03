import csv

# ------ chemin des fichier.csv  ------
data_csv = "2020_installations_sportives.csv" # fichier orginal (sujet)

# Fichier constituer du code de l'installation, nom de l'installation, nombre d'Equipement, de l'adresse et du nombre de place de parking handicaper ou pas.
data_installations_uniques_csv = "data/IntallationsUniques.csv" 

#Fichier constituer du code INSEE de la commune, du nom de la commune, du code du department et du nom du département.
data_communes_uniques_csv = "data/CommunesUniques.csv"

# Fichier constituer du code de l'installation, du code INSEE de la commune, du libelle, des different moyen de transport(Metro,Bus,Tram,Train,Bateau ou autre voir pas) et des la date de mise à jour et de création
data_admissions_par_formation_detaillee_csv = "data/AdmissionParFormationDetaillee.csv"


# ------ Fonction -------

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

def ecriture_csv(nom_fichier_csv, header):
    # Ouverutre d'un fichier csv en mode 'w" write = écriture et un saut de ligne
    with open(nom_fichier_csv, "w", newline="") as csv_file:
        # Écriture du fichier csv avec un paramètre un delimitation par le ";"
        writer = csv.writer(csv_file, delimiter=";")
        # Écriture de l'en tête du fichier csv
        writer.writerow(header)
        # Écriture du fichier.csv
        writer.writerow(["31", "Haute-Garonne"]) # test ecriture dans le fichier csv


# ----   fichier.csv en liste  --------

def csv_en_liste(nom_fichier_csv, valeur_ligne, valeur_valeur):
    with open(nom_fichier_csv, errors="ignore") as f:
        lecture = csv.reader(f, delimiter=";")
        lignes = list(lecture)

    #print(f"La ligne 0 du fichier: {lignes[0]}.")
    #print(f"La ligne 1 du fichier: {lignes[1]}.")
    #print(f"Le nombre de lignes du fichier: {len(lignes)}.")
    #print("")
    print(f"La ligne", valeur_ligne, "du fichier qui donne", lignes[0][valeur_valeur], ":", lignes[valeur_ligne][valeur_valeur])



# -----  Test des Fontion et Affichage ----

# Test de la fonction lecutre_csv
lecture_csv(data_csv)
  
######   Test des nouveau fichier csv cree   #####

lecture_csv(data_installations_uniques_csv)
print("")
lecture_csv(data_communes_uniques_csv)
print("")
lecture_csv(data_admissions_par_formation_detaillee_csv)

  
# ----  Test de la fonction fichier.csv en liste ----

ligne = 2 # ligne 0 = en-tête 
valeur = 3 # valeur = A sur le execel 
csv_en_liste(data_csv, ligne, valeur)
