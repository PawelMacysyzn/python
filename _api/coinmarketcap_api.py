import json
import requests
import secrets_key

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': secrets_key.API_KEY,
}


response = requests.get(url, headers=headers)


if (response.status_code != requests.codes.ok):
    print('Error!')
else:
    # print(response.status_code)
    print(json.dumps(response.json(), indent=2))
