import requests
from bs4 import BeautifulSoup
import csv

# Fichier contenant les URLs (chaque ligne contient une URL)
links_file = "links.txt"

# Fichier CSV pour enregistrer les résultats
output_file = "journal_data.csv"

# Ouvrir le fichier contenant les URLs et traiter chaque URL
with open(links_file, 'r') as file:
    urls = file.readlines()

# Ouvrir un fichier CSV pour écrire les données
with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Écrire l'en-tête
    writer.writerow(['URL', 'Title', 'ISSN', 'Homepage', 'How to publish', 'Publisher', 'Subject Area and Category'])

    # Traiter chaque URL
    for url in urls:
        url = url.strip()  # Supprimer les espaces ou nouvelles lignes

        # Envoyer une requête HTTP pour récupérer le contenu de la page
        response = requests.get(url)

        # Vérifier si la requête a réussi (statut 200)
        if response.status_code == 200:
            # Récupérer le contenu HTML de la réponse
            page_content = response.content

            # Parser le contenu HTML avec BeautifulSoup
            soup = BeautifulSoup(page_content, 'html.parser')

            # Extraire les données requises
            title = soup.find('h1').text.strip() if soup.find('h1') else "Title not found"

            # Rechercher l'ISSN
            issn_tag = soup.find('h2', string="ISSN")
            issn = issn_tag.find_next('p').text.strip() if issn_tag else "ISSN not found"

            # Rechercher les liens de Homepage et "How to publish"
            homepage_link = soup.find('a', text="Homepage")['href'] if soup.find('a',
                                                                                 text="Homepage") else "Homepage link not found"
            publish_link = soup.find('a', text="How to publish in this journal")['href'] if soup.find('a',
                                                                                                      text="How to publish in this journal") else "How to publish link not found"

            # Extraire le Subject Area and Category
            subject_area_tag = soup.find('h2', string="Subject Area and Category")
            categories = subject_area_tag.find_next('ul').get_text(
                separator=", ").strip() if subject_area_tag else "Subject Area not found"

            # Extraire le Publisher
            publisher_tag = soup.find('h2', string="Publisher")
            publisher = publisher_tag.find_next('p').text.strip() if publisher_tag else "Publisher not found"

            # Écrire les données dans le fichier CSV
            writer.writerow([url, title, issn, homepage_link, publish_link, publisher, categories])

            print(f"Données extraites pour {url}")

        else:
            print(f"Erreur: Impossible de récupérer la page {url}, statut {response.status_code}")

print(f"Toutes les données ont été extraites et enregistrées dans {output_file}.")
