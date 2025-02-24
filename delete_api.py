import requests
import json

api = "https://reqres.in/api"

authorization_token = "token ....any _token"

def delete_request(user_id):
    url = api + "/users/{user_id}"
    headers = {"Authorization": authorization_token}
    
       
    response = requests.delete(url, headers=headers)
    assert response.status_code==204

    print("The users are deleted successfully:",user_id)
    print("-----------------------------------")
    print("user deleted successfully")


delete_request(2)
