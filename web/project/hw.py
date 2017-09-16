from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello, Django');

def indexhw(request):
    return HttpResponse('Hello World');

def hello(request):
    context = {};
    context['hello'] = 'Hello World!';
    return render(request, 'hello.html', context);
