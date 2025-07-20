from django.shortcuts import render
from .models import User
from django.http import Http404

# Create your views here.

def user_list(request):
    users = User.email.all()
    
    return render(
        request,
        'my_django_project\user\list.html',
         {'users':users}
    )

def user_detail(request, id):
    try:
        user = User.email.get(id=id)
    except User.DoesNotExist:
        raise Http404("No User found.")
    return render (request, 'my_django_project\user\detail.html', {'user':user})    
