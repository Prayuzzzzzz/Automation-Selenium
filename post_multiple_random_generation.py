import requests
import json
import random
import string

api = "https://reqres.in/api"

authorization_token = "token ....any _token"

def generate_random_email():
    domain = "automate.com"
    email_length = 5
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email

def post_request():
    url = api + "/users/"
    headers = {"Authorization": authorization_token}
    data = {
            "name": "Test",
            "job": "QA tester",
            "email": generate_random_email()
        }
    response = requests.post(url, json=data, headers=headers)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    assert response.status_code == 201
    print("The new user posted for the api are:",json_str)
    print("-----------------------------------")
    user_id = json_data.get("id")
    print("the Id for new users is:",user_id)

for _ in range(15):
    newuser = post_request()