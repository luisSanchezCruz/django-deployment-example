from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url('user_login', views.user_login, name='user_login'),
    url('register/', views.register, name='register'), 
    url('', views.index, name='index') 
]