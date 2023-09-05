from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from user.models import User

# Create your views here.

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        User.objects.create_user(username=username, password = password)
        return redirect("/todo/")
    elif request.method == "GET":
        return render(request, "user/signup.html")
    else:
        return HttpResponse("Invalid request method", status=405)
    

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:    # DB에 있는 username이랑 PW가 입력한 것과 일치한다
            auth_login(request, user)
            return redirect("/todo/")
        else:
            return HttpResponse("Invalid auth", status=401)
    
    elif request.method == "GET":
        return render(request, "user/login.html")
    
    else:
        return HttpResponse("Invalid request method", status=405)


def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return redirect("/todo/")
    else:
        return HttpResponse("Invalid request method", status=405)



def whoami(request):
    print(request.user)
    return HttpResponse(request.user)