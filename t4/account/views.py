from django.shortcuts import render,redirect

from django.contrib.auth import login,logout

from django.contrib.auth.models import User, Group

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

from django.contrib.auth import authenticate

from django.http.response import HttpResponse

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

appName = 'app'
import json

import datetime
'''
    API part
'''
# Create your views here.
def test_connect_api(request):
    return HttpResponse(json.dumps({'msg':'Hello'}))

# check if LoginUser exist
def checkIfLogin_api(request):
    if request.method == 'POST':
        # json.loads(request.body.decode('utf-8')) is a dictionary looks like
        # {'data': {'user': 'mark', 'pass': 'a1} in order to make it more simple data = ...[data]
        data = json.loads(request.body.decode('utf-8'))['data']
        # print(data['password'])
        # filter 不能同时查询账号和密码很奇怪
        auth = authenticate(**data)
        if auth != None:
            return HttpResponse(json.dumps({'msg':'login Success'}))
        else:
            return HttpResponse(json.dumps({'msg':'login failed'}))
        #username="john", password="secret"
    return HttpResponse(json.dumps({'msg':'Hello1'}))


'''
    Backend part
'''
def writeToLog(request,string):
    with open('Log.txt','a',encoding= 'utf-8') as f:
        f.write(string)
        f.write('\n')

def getCurrentTime():
    now_time = datetime.datetime.now()
    str_time = datetime.datetime.strftime(now_time,'%Y-%m-%d %H:%M:%S')
    return str_time

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            # return redirect('/dogInfo_list/')
            user = form.get_user()
            login(request,user)

            # if 'next' in request.POST:
            #     return redirect(request.POST.get('next'))
            # else:
            ip = get_client_ip(request)
            print('用户 {} ip {} 登陆'.format(request.user.first_name,ip))
            string = '用户 {} ip {} 时间 {} 登陆 '.format(request.user.first_name,ip,getCurrentTime())
            writeToLog(request,string)
            # return redirect('/{}/table1'.format(appName))#这里必须要127.0.0.1后的完整url
            return redirect('/用水量/table1/?department=产业园')
    else:
        grouplst = Group.objects.all()
        #第一次创建组1，2，3
        if not grouplst:
            Group.objects.get_or_create(name = '1')
            Group.objects.get_or_create(name = '2')
            Group.objects.get_or_create(name = '3')

        if not User.objects.filter(username='admin'):
            user=User.objects.create_superuser("admin","rock@51reboot.com","123456")
            user.set_password("admin")
            new_group = Group.objects.get(name = '3')
            user.groups.add(new_group)
            user.save()
            print('account was created')
        form = AuthenticationForm()
        title = '设备管理分析系统'
        background = 'image/download.jfif'
    return render(request,"login.html",{'form':form,'title':title,'backgroundImage':background})

def logout_view(request):
    
        if request.user:
            logout(request)
        return redirect('/login/')

def changePass_view(request):

    if request.method == 'POST':
        
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # print('it is valid')
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            # messages.success(request, 'Your password was successfully updated!')
            return redirect('/index/')
        else:
            # print('it is not valid')
            return render(request, 'changeError.html')
    
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'changePass.html',{"form":form})

