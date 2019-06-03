from django.shortcuts import render


def hello(request):
    return render(request,'demotest/hello.html')

# Create your views here.
