from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://mexico.as.com/resultados/futbol/mexico_clausura/clasificacion/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

name = soup.find_all('span', class_="nombre-equipo")
la = list()

for i in name:
    la.append(i.text)

print(la)

