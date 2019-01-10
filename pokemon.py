import json
from urllib import request, parse
from urllib.request import Request

URL_STUB = "https://api.pokemontcg.io/v1/cards/base1-"

'''
Gets json data from Pokemon TCG API.
Retrieves the name of all pokemons from the set.
'''
def getPokemon():
    pokeList = []
    for i in range(1, 70):
        URL = URL_STUB + str(i)
        URL = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
        
        response = request.urlopen(URL)
        response = response.read()
        data = json.loads(response)

        #print(data["card"]["name"])
        pokeList.append(data["card"]["name"])

    return pokeList

'''
Retrieves the hp of the inputed pokemon.
'''
def getHP(pokemon):
    for i in range(1, 70):
        URL = URL_STUB + str(i)
        URL = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
        
        response = request.urlopen(URL)
        response = response.read()
        data = json.loads(response)

        if (pokemon == data["card"]["name"]):
            return data["card"]["hp"]

'''
Retrieves the image of the inputed pokemon
'''
def getImage(pokemon):
    for i in range(1, 70):
        URL = URL_STUB + str(i)
        URL = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
        
        response = request.urlopen(URL)
        response = response.read()
        data = json.loads(response)

        if (pokemon == data["card"]["name"]):
            return data["card"]["imageUrl"]

        
print(getPokemon())
print(getHP("Alakazam"))
print(getImage("Alakazam"))