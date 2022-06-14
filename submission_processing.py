import itertools
import bs4


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
            # submission.parents is a generator containing a sequential order of all the parents of the submission link. The parent containing the submission id is 5 levels above the submission link.
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
