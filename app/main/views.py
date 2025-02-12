from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request) -> HttpResponse:
    context = {
        'title': 'Home',
        'content': 'Welcome'

    }
    return render(request, 'main/index.html',context)
def about(request) -> HttpResponse:
    return HttpResponse('About')