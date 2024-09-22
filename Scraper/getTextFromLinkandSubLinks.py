import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


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


# URL du site principal à traiter
url = "https://www.keaipublishing.com/en/journals/ai-open/"

# Fichier dans lequel enregistrer le texte
output_file = "site_text_output.txt"

# Récupérer le texte principal et les textes des liens du même domaine et les stocker dans un fichier
get_text_and_follow_same_domain_links(url, output_file)

print(f"Le texte a été récupéré et enregistré dans {output_file}.")
