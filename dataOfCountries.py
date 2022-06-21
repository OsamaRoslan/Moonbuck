import csv
import random
import sys
from itertools import permutations
from sys import maxsize

import folium
from folium import plugins

from geopy import Nominatim, distance

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
    randomlist = random.sample(range(0, len(listcountry)), random.randint(6, 10))
    #randomList() = [1, 2, 3, 4, 5, 6]
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


def FindingRoute(list, size):
    index = []
    for s in range(size + 1):
        index.append(s)

    for i in range(len(index)):
        output = getPath(index[i], len(index), list)
    finalpath = output[1]

    print(finalpath)
    return output[1]


def getPath(source, numofvertex, list):
    vertex = []
    for i in range(numofvertex):
        for y in range(numofvertex):
            if y != source:
                vertex.append(y)
        minDistance = maxsize
        next_permutation = permutations(vertex)
        for z in next_permutation:
            path = []
            currentDistance = 0
            x = source
            path.append(source)
            for j in z:
                currentDistance = currentDistance + getDistance(x, j, list)
                x = j
                path.append(j)
            currentDistance = currentDistance + getDistance(x, source, list)
            path.append(source)
            if (currentDistance < minDistance):
                minDistance = currentDistance
                finalpath = path
        return minDistance, finalpath


def getDistance(x, j, list):
    return list[j][x]

def routeName(country, route):
    text = ""
    for x in range(len(route)):
        index = route[x]
        text = text + (country.getShop(index).address + " ---> ")

    print(text)

def getmap(country, route, fileName):
    totalLatitude = 0
    totalLongitude = 0

    for x in range(len(route)-1):
        totalLatitude = totalLatitude + float(country.getShop(x).latitude)
        totalLongitude = totalLongitude + float(country.getShop(x).longitude)

    meanLatitude = totalLatitude / (len(route) - 1)
    meanLongitude = totalLongitude / (len(route) - 1)

    locations = []
    num = (len(route) - 1)

    for i in range(num):
         test = [float(country.getShop(route[i]).latitude), float(country.getShop(route[i]).longitude)]
         if ((i + 1) >= num):
             break

         else:
             loci = [float(country.getShop(route[i]).latitude), float(country.getShop(route[i]).longitude)]

         locations.append(loci)

    secondLast = [float(country.getShop(route[num-1]).latitude), float(country.getShop(route[num-1]).longitude)]
    last = [float(country.getShop(route[num]).latitude), float(country.getShop(route[num]).longitude)]
    locations.append(secondLast)
    locations.append(last)


    my_map = folium.Map(location=[meanLatitude, meanLongitude], zoom_start=14, control_scale=True)

    for i in range(len(locations)):
        if(i == 0):
            folium.Marker(locations[i],icon=folium.Icon(color='black',icon_color='#FFFF00')).add_to(my_map)
        elif(i != (len(locations)-1)):
            folium.Marker(locations[i]).add_to(my_map)

    antpath = plugins.AntPath(locations=locations)
    antpath.add_to(my_map)

    fileName = fileName + ".html"

    my_map.save(fileName)


# code start here
# read dataset of strategic location around the world
file = open('Database\\directory.csv', encoding='utf-8')
type(file)
csvreader = csv.reader(file)

header = []
header = next(csvreader)

AErows = []
CNrows = []
GBrows = []
JProws = []
USrows = []

# filter each country into each array
for row in csvreader:
    if row[7] == "AE":
        AErows.append(row)
    elif row[7] == "CN":
        CNrows.append(row)
    elif row[7] == "GB":
        GBrows.append(row)
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
ENG = Countries("ENGLAND", GBrows)

# Show all graph in each country
usG = USA.getGraph()
jpG = JPN.getGraph()
aeG = UAE.getGraph()
cnG = CHN.getGraph()
egG = ENG.getGraph()

row = len(USA.shops) - 1

print("USA Shop Route")
route = FindingRoute(usG, len(USA.shops) - 1)
routeName(USA,route)
sys.setrecursionlimit(9999999)
getmap(USA,route,"USAmap")

print("\nJapan Shop Route")
route = FindingRoute(jpG, len(JPN.shops) - 1)
routeName(JPN,route)
getmap(JPN,route,"JPNmap")

print("\nUAE Shop Route")
route = FindingRoute(aeG, len(UAE.shops) - 1)
routeName(UAE,route)
getmap(UAE,route,"UAEmap")


print("\nChina Shop Route")
route = FindingRoute(cnG, len(CHN.shops) - 1)
routeName(CHN,route)
getmap(CHN,route,"CHNmap")


print("\nEngland Shop Route")
route = FindingRoute(egG, len(ENG.shops) - 1)
routeName(ENG,route)
getmap(ENG,route,"ENGmap")


