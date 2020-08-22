from django.shortcuts import render
from sec_app.models import User

# Create your views here.

def index(request):
    return render(request, 'sec_app/index.html')

def users(request):
    users_data = User.objects.order_by('first_name')
    users_dict = {
        'users' : users_data,
    }
    return render(request, 'sec_app/users.html', context = users_dict)