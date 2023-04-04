import os
import ast
import urllib

def deleteFolderContent(folderPath):
    for root, dirs, files in os.walk(folderPath, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

def removePath(app_name):
    rootPath = os.getcwd()
    print('remove root path')

    app_name = urllib.parse.unquote(app_name)
    
    mainUrlPath = rootPath +'\\'+rootPath.split('\\')[-1]+'\\urls.py'
    
    originlst = []

    with open(mainUrlPath,'r',encoding='utf-8') as f:
        originlst = f.readlines()
    f.close()

    removePath ="path('{}/',include('{}.urls'))".format(app_name,app_name)

    afterRemovelst = [i for i in originlst if removePath not in i]

    afterRemoveString = ''.join(afterRemovelst)

    with open(mainUrlPath,'w',encoding='utf-8') as f:
        f.write(afterRemoveString)
    f.close()

   
    
def unistallApp(app_name):
    rootPath = os.getcwd()
    print('unistall app from settings')

    app_name = urllib.parse.unquote(app_name)
    
    mainSettingsPath = rootPath +'\\'+rootPath.split('\\')[-1]+'\\settings.py'
    
    originlst = []

    with open(mainSettingsPath,'r',encoding='utf-8') as f:
        originlst = f.readlines()
    f.close()

    removePath ="'{}.apps.{}Config'".format(app_name,app_name)

    afterRemovelst = [i for i in originlst if removePath not in i]

    # print(afterRemovelst)
    afterRemoveString = ''.join(afterRemovelst)

    with open(mainSettingsPath,'w',encoding='utf-8') as f:
        f.write(afterRemoveString)
    f.close()

def getDefList(filename):
    '''
    解析文件中的所有className
    '''
    with open(filename,'r',encoding='utf-8') as file:
        node = ast.parse(file.read())

    functions = [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
    classes = [n.name for n in node.body if isinstance(n, ast.ClassDef)]

    # for i in functions:
    #     print(i)
    return functions