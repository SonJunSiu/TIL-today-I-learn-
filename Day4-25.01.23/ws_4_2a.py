import requests
from pprint import pprint as print

# 특정 데이터 출력
dummy_data = []
for i in range (1, 11) :
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    response = requests.get(API_URL)
    parsed_data = response.json()
    dummy_data.append(parsed_data['name'])
# API_URL = 'https://jsonplaceholder.typicode.com/users/'
# response = requests.get(API_URL)
# parsed_data = response.json()

# print(parsed_data['name'])
print(dummy_data)


