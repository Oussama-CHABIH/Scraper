import pandas as pd

# Spécifiez le chemin vers le fichier CSV d'entrée et de sortie
input_file = "journal_data.csv"
output_file = "filtered_data.csv"

# Lire le fichier CSV dans un DataFrame pandas
df = pd.read_csv(input_file)

# Spécifiez le nom de la colonne à analyser (par exemple: "description")
column_name = "Subject Area and Category"

# Vérifier si la colonne existe dans le fichier CSV
if column_name in df.columns:
    # Filtrer les lignes où la colonne contient 'computer' ou 'software'
    filtered_df = df[df[column_name].str.contains('computer|software', case=False, na=False)]

    # Écrire le DataFrame filtré dans un nouveau fichier CSV
    filtered_df.to_csv(output_file, index=False)

    print(f"Les lignes contenant 'computer' ou 'software' ont été enregistrées dans {output_file}.")
else:
    print(f"La colonne '{column_name}' n'existe pas dans le fichier CSV.")
