from django.urls import path
from . import views

app_name = 'my_django_project'

urlpatterns = [
    path('hello/', views.hello, name= 'hello'),
    path('users/', views.user_list, name= 'users'),
    path('new_user/', views.new_user, name='new_user'),
    path('users/<int:id>/', views.user_detail, name='user_detail'),
]