'''
coding:utf8
@Time : 2020/6/6 18:49
@Author : cjr
@File : tasks.py
'''
# Create your tasks here
from __future__ import absolute_import, unicode_literals
import time
from celery import shared_task


@shared_task
def test():
    print(1)
    time.sleep(5)
    print(2)
