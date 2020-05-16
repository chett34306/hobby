from bs4 import BeautifulSoup
import requests

def redfinscrap():
    
    response = requests.get('https://www.zillow.com/homes/98029_rb/')
    #'https://www.redfin.com/zipcode/98029')
    soup = BeautifulSoup(response.text, 'lxml')
    print(soup)
    items = soup.find_all('ul', class_='photo-cards photo-cards_wow photo-cards_short')
    print("****all properties***")
    print(items)

redfinscrap()