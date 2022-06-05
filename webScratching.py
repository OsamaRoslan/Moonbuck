import requests
import pandas as pd
from bs4 import BeautifulSoup


# Extract the link and the name country of the websites from text file
def extractWebsite(indices, links, countries):
    for index in indices:
        i = index % 5
        Web = Website(links[int(index) - 1], countries[int(index) - 1] + str(i))
        Web.createText()


# Extract word from website
class Website:

    # instance attributes
    def __init__(self, url, country):
        self.url = url
        self.country = country

    def createText(self):
        # Make a request
        page = requests.get(self.url)
        doc = BeautifulSoup(page.text, 'html.parser')
        text = "Title: " + doc.title.text

        for x in range(len(doc.body.findAll("p"))):
            text += str(doc.body.findAll("p")[x].text)
            text += "\n"

        self.country += ".txt"
        with open(self.country, 'w') as f:
            f.write(text)


# read data from excel
def readExcel():
    print("running...")
    df = pd.read_excel(r'Data.xlsx')
    indices = df.get("Index")
    links = df.get("Link")
    countries = df.get("Country")
    extractWebsite(indices, links, countries)


# read data from google sheet


# main
readExcel()
