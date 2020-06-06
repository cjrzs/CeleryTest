'''
coding:utf8
@Time : 2020/6/6 17:14
@Author : cjr
@File : urls.py
'''

from django.urls import path
from . import views

urlpatterns = [
    path('celery_test/', views.celery_test),
]
