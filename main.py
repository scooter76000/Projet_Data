import csv

data_csv = "/home/runner/Projet-Data-Groupe-G/fichier1.csv" #chemin fichier selon le pwd 

"""
pwd est un commande linux/Unix pour avoir le nom complet de l'arborescence d'un fichier
"""

with open(data_csv, errors="ignore") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)