import requests
import json

api = "https://reqres.in/api/users?page=2"  # Change the page number to 3

def get_request():
    url = api
    response = requests.get(url)
    
    # Check if the status code is 200 (successful request)
    assert response.status_code == 200
    
    # Convert the response to a Python object (usually a dictionary)
    json_data = response.json()
    
    # Convert the Python object back to a JSON string with indentation for better readability
    json_str = json.dumps(json_data, indent=5)
    
    # Print the formatted JSON string
    print("The returned users for page 2 are:", json_str)
    print("------------")

# Call the function to make the request and display the result
get_request()
