from venv import create
import requests
import bs4
import itertools
import os
from dotenv import load_dotenv


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


def solved_problems(username, session):

    response = session.get(f'https://dmoj.ca/api/user/info/{username}').json()
    problem_list = response['solved_problems']

    return problem_list


def best_submission(username, problem_code, session):

    page_number = 1

    while True:
        response = session.get(
            f'https://dmoj.ca/problem/{problem_code}/rank/{page_number}')

        if response.status_code == 404:
            break

        soup = bs4.BeautifulSoup(response.text, 'lxml')
        submission = soup.find('a', string=username)

        if(submission):
            # submission.parents is a generator containing a sequential order of all the parents of the submission link. The parent div containing the submission id is 5 levels above the submission link.
            # islice will return a new generator from index 4 to the end
            # calling next() on the sliced iterator will return the links 5th parent, as it is now the first element to be yielded

            submission_id = next(itertools.islice(
                submission.parents, 4, None))['id']
            return submission_id

        page_number += 1


def process_submission(submission_id, session):
    response = session.get(f'https://dmoj.ca/src/{submission_id}')
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    source_code = soup.find('code').text
    return source_code


def create_file(problem_id, source_code):
    f = open(f'{problem_id}.cpp', 'w+')
    f.write(source_code)
    f.close()


load_dotenv()

DMOJ_USERNAME = os.getenv('DMOJ_USERNAME')
DMOJ_PASSWORD = os.getenv('DMOJ_PASSWORD')

session = login(DMOJ_USERNAME, DMOJ_PASSWORD)

problem_list = solved_problems(DMOJ_USERNAME, session)


submission_id = best_submission(DMOJ_USERNAME, 'coci14c1p6', session)
source_code = process_submission(submission_id, session)

create_file('coci14c1p6', source_code)
