from django.urls import path
from basicapp import views

urlpatterns = [
    path('', views.Form_name_view, name = 'form'),
]
