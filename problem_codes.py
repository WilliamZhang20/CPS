def solved_problems(username, session):

    response = session.get(f'https://dmoj.ca/api/v2/user/{username}').json()
    problem_list = response['data']['object']['solved_problems']

    return problem_list
