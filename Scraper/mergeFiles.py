import os

# Dossier où se trouvent les fichiers à fusionner
directory = "C:\\Users\\H2O\\Documents\\Htmls"

# Nom du fichier final fusionné
output_file = "C:\\Users\\H2O\\Documents\\Htmls\\merged file\\merged_file.html"

# Ouvrir le fichier de sortie en mode écriture
with open(output_file, 'w', encoding='utf-8') as outfile:
    # Parcourir tous les fichiers dans le dossier
    for filename in os.listdir(directory):
        # Vérifier si le fichier est un fichier HTML ou texte (modifiez l'extension si nécessaire)
        if filename.endswith(".html") or filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)

            # Lire le contenu de chaque fichier
            with open(file_path, 'r', encoding='utf-8') as infile:
                content = infile.read()

                # Supprimer les retours à la ligne et les espaces inutiles
                content_single_line = ' '.join(content.split())

                # Écrire le contenu sur une seule ligne dans le fichier fusionné
                outfile.write(f"<!-- Contenu du fichier: {filename} -->\n")
                outfile.write(content_single_line)
                outfile.write("\n\n")  # Ajouter un espace entre les fichiers
            print(f"Fichier {filename} ajouté à {output_file}.")

print(f"Tous les fichiers ont été fusionnés dans {output_file} sous forme de lignes uniques.")