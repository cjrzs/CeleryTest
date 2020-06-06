from django.shortcuts import render

# Create your views here.
# 标准模块
import time
# django模块
from django.http import HttpResponse
# 自定义模块
from .tasks import test


def celery_test(request):
    s1 = 'hello, cjr2'
    # print(1)
    # time.sleep(5)
    # print(2)
    test.delay()
    return HttpResponse(f'{s1}')
