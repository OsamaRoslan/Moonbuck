from geopy.geocoders import Nominatim
import csv
import random
from geopy import distance

geolocator = Nominatim(user_agent="goole maps")


class Shop:
    graph = []

    def __init__(self, country, address, longitude, latitude):
        self.country = country
        self.address = address
        self.latitude = latitude
        self.longitude = longitude

    def getGraph(self):
        print(self.country)
        print(self.graph)


# This class contains the name of the country and some shops in different location
class Countries:
    name = "Name of Contry"
    shops = []
    graph = []

    def __init__(self, country):
        self.name = country

    def listOfShops(self):
        pass

    def getGraph(self):
        pass


def randomList(listcountry):
    # Generate 5 random numbers between 0 and length of country
    randomlist = random.sample(range(0, len(listcountry)), random.randint(6, 10))
    return randomlist


def updateList(listCountry):
    newList = []
    for number in randomList(listCountry):
        newList.append(listCountry[number])
    return newList


# return a list of shops with address, longitude and latitude
def setLocation(lists, country):
    # Shop = [`address`, `longitude`, `latitude`]
    Shops = []

    for list in lists:
        # street`, `city`, `county`, `state`, `country`
        address = str(list[4] + ',' + list[6] + ',' + list[7])
        moonbuck = Shop(country, address, list[11], list[12])
        Shops.append(moonbuck)

    calculateDistance(Shops)
    return Shops


def calculateDistance(shops):
    line = []
    for shop in shops:
        shop1 = (shop.latitude, shop.longitude)
        for x in range(0, len(shops)):
            shop2 = (shops[x].latitude, shops[x].longitude)
            line.append((distance.distance(shop1, shop2)).km)

        shop.graph.append(line)
        # to reset line
        line = []


# read dataset of strategic location around the world
file = open('Database\\directory.csv', encoding='utf-8')
type(file)
csvreader = csv.reader(file)

header = []
header = next(csvreader)

AErows = []
CNrows = []
EGrows = []
JProws = []
USrows = []

# filter each country into each array
for row in csvreader:
    if row[7] == "AE":
        AErows.append(row)
    elif row[7] == "CN":
        CNrows.append(row)
    elif row[7] == "EG":
        EGrows.append(row)
    elif row[7] == "JP":
        JProws.append(row)
    elif row[7] == "US":
        USrows.append(row)
    else:
        pass

file.close()

# in configured units (default miles)

USA = setLocation(updateList(USrows), "USA")
JPN = setLocation(updateList(JProws), "JAPAN")
UAE = setLocation(updateList(AErows), "UAE")
CHN = setLocation(updateList(CNrows), "CHINA")
ENG = setLocation(updateList(EGrows), "ENGLAND")

# Show all graph in each country
print(USA.pop().getGraph())
print(JPN.pop().getGraph())
print(UAE.pop().getGraph())
print(CHN.pop().getGraph())
print(ENG.pop().getGraph())

