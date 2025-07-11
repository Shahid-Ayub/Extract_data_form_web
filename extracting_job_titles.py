import requests
from bs4 import BeautifulSoup

url = input('Enter URL: ')  # ask's user to enter the URL

response = requests.get(url) # SEND REQUEST TO THE WEV SERVER

soup = BeautifulSoup(response.text, "html.parser") # look after the html content

jobs = soup.find_all("div", class_="card-content") # this statments looks for all the jobs

print("Python-related jobs:\n")
 
for job in jobs: # loop for finding the required job details

    title = job.find("h2", class_="title").text # loook for the job titles

    company = job.find("h3", class_="company").text # look for the job company

    location = job.find("p", class_="location").text # looks for the company location

    if "python" in title.lower():

        print(f"Title: {title}")   # print the required data -----

        print(f"Company: {company}")

        print(f"Location: {location}")

        print("-" * 40)