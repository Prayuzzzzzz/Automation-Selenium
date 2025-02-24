import requests
import json

api = "https://reqres.in/api"

authorization_token = "token ....any _token"

def post_request():
    url = api + "/users/"
    headers = {"Authorization": authorization_token}
    data = {
            "name": "John",
            "job": "QA tester",
            "email": "john@mail.com"
        }
       
    response = requests.post(url, json=data, headers=headers)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    assert response.status_code==201
    user_id =json_data["id"]
    print("The new users posted for the api are:",json_str)
    print("-----------------------------------")
    print("the Id for new users is:",user_id)


post_request()
