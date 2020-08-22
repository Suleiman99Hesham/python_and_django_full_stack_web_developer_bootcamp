from django.urls import path
from sec_app import views

urlpatterns = [
    path('',views.users, name = 'users')
]
