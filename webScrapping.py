import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import gspread
import pandas as pd
from bs4 import BeautifulSoup

OS = ""


# Extract the link and the name country of the websites from text file
def extractWebsite(indices, links, countries, sheet):
    if sheet:
        for index in indices:
            # links = [[url]]
            # create object Website(links, name of text file)
            Web = Website(links[0], "Data" + index)
            Web.createText()
    else:
        for index in indices:
            Web = Website(links[int(index) - 1], "Data" + index)
            Web.createText()


# Extract word from website
class Website:
    # instance attributes
    def __init__(self, url, name):
        self.url = url
        self.name = name

    def createText(self):
        # Make a request from website for its html
        page = requests.get(self.url)
        # module for web scrapping
        doc = BeautifulSoup(page.text, 'html.parser')
        try:
            text = "Title: " + doc.title.text
        except:
            text = ""
            print("! No Title Found!!")
        print("!")
        # find paragraph in the html
        for x in range(len(doc.body.findAll("p"))):
            line = str(doc.body.findAll("p")[x].text).replace("\n", " ")
            if line != "":
                text += line
                text += "\n"
            else:
                pass

        # address for text file
        self.name = "Data file\\" + self.name + ".txt"
        print("! Creating file at: ", self.name)
        # Writing the contents of website in the text file
        with open(self.name, 'w', encoding="utf-8") as f:
            f.write(text)


# read data from excel
def readExcel(OS):
    print("! Read from Excel...")
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
    print("! Read from Google Sheet...")

    # Credential for extracting the data
    if OS == "mac":
        sa = gspread.service_account("Database//Creds.json")
    if OS == "windows":
        sa = gspread.service_account("Database\\Creds.json")

    sh = sa.open("Data")
    sheet = sh.worksheet("Sheet1")
    indices = sheet.get("A2:A26")
    links = sheet.get("B2:B26")
    countries = sheet.get("C2:C26")

    # extract website by line
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
    print("! This Code Cannot Be Supported by Your Operating System")
