import os

# Dossier où se trouvent les fichiers à fusionner
directory = "C:\\Users\\H2O\\Documents\\Htmls"

# Nom du fichier final fusionné
output_file = "C:\\Users\\H2O\\Documents\\Htmls\\merged file\\merged_file.html"

# Ouvrir le fichier de sortie en mode écriture
with open(output_file, 'w', encoding='utf-8') as outfile:
    # Parcourir tous les fichiers dans le dossier
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Vérifier si c'est un fichier (éviter les dossiers)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as infile:
                # Lire toutes les lignes du fichier
                lines = infile.readlines()

                # Vérifier si le fichier a assez de lignes
                if len(lines) >= 1288:
                    # Récupérer les lignes 1273, 1276 et 1288 (indices 1272, 1275 et 1287)
                    line_1273 = lines[1272]
                    line_1276 = lines[1275]
                    line_1288 = lines[1287]

                    # Sauvegarder les lignes dans le fichier de sortie
                    outfile.write(f"{filename}:\n")
                    outfile.write(f"Line 1273: {line_1273}")
                    outfile.write(f"Line 1276: {line_1276}")
                    outfile.write(f"Line 1288: {line_1288}\n")
                    outfile.write("-" * 40 + "\n")
                else:
                    # Si le fichier n'a pas assez de lignes, ajouter un message d'erreur
                    outfile.write(f"{filename}: Le fichier ne contient pas assez de lignes.\n")
                    outfile.write("-" * 40 + "\n")

print(f"Les lignes 1273, 1276, et 1288 ont été sauvegardées dans {output_file}.")