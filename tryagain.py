import requests

# API endpoint for deleting a user (example: user ID 2)
api_url = "https://reqres.in/api/users/2"

# Send DELETE request
response = requests.delete(api_url)

# Check response
if response.status_code == 204:
    print("User deleted successfully!")
else:
    print(f"Failed to delete. Status Code: {response.status_code}, Response: {response.text}")
