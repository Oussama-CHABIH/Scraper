import pandas as pd

# Spécifiez le chemin vers le fichier CSV et le fichier texte
csv_file = "filtered_data.csv"
txt_file = "titles2024.txt"
output_csv = "filtered_data2.csv"

# Charger le fichier CSV dans un DataFrame pandas
df = pd.read_csv(csv_file)

# Charger les titres du fichier texte dans un ensemble (pour une recherche rapide)
with open(txt_file, 'r', encoding='utf-8') as f:
    valid_titles = set(line.strip() for line in f)

# Vérifier si la colonne 'title' existe dans le CSV
if 'Title' in df.columns:
    # Garder uniquement les lignes dont le titre existe dans le fichier txt
    filtered_df = df[df['Title'].isin(valid_titles)]

    # Sauvegarder le DataFrame filtré dans un nouveau fichier CSV
    filtered_df.to_csv(output_csv, index=False)

    print(f"Les lignes avec des titres présents dans {txt_file} ont été enregistrées dans {output_csv}.")
else:
    print("La colonne 'title' n'existe pas dans le fichier CSV.")
