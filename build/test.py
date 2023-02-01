with open('./settings.py','r') as f:
    content = f.readlines()
    index = content.index('INSTALLED_APPS = [\n') + 7
    content.insert(index,'    \'account\',\n')
    with open('./test1.py','w') as f1:
        f1.write(''.join(content))