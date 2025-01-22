NAME = 'develper' #settings.py
MAIN_URL = 'http://127.0.0.1:8000'

def create_url(name, main_url, page_num=1):
    new_url = f'{main_url}/{name}?page={page_num}'
    return new_url  #create url.py


result = create_url(NAME, MAIN_URL)

print(result)

