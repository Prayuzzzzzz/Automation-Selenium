import requests
import json

api = "https://reqres.in/api/users"

def get_request():
    url = api
    response = requests.get(url)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data,indent=5)
    print("the returned users for the api are:",json_str)
    print("------------")

get_request() 
