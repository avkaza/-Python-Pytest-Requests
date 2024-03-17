import requests
import pytest

HOST = 'https://pokemonbattle.me:9104'

# Проверяем, что ответ запроса get/pokemons приходит с кодом 200
def test_status_code():
    response = requests.get(url= f'{HOST}/pokemons')
    assert response.status_code == 200

# Проверяем, что ответ запроса get/trainers приходит с кодом 200
def test_status_code_trainers():
    response = requests.get(url= f'{HOST}/trainers')
    assert response.status_code == 200


# Проверяем, что в ответе приходит строчка с именем моего тренера 
def test_trainer_id():
     id= requests.get(url= f'{HOST}/trainers', params = {'trainer_id': 974})
     
     assert id.json()['trainer_name']=='Lionne'
