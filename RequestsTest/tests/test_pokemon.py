import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER={'Content-Type':'application/json','trainer_token':'6ae9e1b15c50fa5fb53e1a6f7e0d4b31'}

def test_gef_trainers():
    response=requests.get(f'{URL}/trainers',params={'trainer_id':4437},timeout=5)
    assert response.status_code==200,'Unexpested status code'
    assert response.json()['trainer_name']=="Zamaza", ''