from django.urls import path
from . import views 
# from views import say_hello

# from playground.views import say_hello
# Mapping url to views
#urlconf

urlpatterns=[
path('hello/',views.say_hello,name='hello')
]