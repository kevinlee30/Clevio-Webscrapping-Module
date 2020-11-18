#Clevio - Data Scraping

import bs4
import requests

url = requests.get('https://www.newegg.com/Laptops-Notebooks/Category/ID-223?Tpk=laptop')
soup = bs4.BeautifulSoup(url.text, 'html.parser')

