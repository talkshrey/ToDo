from collections import namedtuple
from django.urls import path
from django.urls.conf import include
from . import views
from django.contrib.auth import views as auth

urlpatterns = [
    path('home/', views.upload, name='index'),
    path('', views.home, name='home'),
    path('display/', views.home_page, name='display'),
    path('upload/', views.upload, name='upload'),
    path('update/<int:task_id>', views.update_task, name='update'),
    path('delete/<int:task_id>', views.delete_task, name='delete'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]