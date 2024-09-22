import pandas as pd

# Spécifiez le chemin vers le fichier CSV d'entrée et le fichier de sortie
input_file = "filtered_data.csv"
output_file = "output_cases.txt"

# Lire le fichier CSV dans un DataFrame pandas
df = pd.read_csv(input_file)

# Spécifiez le nom de la colonne à analyser (exemple: "couleur")
column_name = "Subject Area and Category"

# Vérifier si la colonne existe dans le fichier CSV
if column_name in df.columns:
    # Extraire les valeurs uniques de la colonne et les compter
    value_counts = df[column_name].value_counts()

    # Écrire les résultats dans un fichier texte
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Les différents cas dans la colonne '{column_name}' sont :\n\n")
        for value, count in value_counts.items():
            f.write(f"{value}: {count}\n")

    print(f"Les résultats ont été écrits dans {output_file}.")
else:
    print(f"La colonne '{column_name}' n'existe pas dans le fichier CSV.")
