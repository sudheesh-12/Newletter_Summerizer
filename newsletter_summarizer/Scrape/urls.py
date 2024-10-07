from django.urls import path
from . import views

urlpatterns = [
    path('',views.head_function,name="head_function")
]
