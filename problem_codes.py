def solved_problems(username, session):

    response = session.get('https://dmoj.ca/api/v2/user/{}'.format(username)).json()
    problem_list = response['data']['object']['solved_problems']

    return problem_list
