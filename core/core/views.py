#I made this file - Piyush
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

list=["HI"]

def login(request):
    if request.method == 'POST':
        username = request.POST.get['username']
        password = request.POST.get['password']
        username1 = str(username)
        password1 = str(password)
        user = authenticate(request, username=username1, password=password1)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'login.html')

def index(request):
    text = request.GET.get('text','default')
    list.append(text)
    params={'list':list}
    return render(request,'index.html',params)
    # return HttpResponse("<h1>Hello World</h1>")

def about(request):
    return HttpResponse("This is about route page")

def submitted(request):
    text = request.GET.get('text','default')
    params={'textarea':text}
    return render(request,"submit.html",params)

list=[{'user':"Hi",'bot':"Hello"},{'user':"Thank you",'bot':"Bye"}]
def home(request):
    user_chat= request.GET.get('user-input')
    bot_response="Hi Iam a bot"
    
    item={'user':user_chat,'bot':bot_response}
    
    list.append(item)
    length=len(list)
    params = {'list':list,'length':length}
    return render(request,"home.html",params)