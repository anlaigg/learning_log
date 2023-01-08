"""为应用程序users 定义URL模式"""
from django.urls import path,include
from . import views

app_name = 'users'
urlpatterns = [
	# 包含默认身份验证URL
	path('',include('django.contrib.auth.urls')),
	path('register', views.register, name='register'),
]