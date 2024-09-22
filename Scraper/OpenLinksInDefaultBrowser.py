import webbrowser
import time

# Liste des URLs à ouvrir
urls = [
'https://www.scopus.com//sourceid//21101027394',
'https://www.scopus.com//sourceid//21101052353',
'https://www.scopus.com//sourceid//21100242828',
'https://www.scopus.com//sourceid//78470',
'https://www.scopus.com//sourceid//21101039156',
'https://www.scopus.com//sourceid//21101133424',
'https://www.scopus.com//sourceid//21101021053',
'https://www.scopus.com//sourceid//21100901898',
'https://www.scopus.com//sourceid//21100855805',
'https://www.scopus.com//sourceid//21100935898',
'https://www.scopus.com//sourceid//21100815354',
'https://www.scopus.com//sourceid//21100818502',
'https://www.scopus.com//sourceid//21101094914',
'https://www.scopus.com//sourceid//19700177033',
'https://www.scopus.com//sourceid//21101073954',
'https://www.scopus.com//sourceid//21101157925',
'https://www.scopus.com//sourceid//21100981170',
'https://www.scopus.com//sourceid//21100327713',
'https://www.scopus.com//sourceid//21101018670',
'https://www.scopus.com//sourceid//25064',
'https://www.scopus.com//sourceid//21101101245',
'https://www.scopus.com//sourceid//19900188004',
'https://www.scopus.com//sourceid//21100197714',
'https://www.scopus.com//sourceid//21101030114',
'https://www.scopus.com//sourceid//21101168860',
'https://www.scopus.com//sourceid//21100199727',
'https://www.scopus.com//sourceid//21101176845',
'https://www.scopus.com//sourceid//21101102022',
'https://www.scopus.com//sourceid//21101051699',
'https://www.scopus.com//sourceid//21101186339',
'https://www.scopus.com//sourceid//21101201510',
'https://www.scopus.com//sourceid//21101151576',
'https://www.scopus.com//sourceid//40067',
'https://www.scopus.com//sourceid//21101128459',
'https://www.scopus.com//sourceid//21101120357',
'https://www.scopus.com//sourceid//21100788880',
'https://www.scopus.com//sourceid//21101192901',
'https://www.scopus.com//sourceid//21100217007',
'https://www.scopus.com//sourceid//21101152758',
'https://www.scopus.com//sourceid//21101184660',
'https://www.scopus.com//sourceid//5800207596',
'https://www.scopus.com//sourceid//21101181972',
'https://www.scopus.com//sourceid//6400153142',
'https://www.scopus.com//sourceid//21100778845',
'https://www.scopus.com//sourceid//19900191717',
'https://www.scopus.com//sourceid//21101188421',
'https://www.scopus.com//sourceid//21101180709',
'https://www.scopus.com//sourceid//21100903490',
'https://www.scopus.com//sourceid//20569',
'https://www.scopus.com//sourceid//21100199733',
'https://www.scopus.com//sourceid//27273',
'https://www.scopus.com//sourceid//24020',
'https://www.scopus.com//sourceid//17600155043',
'https://www.scopus.com//sourceid//21100464658',
'https://www.scopus.com//sourceid//20980',
'https://www.scopus.com//sourceid//21100222913',
'https://www.scopus.com//sourceid//21100793186',
'https://www.scopus.com//sourceid//4400151723',

    # Ajoutez autant d'URLs que nécessairez
]

# Ouvrir le premier lien dans le navigateur
webbrowser.open(urls[0])

# Ouvrir chaque URL dans un nouvel onglet
for url in urls[1:]:
    time.sleep(2)  # Attendre 1 seconde avant d'ouvrir un nouvel onglet (facultatif)
    webbrowser.open_new_tab(url)
