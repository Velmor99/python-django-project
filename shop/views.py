from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): # имя index - потому что эта функция отвечает за страницу "/" в приложении shop
    return HttpResponse("<main><h1>Hello from the Shop app</h1><p>This is my first app</p></main>")