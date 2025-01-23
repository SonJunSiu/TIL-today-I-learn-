from conf import settings
from utils import create_url

k = create_url.create_url (settings.NAME, main_url=settings.MAIN_URL)
print(k)
settings.NAME  

def add (x, y):
    return x + y
print(add(3, 5))