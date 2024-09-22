from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Démarrer le WebDriver (ici avec Chrome)
s = Service('C:\\Program Files\\Google\\Chrome\\Application\\129.0.6668.58\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

# Aller à l'URL du site
driver.get(" https://www.scopus.com/sourceid/21101101212")



# Extraire le contenu après la recherche
page_content = driver.page_source
print(page_content)

# Fermer le navigateur
driver.quit()
