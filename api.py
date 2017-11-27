import requests, urllib
RECIPE_ID = "43ed9009"
NUTRITION_ID = "cce11d0a"
RECIPE_API_KEY = "5d20a3cad3a3ca33ed748a1a016b3ad4	—"
NUTRITION_API_KEY = "a5e95201b7bb5dbbd8c85854076ac38f	—"
BASE_URL = "https://api.edamam.com/"

def searchFood(data):
    url = BASE_URL + "search"
    data["api_id"] = RECIPE_ID
    data["api_key"] = RECIPE_API_KEY
    return requests.get(url, params=data).json()
    pass

def recipe(ref):
    stub = 'http://www.edamam.com/ontologies/edamam.owl#'
    stub += ref
    url = BASE_URL + "search"
    data = {}
    data["r"] = stub
    data["api_id"] = RECIPE_ID
    data["api_key"] = RECIPE_API_KEY
    res = requests.get(url, params=data)
    return res.json()[0]