import os

def create_file(problem_code, source_code, prob_info, lang, directory):
    # prob_info[0] = full_name, prob_info[1] = category
    if not os.path.isdir('{}/{}'.format(directory, prob_info[1])):
        os.makedirs('{}/{}'.format(directory, prob_info[1]))
        print('Created directory {}.'.format(prob_info[1]))

    # finding language extension
    if(len(lang)>=3 and lang[0:3]=='CPP'):
        ext = '.cpp'
    elif(lang=='C'):
        ext = '.c'
    elif(len(lang)>3 and lang[0:4]=='JAVA'):
        ext = '.java'
    elif(len(lang)>=2 and lang[0:2]=='PY'):
        ext = '.py'
    else:
        ext = '.cpp'
    name = prob_info[0] + ext
    print('file: {}'.format(name))
    f = open(f'{directory}/{prob_info[1]}/{name}', 'w+', encoding='utf-8')
    f.write(source_code)
    f.close()
