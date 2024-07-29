from django.shortcuts import render

from django.http import HttpResponse




# def say_hello(request):
#     return HttpResponse('Hello world')
  


# in other frame work what we could view in django we called it as teplates
def  say_hello(request):
    return render(request,'hello.html',{'name':"Deepak"})
