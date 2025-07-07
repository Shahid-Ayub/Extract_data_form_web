import urllib.request
from bs4 import BeautifulSoup

url = input("Enter the URL: ")

html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

paragraphs = soup.find_all('p')

word = input("Enter the word you want to find: ").lower()

if len(paragraphs) >= 4:
    text = paragraphs[3].get_text().lower()
    if word in text:
        print("Found the word!")
        print("Paragraph:", paragraphs[3].get_text())
    else:
        print("Word not found in the 4th paragraph.")
else:
    print("The page does not have at least 4 paragraphs.")
