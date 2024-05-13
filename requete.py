import json

# Fichier à convertir
filename = 'data1.txt'

# Liste résultante des données JSON
data = []

# Noms des champs dans le fichier
fields = ['title', 'cast', 'directors', 'producers', 'companies', 'year']

with open(filename) as fh:
    for line in fh:
        # Conversion de la ligne en un dictionnaire JSON
        record = json.loads(line)
        
        # Ajout du dictionnaire à la liste des données
        data.append(record)

# Création du fichier JSON
with open("test2.json", "w") as out_file:
    json.dump(data, out_file, indent=4)
