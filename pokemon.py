import json
from urllib import request, parse

URL_STUB = "https://api.pokemontcg.io/v1/cards/base1-"

def getPokemon():
    for i in range(1, 70):
        URL = URL_STUB + str(i)

        response = request.urlopen(URL)
        response = response.read()
        data = json.loads(response)

        
