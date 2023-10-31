#I made this file - Piyush
from django.http import HttpResponse
from django.shortcuts import render

list=["HI"]

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
def login(request):
    return render(request,"Resgis_login.html")

list=[{'user':"Hi",'bot':"Hello"},{'user':"Thank you",'bot':"Bye"}]
def home(request):
    user_chat= request.GET.get('user-input')
    bot_response="Hi Iam a bot"
    
    item={'user':user_chat,'bot':bot_response}
    
    list.append(item)
    length=len(list)
    params = {'list':list,'length':length}
    return render(request,"home.html",params)