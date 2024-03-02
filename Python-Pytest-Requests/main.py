import requests 

token = 'ae4f59130a043464e87dc03db0f09f2e'

# Создаем тренера POST
response = requests.post(url='https://pokemonbattle.me:9104/trainers/reg', json={
    "trainer_token": token,
    "email": "anna@qa.ru",
    "password": "123qa"
}, headers= {"Content-Type": "application/json"})

print(response) 

# Активируем тренера POST
response_confirm = requests.post(url='https://pokemonbattle.me:9104/trainers/confirm_email', json= {
    "trainer_token": token
}, headers= {"Content-Type": "application/json"})

if response_confirm.status_code == 200:
    print('ok')
else:
    print('bad')


# Создание покемона POST
response_create_pokemon = requests.post(url='https://pokemonbattle.me:9104/pokemons', json= {
    "name": "Принцесса",
    "photo": "https://dolnikov.ru/pokemons/albums/039.png"
}, headers= {"Content-Type": "application/json", "trainer_token": token })

print(response_create_pokemon.text)


# Сохраняем id созданного покемона
pokemon_id = response_create_pokemon.json()['id']

# Смена имени покемона
response_change = requests.put(url='https://pokemonbattle.me:9104/pokemons', 
json= {
    "pokemon_id": pokemon_id,
    "name": "Новое имя"
},
headers= {"Content-Type": "application/json", "trainer_token": token })

print(response_change.text)


# Поймать покемона в покебол
response_add_pokeball = requests.post(url='https://pokemonbattle.me:9104/trainers/add_pokeball',
{
    "pokemon_id": pokemon_id
},
headers= {"Content-Type": "application/json", "trainer_token": token })

print(response_add_pokeball.text)