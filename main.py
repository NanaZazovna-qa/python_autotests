import requests
import json
# Если в коде используется не вся библиотека, а только ее определенные функции,
# то пишется FROM_название_библиотеки IMPORT_название_функции: from requests import requests

token = 'be3b5b9b8832783f0d3f32dbec2b23fd'

# Создаем тренера
response = requests.post('https://pokemonbattle.me:5000//trainers/reg', json={
    "trainer_token": token,
    "email": "nanabaikonur@mail.ru",
    "password": "Nana_1211"
},
    headers={'Content-Type': 'application/json'})

print(response.text)

# Активируем тренера
# Значение ответа может быть не только текст, а статус код, response_activation.status_code

response_activation = requests.post('https://pokemonbattle.me:5000//trainers/confirm_email', json={
    "trainer_token": token
},
    headers={'Content-Type': 'application/json'})

if response_activation.status_code == 200:
    print('OK')
else:
    print('not ok')

# Создаем покемона
response_pokemon = requests.post('https://pokemonbattle.me:5000//pokemons', json={
    "name": "Арканайн",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/a/a8/059Arcanine_AG_anime.png/revision/latest/scale-to-width-down/250?cb=20140902043233.png"
},
    headers={'Content-Type': 'application/json', 'trainer_token': token})
# pokemon_id = response_pokemon.json()['id']
print(response_pokemon.text)

# Изменяем покемона
response_change = requests.put('https://pokemonbattle.me:5000//pokemons', json={
    "pokemon_id": 3211,
    "name": "Арканайн!",
    "photo": ""
},
    headers={'Content-Type': 'application/json', 'trainer_token': token})
print(response_change.text)

# Ловим покемона в покебол
response_add_pokeball = requests.post('https://pokemonbattle.me:5000//trainers/add_pokeball', json={
    "pokemon_id": 3211,
},
    headers={'Content-Type': 'application/json', 'trainer_token': token})
print(response_add_pokeball.text)
