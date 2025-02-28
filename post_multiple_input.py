import requests
import json

api = "https://reqres.in/api"

authorization_token = "token ....any _token"

def post_request(user_names):
    url = api + "/users/"
    headers = {"Authorization": authorization_token}
    user_ids = []

    for name in user_names:
        data = {
            "name": name,
            "job": "QA tester"
        }
        response = requests.post(url, json=data, headers=headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("The new user posted for the api are:",json_str)
        print("-----------------------------------")
        user_id = json_data.get("id")
        print("the Id for new users is:",user_id)

        if user_id:
            user_ids.append(user_id)
            assert response.status_code==201
            assert "name" in json_data
            print("-----Post multiple user is success---",name)
    return user_ids


#user_name_examples and function call
user_names = ["Ram ", "Shayam","hari"]
user_ids = post_request(user_names)
print("Created user ids are:",user_ids)