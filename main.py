import requests
import bs4
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


def solved_problems(username, session):

    response = session.get(f'https://dmoj.ca/api/user/info/{username}').json()
    problem_list = response['solved_problems']

    return problem_list


def best_submission(problem_code, session):

    page_number = 1

    while True:
        response = session.get(
            f'https://dmoj.ca/problem/{problem_code}/rank/{page_number}')

        if response.status_code == 404:
            break

        soup = bs4.BeautifulSoup(response.text, 'lxml')
        submission = soup.find('a', string=DMOJ_USERNAME)

        if(submission):
            print(submission, page_number)
            return

        page_number += 1


def process_submission(submission_id, session):
    response = session.get(f'https://dmoj.ca/src/{submission_id}')
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    source_code = soup.find('code').text


load_dotenv()

DMOJ_USERNAME = os.getenv('DMOJ_USERNAME')
DMOJ_PASSWORD = os.getenv('DMOJ_PASSWORD')

session = login(DMOJ_USERNAME, DMOJ_PASSWORD)

problem_list = solved_problems(DMOJ_USERNAME, session)
