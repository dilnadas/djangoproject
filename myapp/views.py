from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fn_myIndex(request):
    return HttpResponse('welcome to django')
def fn_index(request):
    lang = ['c']
    return render(request,'index.html',{'list1':lang})   