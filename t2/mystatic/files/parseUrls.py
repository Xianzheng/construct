import os
from plugin.view_plugin_tools import getDefList
'''
打开或者穿件./out/url.py文件写入关于headers,load library
还包含了urlpatterns = [
'''
def writeUrlLoad():

    oldPath = os.getcwd()
    # print(type(oldPath))
    readPahtString = oldPath + '/' +'plugin'
    readPath = os.chdir(readPahtString)
    lst = os.listdir(readPath)
    newlst = ['.'+i[:-3] for i in lst]
    newlst = [i for i in newlst if i not in ['.__pycach']]
    os.chdir(oldPath)
    # print(newlst)

    with open('./out/urls.py','w',encoding='utf-8') as f:
        f.write('from django.urls import path ,include\n')
        f.write('from .views import *\n')
        for i in newlst:
            f.write('from {} import *\n'.format(i))
        # f.write('from .views_visual import *\n')
        # f.write('from .view_upload import *\n')
        # f.write('from .view_deleteApp import  *\n')
        f.write('urlpatterns = [\n')
        f.close()
'''
打开./draw/drawModels.txt读取所有的model名
存入modelname链表
然后打开或者创建./out/urls.py'写入url信息根据model名
比如model名是tabel1,写入path('table1/',table1_view)到urls.py文件
'''
def writeUrlBody():
    modelnameLst = []
    with open('./draw/drawModels.txt','r',encoding='utf-8') as f:
    
        lst = f.readlines()

        for index in range(len(lst)):
            parselst = lst[index].split(':')
            name = parselst[0]#得到class的名字
            body = parselst[1].replace('\n','')
            modelnameLst.append(name)

        f.close()
    #print(modelnameLst)
    with open('./out/urls.py','a',encoding='utf-8') as f:
        oldPath = os.getcwd()
        deflst = []
        # print(type(oldPath))
        readPahtString = oldPath + '/' +'plugin'
        readPath = os.chdir(readPahtString)
        lst = os.listdir(readPath)
        lst = [i for i in lst if i not in ['__pycache__', 'view_plugin_tools.py']]
        # print(lst)
        for i in lst:
            tempPath = readPahtString + '/'+i
            deflst.extend(getDefList(tempPath))
        os.chdir(oldPath)

        print(deflst)
        for index in range(len(modelnameLst)):

            if index == 0:
                i = modelnameLst[index]
                f.write("    path('{}/',{}),\n".format(i,i+'_view'))
            else:
                
                i = modelnameLst[index]
                f.write("    path('{}/<tableId>',{}),\n".format(i,i+'_view'))
        f.write("    path('addSubTable/<tableId>/<tableModel>',addSubTable_view),\n")
        f.write("    path('updateRow/<modelName>/<rowId>/<tableId>',updateRow_view),\n")
        f.write("    path('deleteRow/<modelName>/<rowId>/<tableId>',deleteRow_view),\n")
        for i in deflst:
            f.write("    path('{}/',{}),\n".format(i[:-5],i))
        # f.write("    path('visual1/',visual1_view),\n")
        # f.write("    path('visual2/',visual2_view),\n")
        # f.write("    path('upload/',upload_view),\n")
        # f.write("    path('getUploadFiles/',getUploadFiles_view),\n")
        # f.write("    path('getAppName/',getAppName_view),\n")
        # f.write("    path('deleteApp/',deleteApp_view),\n")
        f.write(']\n')
        f.close()


'''
运行function
'''
writeUrlLoad()
writeUrlBody()