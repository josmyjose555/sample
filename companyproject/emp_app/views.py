from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'index.html',{'name':'Josmy'})
def add(request):
    var1=int(request.POST['n1'])
    var2=int(request.POST['n2'])
    sum=var1+var2

    return render(request,'result.html',{'Result':sum})