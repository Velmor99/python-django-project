from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Course


# Create your views here.
def index(request): # имя index - потому что эта функция отвечает за страницу "/" в приложении shop
    courses = Course.objects.all()
    return render(request, 'shop/courses.html', {'courses': courses})
    # return HttpResponse("".join([f"{course}</br>" for course in courses]))

def single_course(request, course_id):
    # option 1
    # try:
    #     course = Course.objects.get(pk=course_id)
    #     return render(request, "shop/single_course.html", {"course": course})
    # except Course.DoesNotExist:
    #     raise Http404()
    
    # option 2
    course = get_object_or_404(Course, pk=course_id)
    return render(request, "shop/single_course.html", {"course": course})