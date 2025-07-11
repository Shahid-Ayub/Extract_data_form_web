import requests
from bs4 import BeautifulSoup  

url = input('Enter your URL: ') # Says to users to enter the URL

response = requests.get(url)   # send request and get respone from the web

if response.status_code == 200: # looks that url matches or not if yes it return 200 if no then 403

    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.find_all('div', class_='quote') # looks for the quotes
    
    for i, quote in enumerate(quotes, start=1): # start the loop form 1

        text = quote.find('span', class_='text').text # Make the quotes as same as at the web
  
        author = quote.find('small', class_='author').text 

        print(f"{i}. {text} --- {author}")  # looks for the Author names who wrote the quotes

else:
    print("Failed to retrive the webpage", response.status_code)  # if requests did not matches the response showa 404