import requests

BASE = 'http://127.0.0.1:5000/'

data = [{'name': 'Hugo', 'likes': 10, 'views': 1200},
        {'name': 'How to make rest api', 'likes': 78, 'views': 8000},
        {'name': 'Joe', 'likes': 35, 'views': 2200}]

for i in range(len(data)):
    response = requests.put(BASE + 'video/' + str(i), data[i])
    print(response.json())

input()
response = requests.get(BASE + 'video/2')
print(response.json())

input()
response = requests.patch(BASE + 'video/2', {'views': 99})
print(response.json())

input()
response = requests.delete(BASE + 'video/0')
print(response)
