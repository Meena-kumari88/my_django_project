from django.shortcuts import render, redirect
from .models import User
from django.http import Http404, HttpResponse
from .forms import UserForm

# Create your views here.

def hello(request):
    return HttpResponse("Hello World")

def user_list(request):
    users = User.objects.all()
    
    return render(
        request,
        'my_django_project/user/users.html',
         {'users':users}
    )

def user_detail(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        raise Http404("No User found.")
    return render (request, 'my_django_project/user/detail.html', {'user':user}) 

def new_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        role = request.POST.get('role')
        
        if name and email and role:
            User.objects.create(name=name, email=email, role=role)
            return redirect('my_django_project:users')
    return  render(request, 'my_django_project/user/new_user.html')    

