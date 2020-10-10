from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    return render(request, 'basic_app/index.html')

@login_required(login_url='basic_app:user_login')
def special(request):
    return HttpResponse('YOU ARE LOGED IN , NICE')

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

def register(request):
    
    registered = False
    if request.method == 'POST':
        
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context_data = {
        'user_form' : user_form,
        'profile_form' : profile_form,
        'registered' : registered,
    }

    return render(request, 'basic_app/registration.html', context = context_data)

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse('ACOUNT IS NOT ACTIVE')
        else:
            print('Someone tried to login and failed!')
            print('Username: {} and Password: {}'.format(username, password))
            return HttpResponse('INVALID LOGIN DETAILED SUPPLIED!')
    else:
        context = {}
        return render(request, 'basic_app/login.html',context)




