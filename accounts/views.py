from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,' invalid credintial ')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if  request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']
        email=request.POST['email']    

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username is taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save();
                return redirect('login')

        else:
            messages.info(request,'Password not matching..')
            return redirect('register')
    else:

        return render(request,'register.html')

def logout2(request):
    auth.logout(request)
    return redirect('/')

