from distutils.command.upload import upload
from tkinter import messagebox
from django.http import HttpResponse
from shop.models import shop

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    shops=shop.objects.all()
    return render(request,'index.html',{'shopss':shops})

def add_item(request):
    if request.method=='POST':
        p_name=request.POST['product_name']
        p_desc=request.POST['product_desc']
        p_price=request.POST['product_price']
        p_offer=request.POST['product_offer']
        p_image=request.FILES['product_image']
        p=shop.objects.create(name=p_name,desc=p_desc,price=p_price,offer=p_offer,img=p_image)
        p.save();
        # return  HttpResponse('item added')
        return redirect('/login')
    else:
       return render(request,'new_entry.html')

def login(request):
    return render(request,'login.html')  