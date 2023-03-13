import ast

def getModelList(filename):
    '''
    解析文件中的所有className
    '''
    with open(filename,'r',encoding='utf-8') as file:
        node = ast.parse(file.read())

    functions = [n for n in node.body if isinstance(n, ast.FunctionDef)]
    classes = [n.name for n in node.body if isinstance(n, ast.ClassDef)]

    for i in functions:
        print(i)
    return classes