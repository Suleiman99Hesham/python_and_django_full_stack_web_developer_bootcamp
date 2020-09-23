from django.shortcuts import render
from sec_app.models import User
from sec_app.forms import Register
# Create your views here.

def index(request):
    users_data = User.objects.order_by('first_name')
    users_dict = {
        'users' : users_data,
    }
    return render(request, 'sec_app/index.html', context = users_dict)

def register(request):
    form = Register()
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            User = form.save(commit = True)
            form = Register()
            return index(request)
        else:
            print("ERROR FROM INVALID")
            
    return render(request, 'sec_app/register.html', {"form" : form})