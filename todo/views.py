from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.decorators import login_required
from todo.models import Todo


# Create your views here.

def index(request):
    if request.method == "GET":
        todos = Todo.objects.all()
        print(todos)
        context = {
            "todos":todos,   
        }
        return render(request, "todo/index.html", context)
    else:
        return HttpResponse("Invalid request method", status=405)

@login_required(login_url='/user/login/')   # login url은 redirect할 url
@csrf_exempt
def create(request):

    if request.method == "POST":
        Todo.objects.create(
            content=request.POST['content'], 
            user=request.user,
            image = request.FILES.get("image")
        )
        return redirect("/todo/")
    elif request.method == "GET":
        return render(request, "todo/create.html")
    else:
        return HttpResponse("Invalid request method", status=405)

    
def read(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {
            "todo":todo,   
        }
    return render(request, "todo/detail.html", context)

@csrf_exempt
def delete(request, todo_id):
    if request.method == "POST": 
        todo = Todo.objects.get(id=todo_id)
        if request.user == todo.user:   # 다른 api에서? 접속해서 삭제하려고 하는 걸 막기 위한 장치/벡엔드에서 꼭 해줘야 함!
            todo.delete()
            return redirect("/todo/")
        else:
            return HttpResponse("You are not allowed to delete this todo", status=403)
    else:
        return HttpResponse("Invalid request method", status=405)

@csrf_exempt  
def update(request, todo_id):
    if request.method == "POST":
        todo = Todo.objects.get(id=todo_id)
        if request.user == todo.user:
            todo.content = request.POST["content"]
            todo.save()
            return redirect(f"/todo/{todo_id}/")
        else:
            return HttpResponse("You are not allowed to delete this todo", status=403)
    elif request.method == "GET":
        todo = Todo.objects.get(id=todo_id)
        context = {
            "todo":todo,   
        }
        return render(request, "todo/update.html", context)
    else:
        return HttpResponse("Invalid request method", status=405)