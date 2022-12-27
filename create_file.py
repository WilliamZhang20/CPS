import os

def create_file(source_code, prob_info, language, directory):
    # Note: prob_info[0] = full_name, prob_info[1] = category
    if not os.path.isdir('{}/{}'.format(directory, prob_info[1])):
        os.makedirs('{}/{}'.format(directory, prob_info[1]))

    # finding language extension
    if(len(language)>=3 and language[0:3]=='CPP'):
        ext = '.cpp'
    elif(language=='C'):
        ext = '.c'
    elif(len(language)>3 and language[0:4]=='JAVA'):
        ext = '.java'
    elif(len(language)>=2 and language[0:2]=='PY'):
        ext = '.py'
    elif(language=="TEXT"):
        ext = '.txt'
    else:
        ext = '.cpp'
    prob_info[0] = prob_info[0].replace("/", "\\") # corner case: slash confusion
    name = prob_info[0] + ext
    f = open('{}/{}/{}'.format(directory, prob_info[1], name), 'w+', encoding='utf-8')
    f.write(source_code)
    f.close()
