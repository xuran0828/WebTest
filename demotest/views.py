from django.shortcuts import render
from demotest.models import Test
from django.http import HttpResponseRedirect
#def hello(request):
    #treturn render(request,'demotest/hello.html')
#这里进行request请求的时候，对应着demotest地下的templates中的文件名
# Create your views here.
def add(request):
    test=Test(name='google')
    print("i am aksdmskdj")
    test.save()
    context={'test':test}
    return render(request,'demotest/add.html',context)
def deletes(request):
    print("i am a dsdl adsskdd")
    test=Test.objects.get(id=4)
    print("i am akdds")
    test.delete()
    return render(request,'demotest/deletes.html')
def updates(request):
    test=Test.objects.get(id=5)
    test.name='baidu'
    test.save()
    return render(request,'demotest/updates.html')
def checks(request):
    test=Test.objects.all()
    print(test)
    return render(request,'demotest/check.html')
