  
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


"""fonction lecture et ecriture de fichier CSV qui prend en paramètre le nom du fichier en entrée et celui en sortie une liste d'Index des colonnes qu'on veut recuperer"""
def lire_et_ecrire_csv(nom_fichier_entree, nom_fichier_sortie,
                       colonnes_a_recuperer, nombre_ligne):
  """Ici on lit le fichier csv et on rentre les donn""ées dans une liste"""
  
  donnees = [] 
  with open(nom_fichier_entree, 'r', encoding="ISO-8859-1") as fichier_entree:
    reader = csv.reader(fichier_entree, delimiter = ';')
    for ligne in reader:
      donnees.append(ligne)
        
  """ici la fonction crée un nouveau fichier avec le nom en paramètre et avec une double boucle une qui récuperer les ligne et l'autre les colonnes la fonction recupére les données de la liste et les ecrit dans le nouveau fichier csv"""
  with open(nom_fichier_sortie, 'w', newline='') as fichier_sortie:
    writer = csv.writer(fichier_sortie, delimiter = ';' )
    ligne_max = 0
    for ligne in donnees:
      if ligne_max <= nombre_ligne :
        colonnes_selectionnees = [
        ligne[colonne] for colonne in colonnes_a_recuperer
      ]
        ligne_max +=1
        writer.writerow(colonnes_selectionnees)
  

"""Fonction qui recupére les données d'un fichier csv et les stocks dans une liste avec en paramètre le nom du fichier et le nom de la liste qu'on veut creer"""               
def changement_de_données (nom_fichier_entree, Si) :
    Si = []
    with open(nom_fichier_entree, 'r', encoding="ISO-8859-1") as fichier_entree:
        reader = csv.reader(fichier_entree, delimiter=';')
        for ligne in reader:
            Si.append(ligne)
        return Si


def projection_simple(Si,nomDeColonne) :
  for ligne in Si:
      for colonne in Si[ligne] :
        if Si[ligne][colonne] == nomDeColonne :
          
          
          
  



projection_simple(changement_de_données(installations_uniques_csv, "S1"), nomInstallation)


def projection_multiple(Si,nomdecol):
nomdecol=[]
  for ligne in Si:
    for colonne in Si:
      if nomDeColonne == nomdecol
  return nomdecol

def projection_simple_distinct(Si, nomDeColonne):
  
  return Si
