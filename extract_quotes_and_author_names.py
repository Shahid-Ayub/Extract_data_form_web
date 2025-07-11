import requests
from bs4 import BeautifulSoup

url = input('Enter your URL: ')

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.find_all('div', class_='quote')
    
    for i, quote in enumerate(quotes, start=1):

        text = quote.find('span', class_='text').text

        author = quote.find('small', class_='author').text

        print(f"{i}. {text} --- {author}")

else:
    print("Failed to retrive the webpage", response.status_code)