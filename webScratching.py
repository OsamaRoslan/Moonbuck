import requests
from bs4 import BeautifulSoup


# Extract the link and the name country of the websites from text file
def openWebsite(input, i):
    line = input.split(", ")
    index = i % 5
    Web = Website(line[0], line[1].replace("\n", "") + str(index))
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


# main
with open('Data.txt') as f:
    lines = f.readlines()
count = 0
for line in lines:
    count += 1
    openWebsite(line, count)
