"""t2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('产业园_二分厂/',include('产业园_二分厂.urls')),
    path('产业园_一分厂/',include('产业园_一分厂.urls')),
    path('综合楼/',include('综合楼.urls')),
    path('赤壁子公司/',include('赤壁子公司.urls')),
    path('用电量/',include('用电量.urls')),
 
    path('武汉厂区/',include('武汉厂区.urls')),
    path('用水量/',include('用水量.urls')),
    path('产业园/',include('产业园.urls')),
    path('app/',include('app.urls')),
    path('',include('account.urls')),
]