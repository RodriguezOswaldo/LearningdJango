
from django.shortcuts import render
from django.http import HttpResponse


def my_view(request):
    return HttpResponse('Hello World from <b style="color:white; margin:1px;padding: 10px;font-size:23px;background:#134b33">dJango</b>!!')
