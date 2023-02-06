
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

def creation (nom_entree, colonnes, nom_sortie) :
    fichier_sorite = nom_sortie
    with open (nom_entree,'r', newline='') as csv_file :
        reader = csv.reader(csv_file,  delimiter=' ', quotechar='|')
        liste_fichier = []
        for row in reader :
            liste_fichier.append(', '.join(row))
        with open (fichier_sorite, 'w', newline='') as csv_sortie :
            writer = csv.writer(csv_sortie)
            writer.writerow([liste_fichier[line][column] for column in colonnes] for line in range(len(liste_fichier)))

creation(simple_csv,[0,5,8], "installations_uniques.csv")
