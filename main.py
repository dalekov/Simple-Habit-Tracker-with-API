import requests
from datetime import datetime

USERNAME = "denisalekov1"
TOKEN = "dqkjdsmxqspoqsl"



pixela_endpoint = "https://pixe.la/v1/users"

# Creating an account:
params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=params)
# print(response.text)

# # Creating a graph:
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
graph_params = {
    "id": "test-graph-2",
    "name": "Steps Per Day", ## Leave this dict in for the pixel endpoint
    "unit": "steps",
    "type": "int",
    "color": "shibafu",
}
#
graph_headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=graph_headers)
# print(response.text)

# Adding a pixel to the graph:
date = input("What date? (yyyyMMdd): ")
quantity = input("How many steps did you manage?: ")

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}"
pixel_header = {
    "X-USER-TOKEN": TOKEN,
}
pixel_params = {
    "date": date,
    "quantity": quantity
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=pixel_header)
print(response.text)

# Updating a pixel:
date = input("Which date would you like to update? (yyyyMMdd): ")
steps = input("What is the updated data?: ")

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}/{date}"

response = requests.put(url=update_endpoint, json={"quantity": steps}, headers=graph_headers)
print(response.text)

# Deleting a pixel:
delete_date = input("Which date would you like to delete? (yyyyMMdd): ")
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}/{date}"

response = requests.delete(url=delete_endpoint, headers=graph_headers)
print(response.text)


