from django.shortcuts import render
from django.http import HttpResponse
from .models import Course


# Create your views here.
def index(request): # имя index - потому что эта функция отвечает за страницу "/" в приложении shop
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})
    # return HttpResponse("".join([f"{course}</br>" for course in courses]))