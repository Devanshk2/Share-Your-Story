from django.shortcuts import render,HttpResponse,redirect
from home.models import  Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as dj_login ,logout as dj_logout
from django.contrib import messages

# Create your views here.
def home(request):
    # return HttpResponse('This is home')
    return render(request,'home/home.html')
def about(request):
    return render(request,'home/about.html')
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        if len(name)<2 or len(email)<5 or len(phone)<10 or len(content)<5:
            messages.error(request,'Please provide information correctly!')
        else:
            contact=Contact(name=name,email=email,issue=content,phone=phone)
            contact.save()
            messages.success(request,'Your message has been sent successfully!')
    return render(request,'home/contact.html')
def signup(request):
    
    if request.method == 'POST':
        # get the inputs
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        #create user
        if(len(username)>2 and username.isalnum() and len(password)>2):
            myuser = User.objects.create_user(username,email,password)
            myuser.save()
            messages.success(request,'Welcome to YouBlog')
            myuser=authenticate(username=username,password=password)        #to login just after registration
            dj_login(request,myuser)
            return redirect('home')
        else:
            messages.error(request, "length of username and password must be atleast 3 characters")
            return redirect('/signup')
    # else:
    #     return HttpResponse("Not Found")
    return render(request,'home/signup.html')
    
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            messages.success(request,"Welcome Back, " +username )
            dj_login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Please provide valid credentials!")
            return redirect('/login')
    return render(request,'home/login.html')

def logout(request):
    dj_logout(request)
    messages.success(request,"successfully logged out")
    return redirect(home)


