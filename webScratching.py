import requests
from bs4 import BeautifulSoup

url = "https://www.heritage.org/index/country/japan"
# Make a request
page = requests.get(url)
doc = BeautifulSoup(page.text, 'html.parser')

text = "Title: " + doc.title.text + "\n\n"

for x in range(len(doc.body.findAll("p"))):
    text += str(doc.body.findAll("p")[x].text)
    text += "\n"

with open('Data.txt', 'w') as f:
   f.write(text)

