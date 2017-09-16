from django.http import HttpResponse
from django.shortcuts import render_to_response

def search(request):
    return render_to_response('search.html');

def searchresult(request):
    request.encoding = 'utf-8';
    if 'context' in request.GET:
        message = 'The contnet you search is ' + request.GET['context'];
    return HttpResponse(message);
