import requests
import gspread
import pandas as pd
from bs4 import BeautifulSoup


# Extract the link and the name country of the websites from text file
def extractWebsite(indices, links, countries, sheet):
    if sheet:
        for index in indices:
            i = int(index[0]) % 5
            Web = Website(links[0], countries[0] + str(i))
            Web.createText()
    else:
        for index in indices:
            i = int(index) % 5
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
            line = str(doc.body.findAll("p")[x].text).replace("\n", " ")
            if line != "":
                text += line
                text += "\n"

        self.country = "Data file\\" + self.country + ".txt"
        with open(self.country, 'w') as f:
            f.write(text)


# read data from excel
def readExcel():
    print("Read from Excel...\n")
    df = pd.read_excel(r'Data.xlsx')
    indices = df.get("Index")
    links = df.get("Link")
    countries = df.get("Country")
    extractWebsite(indices, links, countries, False)


# read data from google sheet
def readGoogleSheet():
    print("Read from Google Sheet...\n")

    sa = gspread.service_account("Creds.json")
    sh = sa.open("Data")

    sheet = sh.worksheet("Sheet1")
    indices = sheet.get("A2:A26")
    links = sheet.get("B2:B26")
    countries = sheet.get("C2:C26")

    for i in range(len(indices)):
        extractWebsite(indices[i], links[i], countries[i], True)


# main function
readExcel()
# readGoogleSheet()
