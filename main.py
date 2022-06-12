import requests
import os
from dotenv import load_dotenv


def login(username, password):

    s = requests.Session()
    r = s.get('https://dmoj.ca/accounts/login/?next=/user')
    csrf_token = r.cookies['csrftoken']

    data = {
        'username': username,
        'password': password,
        'csrfmiddlewaretoken': csrf_token,
        'next': '/user'
    }

    headers = {'referer': 'https://dmoj.ca/accounts/login/?next='}

    s.post('https://dmoj.ca/accounts/login/?next=',
           data=data, headers=headers)

    return s


load_dotenv()

DMOJ_USERNAME = os.getenv('DMOJ_USERNAME')
DMOJ_PASSWORD = os.getenv('DMOJ_PASSWORD')

session = login(DMOJ_USERNAME, DMOJ_PASSWORD)
