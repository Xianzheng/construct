
# srcfile 需要复制、移动的文件   
# dstpath 目的地址
 
import os
import shutil
from glob import glob
 
def mycopyfile(srcfile,dstpath):                       # 复制函数
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(srcfile)             # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)                       # 创建路径
        shutil.copy(srcfile, dstpath + fname)          # 复制文件
        # print ("copy %s -> %s"%(srcfile, dstpath + fname))
 

src_dir = './out/'
dst_dir = './application/testapp/'                                    # 目的路径记得加斜杠
                   # glob获得路径下所有文件，可根据需要修改

def mycopy(src_dir,dst_dir):
    print(src_dir)
    print(dst_dir)
    src_file_list = glob(src_dir + '*') 
    for srcfile in src_file_list:
        print(srcfile)
        mycopyfile(srcfile, dst_dir)
# mycopyfile('./out/*', './application/testapp/')

def addAppToSetting(added_filePath,added_app,add_to_path):
    print('add app',added_app)
    
    with open(added_filePath,'r',encoding='utf-8') as f:
        content = f.readlines()
        index = content.index('INSTALLED_APPS = [\n') + 7
        
        content.insert(index,'    {}\n'.format(added_app))
        with open(add_to_path,'w',encoding='utf-8') as f1:
            f1.write('')
            f1.write(''.join(content))
            f1.close()
    f.close()


    

def addAppurlsToProjectUrls(added_filePath,added_app,add_to_path):
    with open(added_filePath,'r',encoding='utf-8') as f:
        content = f.readlines()
        index = content.index('urlpatterns = [\n') + 2
        if 'from django.urls import path\n' in content:
            index1 = content.index('from django.urls import path\n')
            content[index1] = 'from django.urls import path,include\n'
        content.insert(index,'    {}\n'.format(added_app))
        with open(add_to_path,'w',encoding='utf-8') as f1:
            f1.write(''.join(content))
            f1.close()
    f.close()

def readFileParseToList(filePath) -> list:
    '''
    读文件传入文件路径
    传出一个链表包含文件的所有信息
    '''
    content = []
    with open(filePath,'r',encoding='utf-8') as f:
        content =  f.readlines();
        
        f.close()
    
    return content

def addCodeToFile(filePath:str,index:int,add_content:str):
    '''
    把add_content 加入进fileName的index行
    '''
    content = readFileParseToList(filePath)

    # print(content)
    content.insert(index,add_content)

    string = ''.join(content)

    with open(filePath,'w',encoding='utf-8') as f:
        f.write(string)
    
    f.close()

# addCodeToFile('./test1.py',12,"appName = 'a'\n")
def changeContent(filePath:str,old:str,new:str):
    '''
    替换一个文件里的所有内容
    '''
    content = readFileParseToList(filePath=filePath)

    content = ''.join(content)

    content = content.replace(old,new)

    with open(filePath,'w',encoding='utf-8') as f:

        f.write(content)

    f.close()

def addUrlToMainUrl(added_url:str):
    '''
        added_url是指添加进MainUrl的内容
    '''
    added_filePath = './urls.py'
    add_to_path = './urls.py'
    addAppurlsToProjectUrls(added_filePath,added_url,add_to_path)


def addAppToInstall(added_app):
    '''
    #添加added_app到main project的settings的INSTALLED_APPS中
    '''
    added_filePath = './settings.py'
    add_to_path = './settings.py'
    addAppToSetting(added_filePath,added_app,add_to_path)



