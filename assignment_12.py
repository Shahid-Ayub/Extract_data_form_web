import urllib.request
from bs4 import BeautifulSoup

# Prompt the user for the URL
url = input("Enter - ")

# Open the URL and read the HTML content
html = urllib.request.urlopen(url).read()

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the span tags
tags = soup('span')

# Initialize sum and count
total = 0
count = 0

# Loop through all span tags
for tag in tags:
    try:
        number = int(tag.contents[0])  # Get the number inside the span
        total += number
        count += 1
    except:
        continue  # In case of unexpected formatting

# Print results
print("Count", count)
print("Sum", total)
