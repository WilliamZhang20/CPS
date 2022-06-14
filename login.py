import requests


def login(username, password):

    # a session object will persist all cookies across requests
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
