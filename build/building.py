import os
from tools import mycopy, addAppToSetting, addAppurlsToProjectUrls
from bs import mycopyAndPaste
import shutil
from glob import glob
import time
projectName = 'application' #项目名
currentPath = os.getcwd()#当前目录页】
previousPath = '\\'.join(currentPath.split('\\')[:-1])#上一层目录
projectPath = previousPath+'\{}'.format(projectName)#生成项目目录
projectMainPath = projectPath +'\{}'.format(projectName)
appName = 'app1'
if __name__ == '__main__':
    os.chdir(previousPath) #cmd切换到上一层目录

    #创建一个新的django project

    os.system('django-admin startproject '+projectName)

    #复制模板setting到 project中
    shutil.copy(currentPath+'./settings.py',projectMainPath+'./settings.py') 


    #在django project中创建app，在app中写入template文件夹，由parsing文件填入内容，并在setting的installed app装上，应该就可以用了


    os.chdir(projectPath)#切换到项目目录

    if not os.path.isdir(appName):#如果没有创建过就穿件app
        os.system('python manage.py startapp '+appName)

    os.chdir(currentPath)# 切换至生成项目目录

    #运行parsing 文件生成app 所需文件
    os.system('python parseModel.py')
    os.system('python parseForm.py')
    os.system('python parseUrls.py')
    os.system('python parseView.py')
    os.system('python tools.py')

    #迁移out文件进入app
    coped_fileName = './out/'
    mycopy('./{}/'.format(coped_fileName),'../{}/{}/'.format(projectName,appName))

    #在项目的urls.py中绑定app的urls.py

    os.chdir(projectMainPath)#切换到项目的主url

    #添加account url
    added_filePath = './urls.py'
    added_url = "path('',include('{}.urls')),".format('account') 
    add_to_path = './urls.py'
    addAppurlsToProjectUrls(added_filePath,added_url,add_to_path)

    # 添加appUrl
    added_filePath = './urls.py'
    added_url = "path('{}/',include('{}.urls')),".format(appName,appName) 
    add_to_path = './urls.py'
    addAppurlsToProjectUrls(added_filePath,added_url,add_to_path)


    os.chdir(projectMainPath)
    # add account to main setting
    added_filePath = './settings.py'
    added_app = '\'account\','
    add_to_path = './settings.py'
    addAppToSetting(added_filePath,added_app,add_to_path)

    #等待一秒在读写
    #add app to main setting

    added_filePath = './settings.py'
    added_app = '\'app1\','
    add_to_path = './settings.py'
    addAppToSetting(added_filePath,added_app,add_to_path)

    #写入template

    os.chdir(projectPath+'/{}'.format(appName))#切换到项目目录

    if not os.path.isdir('templates'):#如果没有创建过就穿件app
        os.makedirs('templates')

    coped_fileName = 'templates'
    os.chdir(currentPath)
    mycopy('./{}/'.format(coped_fileName),'../{}/{}/{}/'.format(projectName,appName,coped_fileName))

    print(currentPath)
    print(projectPath)
    mycopyAndPaste(currentPath +'/account',projectPath+'/account')
    mycopyAndPaste(currentPath +'/mystatic',projectPath+'/mystatic')

    os.chdir(projectPath)
    os.system('python manage.py makemigrations')
    os.system('python manage.py migrate')
    os.system('python manage.py runserver')