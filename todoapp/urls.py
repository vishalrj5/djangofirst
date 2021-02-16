"""mytodoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.urls import path
from todoapp.views import create_task,addTask,calc,ad,sub,mul

urlpatterns = [
    path('create', create_task),
    path('add',addTask,name="add"),
    path('calc',calc),
    path('addition',ad,name='calc1'),
    path('sub',sub,name='calc2'),
    path('mul',mul,name="calc3"),
]
