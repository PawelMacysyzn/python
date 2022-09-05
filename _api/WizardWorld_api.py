import requests

url = 'https://wizard-world-api.herokuapp.com/Elixirs?Difficulty=Unknown'

response = requests.get(url)


def rest_API(response):
    if (response.status_code != requests.codes.ok):
        print('Something went wrong')
    else:
        print(response.json())