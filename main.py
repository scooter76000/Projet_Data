import csv

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


simple_csv = "fichier1.csv"


def creation_fichier(colonnes, nom_fichier):
    fichier_sortie = nom_fichier
    with open(simple_csv, 'r') as csv_file, open(fichier_sortie, 'w', newline='') as csv_sortie:
        reader = csv.reader(csv_file)
        writer = csv.writer(csv_sortie)
        header = next(reader)
        colonne = [header[index] for index in colonnes]
        writer.writerow(colonne)
        for ligne in reader:
            colonne = [ligne[index] for index in colonnes]
            writer.writerow(colonne)


creation_fichier([0], "installations uniques.csv")





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

######    Lecture / Ecriture : ok    ###### Fin

"""