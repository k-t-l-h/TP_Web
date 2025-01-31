"""AskNumbers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ask/',views.ask, name='ask'),
    path('hot/',views.hot, name='hot'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('question/<int:pk>/',views.question, name='question'),
    path('settings/',views.settings, name='settings'),
    path('signup/',views.signup, name='signup'),
    path('new_question/',views.new_question, name='new_question'),
    path('new_answer/',views.new_answer, name='new_answer'),
    path('tag/',views.tag, name='tag'),
]
