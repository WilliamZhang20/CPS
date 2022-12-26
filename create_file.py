def create_file(problem_code, source_code, prob_info, language, directory):
    # prob_info[0] = full_name, prob_info[1] = category
    if not os.path.isdir(f'{directory}\{prob_info[1]}'):
        os.makedirs(f'{directory}\{prob_info[1]}')
        print('Created directory {}.'.format(prob_info[1]))

    # finding language extension
    if(language.len()>=3 and language[0:3]=='CPP'):
        ext = '.cpp'
    elif(language=='C'):
        ext = '.c'
    elif(language.len()>3 and language[0:4]=='JAVA'):
        ext = '.java'
    elif(language.len()>=2 and language[0:2]=='PY'):
        ext = '.py'
    else:
        ext = '.cpp'
    name = prob_info[0] + ext
    print('file: {}'.format(name))
    #f = open(f'{directory}\{prob_info[1]}\{name}', 'w+', encoding='utf-8')
    #f.write(source_code)
    #f.close()
