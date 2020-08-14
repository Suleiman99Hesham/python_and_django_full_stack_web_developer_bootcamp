from django.urls import path ,re_path, include
from first_app import views

urlpatterns = [
    re_path(r'^$', views.index),
]
