import json
from urllib import request, parse
from urllib.request import Request

URL_STUB = "https://api.pokemontcg.io/v1/cards/base1-"

'''
Starter Pokemon
Squirtle: 63
Charmander: 46
Bulbasaur: 44
'''
STARTERS = [44, 46, 63] 

'''
Gets json data from Pokemon TCG API.
Retrieves the name of all pokemons from the set.
'''
def getAllPokemon():
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
Retrieves the starter pokemons.
'''
def getStarters():
    starterList = []

    for id in STARTERS:
        URL = URL_STUB + str(id)
        URL = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
        
        response = request.urlopen(URL)
        response = response.read()
        data = json.loads(response)
    
        return data["card"]["name"]


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
Retrieves the pokemon based on the ID.
'''
def getPokemon(id):
    URL = URL_STUB + str(id)
    URL = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
        
    response = request.urlopen(URL)
    response = response.read()
    data = json.loads(response)

    return data["card"]["name"] 

'''
Retrieves the id of the inputed pokemon.
'''
def getID(pokemon):
    for i in range(1, 70):
        URL = URL_STUB + str(i)
        URL = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
        
        response = request.urlopen(URL)
        response = response.read()
        data = json.loads(response)

        if (pokemon == data["card"]["name"]):
            return data["card"]["id"]


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

        
#print(getAllPokemon())
print(getStarters())
print(getID("Alakazam"))
print(getHP("Alakazam"))
print(getImage("Alakazam"))
