import requests

BASE = 'http://127.0.0.1:5000/'

# response = requests.put(BASE + 'video/23', {'name': 'Hugo', 'likes': 10, 'views': 1200})
# print(response.json())

# input()

response = requests.get(BASE + 'video/243')
print(response.json())