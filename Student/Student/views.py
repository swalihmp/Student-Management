from django.shortcuts import render
from User.models import Courses
from django.contrib.auth.decorators import login_required

# Create your views here.

# def custom_404(request, exception=None):
#     return render(request, '404.html')



@login_required(login_url = 'login')
def HomePage(request):
    course = Courses.objects.all()
    context ={
        'total':course.count()
    }
    return render(request,'index.html',context)