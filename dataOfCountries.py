from geopy.geocoders import Nominatim
import csv
import random
from geopy import distance

geolocator = Nominatim(user_agent="google maps")


class Shop:
    def __init__(self, country, address, longitude, latitude):
        self.country = country
        self.address = address
        self.latitude = latitude
        self.longitude = longitude

    def getGraph(self):
        print("! ", self.country)
        print("! ", self.graph, "\n")
        return self.graph


# This class contains the name of the country and some shops in different location
class Countries:
    shops = []
    graph = []

    def __init__(self, nameofcountry, countrydetails):
        self.name = nameofcountry
        self.rows = countrydetails
        # short-listed shop based on random list
        self.shops = setLocation(updateList(countrydetails), nameofcountry)
        self.graph = setGraph(self.shops)

    def getShop(self, index):
        return self.shops[index]

    def getGraph(self):
        print("!\n! Graph for ", self.name, " :")
        for x in range(len(self.graph)):
            print("! ", x, " - ", self.graph[x])
        return self.graph


def randomList(listcountry):
    # Generate 5 random numbers between 0 and length of country
    # randomlist = random.sample(range(0, len(listcountry)), random.randint(6, 10))
    randomlist = [1, 2, 3, 4, 5, 6]
    return randomlist




def updateList(listCountry):
    newlist = []
    turn = randomList(listCountry)
    for x in range(len(turn)):
        newlist.append(listCountry[turn[x]])
    return newlist


# return a list of shops with address, longitude and latitude
def setLocation(lists, country):
    # Shop = [`address`, `longitude`, `latitude`]
    Shops = []

    for list in lists:
        # street`, `city`, `county`, `state`, `country`
        address = str(list[4] + ',' + list[6] + ',' + list[7])
        moonbuck = Shop(country, address, list[11], list[12])
        Shops.append(moonbuck)
    return Shops


def setGraph(shop):
    graph = []
    temp = []
    for x in range(len(shop)):
        shop1 = (shop[x].latitude, shop[x].longitude)
        for y in range(len(shop)):
            shop2 = (shop[y].latitude, shop[y].longitude)
            temp.append((distance.distance(shop1, shop2)).km)
        graph.append(temp)
        # to reset the temp array
        temp = []
    return graph


# code start here
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

# USA = setLocation(updateList(USrows), "USA")
USA = Countries("USA", USrows)
JPN = Countries("JAPAN", JProws)
UAE = Countries("UAE", AErows)
CHN = Countries("CHINA", CNrows)
ENG = Countries("ENGLAND", EGrows)

# Show all graph in each country
usG = USA.getGraph()
jpG = JPN.getGraph()
aeG = UAE.getGraph()
cnG = CHN.getGraph()
egG = ENG.getGraph()

