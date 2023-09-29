from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from User.models import Courses,Course_details,Account
import json
from django.http import JsonResponse
import os
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

# Create your views here.

# def custom_404(request, exception=None):
#     return render(request, '404.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('HomePage')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            
            user=auth.authenticate(email=email, password=password)
            
            if user is not None:
                auth.login(request,user)
                user = request.user
                return redirect('HomePage')
            else:
                messages.error(request, "Invalid Credentials....")
                return redirect('login')
        return render(request, 'login.html')
    


@login_required(login_url = 'login')
def logout(request):
    request.session.flush()
    auth.logout(request)
    return redirect('login')


@login_required(login_url = 'login')
def Course(request):
    course = Courses.objects.all()
    
    
    paginator = Paginator(course,3)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    context = {
        'courses' : paged_products
    }
    return render(request,'short-course-view.html',context)


@login_required(login_url = 'login')
def Course_Create(request):
    if request.method == 'POST':
        image = request.FILES['image']
        title = request.POST['title']
        subtitle = request.POST['subtitle']
        description = request.POST['description']
        status = request.POST['status']
        
        course = Courses.objects.create(image=image,title=title,subtitle=subtitle,description=description)
        last_id = course.id
        
        current_course = Courses.objects.get(id=last_id)
        
        Course_details.objects.create(course = current_course,
                title= request.POST['dtitle1'],
                description = request.POST['ddesc1'])
        
        return render(request,'short-course-create.html')
    else:
        return render(request,'short-course-create.html')
    


@login_required(login_url = 'login')   
def Del_course(request):
    body = json.loads(request.body)
    id = body['id']
    
    course = Courses.objects.get(id=id)
    course.delete()
    data ={
        'data':"Completed"
    }
    return JsonResponse(data)



@login_required(login_url = 'login')
def Edit_course(request,id):
    if request.method == 'POST':
        course = Courses.objects.get(id=id)
        if not request.FILES.get('image'):
            Courses.objects.filter(id=id).update(
                title = request.POST['title'],
                subtitle = request.POST['subtitle'],
                description = request.POST['description'],
                status = request.POST['status'],
            )
            return redirect('course')
        else:
            os.remove(course.image.path)
            course.image = request.FILES['image']
            course.save()
            
            Courses.objects.filter(id=id).update(
                title = request.POST['title'],
                subtitle = request.POST['subtitle'],
                description = request.POST['description'],
                status = request.POST['status'],
            )
            
            return redirect('course')
    else:
        context = {
            'course': Courses.objects.get(id=id)
        }
        return render(request,'short-course-edit.html',context)
        
        
@login_required(login_url = 'login')
def Profile(request):
    if request.method == 'POST':
        oldpass=request.POST['oldpass']
        password=request.POST['password']
        password1=request.POST['password1']
        
        user = Account.objects.get(username__exact=request.user.username)

        success = user.check_password(oldpass)
        if success:
            if password == password1:
                user.set_password(password)
                user.save()
                messages.success(request, 'Password Change Completed')
                auth.logout(request)
                return redirect('login')
                
            else:
                messages.success(request,'Passwords Must Be Same...')
                return render(request,'profile.html')
        else:
            messages.error(request, "Invalid Old Password....")
            return render(request,'profile.html')
    else:
        return render(request,'profile.html')