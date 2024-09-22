import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import pandas as pd

# Fonction pour récupérer le texte propre d'une URL
def get_text_from_url(url):
    response = requests.get(url)

    if response.status_code == 200:
        # Parser le contenu HTML avec BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Supprimer les balises script et style (CSS/JS)
        for script in soup(["script", "style"]):
            script.decompose()

        # Récupérer tout le texte visible sur la page
        text = soup.get_text(separator="\n", strip=True)

        return text
    else:
        print(f"Erreur: Impossible de récupérer la page {url}, statut {response.status_code}")
        return None


# Fonction pour récupérer le texte du site principal et des liens du même domaine, puis stocker dans un fichier
def get_text_and_follow_same_domain_links(initial_url, output_file):
    # Extraire le domaine de l'URL initiale
    initial_domain = urlparse(initial_url).netloc

    with open(output_file, 'w', encoding='utf-8') as f:
        # Récupérer et écrire le texte principal dans le fichier
        main_text = get_text_from_url(initial_url)

        if main_text:
            f.write(f"Texte du site principal ({initial_url}):\n")
            f.write(main_text)
            f.write("\n" + "=" * 50 + "\n")

        # Parser à nouveau pour suivre les liens
        response = requests.get(initial_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Trouver tous les liens href sur la page
        links = soup.find_all('a', href=True)
        for link in links:
            href = link['href']

            # Construire l'URL absolue à partir du lien, si besoin
            href = urljoin(initial_url, href)

            # Extraire le domaine du lien
            link_domain = urlparse(href).netloc

            # Vérifier si le domaine est le même que celui de l'URL initiale
            if link_domain == initial_domain:
                # Récupérer et écrire le texte de la page liée dans le fichier
                f.write(f"Texte du lien ({href}):\n")
                link_text = get_text_from_url(href)
                if link_text:
                    f.write(link_text)
                    f.write("\n" + "=" * 50 + "\n")
                else:
                    f.write(f"Impossible de récupérer le texte pour {href}\n")
                    f.write("\n" + "=" * 50 + "\n")


# Charger le fichier CSV
csv_file = "filtered_data2.csv"  # Replace with the actual file path
data = pd.read_csv(csv_file)

# Parcourir chaque ligne du fichier CSV
for index, row in data.iterrows():
    title = row['Title']  # Nom du fichier sera basé sur le titre
    homepage_url = row['Homepage']
    #how_to_publish_url = row['How to publish']

    # Créer des noms de fichiers basés sur le titre du journal
    homepage_output_file = "JournalsTexts//" + f"{title}_homepage_text.txt".replace(" ", "_")
    #how_to_publish_output_file = f"{title}_how_to_publish_text.txt".replace(" ", "_")

    # Traiter la page d'accueil (Homepage)
    if pd.notna(homepage_url):  # Vérifier si l'URL n'est pas vide
        get_text_and_follow_same_domain_links(homepage_url, homepage_output_file)

    # Traiter la page "How to publish"
    #if pd.notna(how_to_publish_url):  # Vérifier si l'URL n'est pas vide
       # get_text_and_follow_same_domain_links(how_to_publish_url, how_to_publish_output_file)

print("Extraction terminée pour tous les liens.")
