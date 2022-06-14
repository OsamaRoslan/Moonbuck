import requests
import gspread
import pandas as pd
from bs4 import BeautifulSoup
import time

OS = ""


# Extract the link and the name country of the websites from text file
def extractWebsite(indices, links, countries, sheet):
    if sheet:
        for index in indices:
            i = int(index[0]) % 5
            if i == 0:
                i = 5
            Web = Website(links[0], "Data" + index)
            Web.createText()
    else:
        for index in indices:
            Web = Website(links[int(index) - 1], "Data" + index)
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
            else:
                pass

        print("Creating Text...")
        self.country = "Data file\\" + self.country + ".txt"
        with open(self.country, 'w', encoding="utf-8") as f:
            f.write(text)


# read data from excel
def readExcel(OS):
    print("Read from Excel...")
    if OS == "mac":
        df = pd.read_excel(r'Database//Data.xlsx')
    if OS == "windows":
        df = pd.read_excel(r'Database\\Data.xlsx')

    indices = df.get("Index")
    links = df.get("Link")
    countries = df.get("Country")
    extractWebsite(indices, links, countries, False)


# read data from google sheet
def readGoogleSheet(OS):
    print("Read from Google Sheet...")


    if OS == "mac":
        sa = gspread.service_account("Database//Creds.json")
    if OS == "windows":
        sa = gspread.service_account("Database\\Creds.json")

    sh = sa.open("Data")
    sheet = sh.worksheet("Sheet1")
    indices = sheet.get("A2:A26")
    links = sheet.get("B2:B26")
    countries = sheet.get("C2:C26")

    for i in range(len(indices)):
        extractWebsite(indices[i], links[i], countries[i], True)


# main function

answer = input("Choose your operating system (1-windows/ 2-mac): ")
if int(answer) == 1:
    OS = "windows"
    # readExcel(OS)
    readGoogleSheet(OS)
elif int(answer) == 2:
    OS = "mac"
    readExcel(OS)
    # readGoogleSheet(OS)
else:
    print("This Code Cannot Be Supported by Your Operating System")