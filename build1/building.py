import os
from tools import *
import shutil
from glob import glob
import time
import sys
appName = 'app'

# print(currentPath)
# print(previousPath)
# print(projectPath)
# print(projectMainPath)
def createApp(appName):
    #切换到项目目录
    os.chdir(projectPath)
    #如果没有创建过就创建app
    print(os.getcwd())
    if not os.path.isdir(appName):
        os.system('python manage.py startapp '+appName)
    

    # 切换至生成项目目录
    os.chdir(currentPath)
    #运行parsing 文件生成app 所需文件
    os.system('python parseModel.py')
    os.system('python parseForm.py')
    os.system('python parseUrls.py')
    os.system('python parseView.py')
    os.system('python tools.py')

    #迁移out文件进入app
    coped_fileName = './out/'
    mycopy('./{}/'.format(coped_fileName),'../{}/{}/'.format(projectName,appName))

    #迁移plugin文件进入app
    coped_fileName = './plugin/'
    mycopy('./{}/'.format(coped_fileName),'../{}/{}/'.format(projectName,appName))

    #配置url到mainUrl,切换到项目的主url
    os.chdir(projectMainPath)
    added_url = "path('{}/',include('{}.urls')),".format(appName,appName) 
    addUrlToMainUrl(added_url)

    #配置setting,在settings的INSTALL_APP中导入App
    added_app = '\'{}\','.format(appName)
    addAppToInstall(added_app)

    #在app中装入template
    
    os.chdir(currentPath)
    #复制building的template的所有文件到project app的 templates中
    # mycopy('./{}/'.format(coped_fileName),'../{}/{}/{}/'.format(projectName,appName,coped_fileName))
    mycopyAndPaste(currentPath +'/templates',projectPath+'/{}/templates'.format(appName))

def addUrlToMainUrl(added_url):
    #添加added_urls到main project的urls.py的urlpatterns中
    added_filePath = './urls.py'
    add_to_path = './urls.py'
    addAppurlsToProjectUrls(added_filePath,added_url,add_to_path)

def addAppToInstall(added_app):
    #添加added_app到main project的settings的INSTALLED_APPS中
    added_filePath = './settings.py'
    add_to_path = './settings.py'
    addAppToSetting(added_filePath,added_app,add_to_path)

def createProject():
    os.chdir(previousPath) #cmd切换到上一层目录
    #创建一个新的django project
    os.system('django-admin startproject '+projectName)
    #复制模板setting到 project中
    shutil.copy(currentPath+'./settings.py',projectMainPath+'./settings.py') 
    os.chdir(currentPath)
    #复制building的mystatic的所有文件和文件夹内的内容到project的 mysstatic中
    mycopyAndPaste(currentPath +'/mystatic',projectPath+'/mystatic')
    os.chdir(projectMainPath)
    #修改setting中的projectName
    changeContent('./settings.py','appbackend',projectName)

def migrateAccount():
    '''
    迁移account进入项目
    '''
    #复制building的account的所有文件和文件夹内的内容到project的 account中
    os.chdir(currentPath)
    mycopyAndPaste(currentPath +'/account',projectPath+'/account')
    #配置url到mainUrl
    os.chdir(projectMainPath)
    added_url = "path('',include('{}.urls')),".format('account') 
    addUrlToMainUrl(added_url)
    #装载account到setting
    os.chdir(projectMainPath)
    #加入'account', 导Installed App
    added_app = '\'account\','
    addAppToInstall(added_app)


    
if __name__ == '__main__':
    projectName = sys.argv[1]
    currentPath = os.getcwd()#当前目录页】
    previousPath = '\\'.join(currentPath.split('\\')[:-1])#上一层目录
    projectPath = previousPath+'\{}'.format(projectName)#生成项目目录
    projectMainPath = projectPath +'\{}'.format(projectName)
    appName = 'app'

    createProject()

    migrateAccount()

    #在django project中创建app，在app中写入template文件夹，由parsing文件填入内容，并在setting的installed app装上，应该就可以用了
    #app为根app
    createApp('app')
    #指定登陆后的appName
    addCodeToFile(filePath=currentPath +'/account/views.py',index=20,add_content="appName = {}\n".format('\''+appName+'\''))
    
    os.chdir(projectPath)
    os.system('python manage.py makemigrations')
    os.system('python manage.py migrate')
    os.system('python manage.py runserver')