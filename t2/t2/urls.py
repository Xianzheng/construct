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
    path('维修情况/',include('维修情况.urls')),
    path('基础数据W/',include('基础数据W.urls')),
    path('基础数据/',include('基础数据.urls')),
    path('武汉分公司/',include('武汉分公司.urls')),
    path('使用时长/',include('使用时长.urls')),
    path('app/',include('app.urls')),
    path('',include('account.urls')),
]
