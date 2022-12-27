import itertools
import bs4


def get_submission(username, problem_code, session):
    # searches for latest submission for yourself only on that problem
    response = session.get('https://dmoj.ca/problem/{}/submissions/{}/?status=AC'.format(problem_code, username))

    if response.status_code == 404:
        return

    soup = bs4.BeautifulSoup(response.text, 'lxml')
    submission = soup.find('a', string=username)
    language = soup.find('span', {"class": "language"}).text

    if(submission):
        # submission.parents is a generator containing a sequential order of all the parents of the submission link. The parent containing the submission id is 5 levels above the submission link.
        # islice will return a new generator from index 4 to the end
        # calling next() on the sliced iterator will return the links 5th parent, as it is now the first element to be yielded

        submission_id = next(itertools.islice(submission.parents, 4, None))['id']
        submission_info = [submission_id, language]
        return submission_info


def process_submission(submission_id, session):
    response = session.get('https://dmoj.ca/src/{}'.format(submission_id))
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    source_code = soup.find('code').text
    return source_code

def find_problem_info(problem_code, session):
    response = session.get('https://dmoj.ca/api/v2/problem/{}'.format(problem_code)).json()
    category = response['data']['object']['group']
    full_name = response['data']['object']['name']
    prob_info = [full_name, category]
    return prob_info
