from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        # Get Form Value
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        username =request.POST['username']
        email =request.POST['email']
        password =request.POST['password']
        password2 =request.POST['password2']
        
        #Check If Password mathes
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already taken..!")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,"Email already taken ..!")
                    return redirect("register")
                else:
                    user=User.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name)
                    #LogIn User directly 
                    # auth.login(request,user)
                    # messages.success(request,"You are succesfully loggedIn ..!")
                    # return redirect("index")    

                    user.save()
                    messages.success(request,"You are succesfully registerd ..!")
                    return redirect("login")

        else:
            messages.error(request,"Both passwords should be matched..!")
            return redirect('register')
    else:
        return render(request,"accounts/register.html")


def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"You are not logged in ..!")
            return redirect("dashboard")
        else:
            messages.error(request,"Invalid Credentials..!")
            return redirect("login")   
    else:    
        return render(request,"accounts/login.html")



def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request,"You Logout..!")
        return redirect("index")



def dashboard(request):
    return render(request,"accounts/dashboard.html")        