import requests
import secrets_key



# url = 'https://api.spoonacular.com/food/products/search?query=yogurt&apiKey=API-KEY'

def getRecipeByIngredients(ingredients):
    payload = {
        'fillIngredients': False,
        'ingredients': ingredients,
        'limitLicense': False,
        'number': 5,
        'ranking': 1
    }


    endpoint = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/findByIngredients"


    headers={
        "X-Mashape-Key": secrets_key.Spoonacular_key.API_KEY,
        "X-Mashape-Host": "mashape host"
    }

    r = requests.get(endpoint, params=payload, headers=headers)
    results = r.json()
    title = results[0]['title']
    print(title)

getRecipeByIngredients('apple')