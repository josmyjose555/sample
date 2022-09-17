from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.models import User,auth

from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=='POST':

        first_name=request.POST['fname']
        Last_name=request.POST['lname']
        Username=request.POST['uname']
        email=request.POST['email']
        password1=request.POST['pswd']
        password2=request.POST['pswd1']

        if password1==password2:

            if User.objects.filter(username=Username).exists():

                messages.info(request,'Username exist')
                return redirect('/register/register')

            else:
                user= User.objects.create_user(username=Username,password=password1, email=email, first_name=first_name, last_name=Last_name)
                user.save();
                messages.info(request,'sign in successful')
                return redirect('/login')
                
                
        else:
            messages.warning(request,'Password not match')
            return redirect('/register/register')
              

    else:
        
        return render(request, 'register.html')
