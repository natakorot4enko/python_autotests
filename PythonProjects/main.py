import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '1a16960dd9b4cf78efa4aedfc241a6dd'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

body = {
    "name": "Бульбазавр",
    "photo_id": 1
}

responce = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body)
print (responce.text)

pokemon_id2 = responce.json() ['id']

body_change = {
    "pokemon_id" : pokemon_id2,
    "name": "Герой",
    "photo_id": 2
}

responce_change = requests.put (url = f'{URL}/pokemons', headers=HEADER, json= body_change)
print (responce_change.text)

body_pokeball = {
    "pokemon_id": pokemon_id2,
}
responce_pokeball = requests.post (f'{URL}/trainers/add_pokeball', headers=HEADER, json= body_pokeball)
print(responce_pokeball.text)