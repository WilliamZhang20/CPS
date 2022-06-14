def create_file(problem_code, source_code, directory):
    f = open(f'{directory}\{problem_code}.cpp', 'w+', encoding='utf-8')
    f.write(source_code)
    f.close()
