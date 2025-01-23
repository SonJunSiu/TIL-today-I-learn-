import requests
from pprint import pprint as print

# 특정 데이터 출력
dummy_data = []
for i in range (1, 11) :
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    response = requests.get(API_URL)
    parsed_data = response.json()
    # print(response)
    # print(parsed_data)

    lat = float(parsed_data['address']['geo']['lat'])
    lng = float(parsed_data['address']['geo']['lng'])

    if -80 < lat < 80 and - 80 < lng < 80  :
        user_info = {
        'name' : parsed_data['name'],
        'lat' : lat,
        'lng' : lng,
        'company_name' : parsed_data['company']['name']
    }
        dummy_data.append(user_info)
print(dummy_data)


