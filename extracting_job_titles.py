import requests
from bs4 import BeautifulSoup

url = input('Enter URL: ')

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Step 2: Find all job listings
jobs = soup.find_all("div", class_="card-content")

# Step 3: Filter and print jobs with "Python" in the title
print("Python-related jobs:\n")
for job in jobs:
    title = job.find("h2", class_="title").text
    company = job.find("h3", class_="company").text
    location = job.find("p", class_="location").text

    if "python" in title.lower():
        print(f"Title: {title}")
        print(f"Company: {company}")
        print(f"Location: {location}")
        print("-" * 40)