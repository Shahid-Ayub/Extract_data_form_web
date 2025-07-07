import urllib.request
from bs4 import BeautifulSoup

# Prompt for input
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

print("Retrieving:", url)

# Loop for the number of times to follow the link
for i in range(count):
    # Open and read the HTML content
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Get all the anchor tags
    tags = soup('a')

    # Find the tag at the given position (1-based index, so subtract 1)
    url = tags[position - 1].get('href', None)
    print("Retrieving:", url)

# Print the last name from the final URL
name = url.split('_')[-1].split('.')[0]
print("The answer to the assignment is:", name)
