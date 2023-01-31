import requests
import pytest


def test_status_code():
    response = requests.get('https://pokemonbattle.me:5000//trainers')
    assert response.status_code == 200


def test_fragment_of_response():
    # Пишем запрос с квери параметром trainer_id
    # приходит отфильтрованная выдача, по нашему параметру
    response = requests.get(
        'https://pokemonbattle.me:5000//trainers', params={'trainer_id': '1972'})
    # и далее мы утверждаем, что в нашем json ключ trainer_name = Nana
    assert response.json()['trainer_name'] == 'Nana'

# Пишем параматезированную функцию
# Указываем какие параметры будем передавать, у меня пара: ключ-значение


@pytest.mark.parametrize('key, value', [('trainer_name', 'Nana')])
def test_p(key, value):
    response = requests.get(
        'https://pokemonbattle.me:5000//trainers', params={'trainer_id': '1972'})
    assert response.json()[key] == value
