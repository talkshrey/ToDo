from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CreateUser
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from toDoApp.models import TaskList
from toDoApp.forms import TaskCreate
from django.http import HttpResponse
from django.contrib.auth import login as user_login 
from django.contrib.auth import logout as user_logout 

# Create your views here.
def home(request):
    context = {}
    return render(request, 'temp.html', context)


def upload(request):
    upload = TaskCreate()
    if request.method == 'POST':
        upload = TaskCreate(request.POST)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'index.html', {'index':upload}) 

def update_task(request, task_id):
    task_id = int(task_id)
    try:
        task_sel = TaskList.objects.get(id = task_id)
    except TaskList.DoesNotExist:
        return redirect('index')
    task_form = TaskCreate(request.POST or None, instance = task_sel)
    if task_form.is_valid():
       task_form.save()
       return redirect('index')
    return render(request, 'update.html', {'upload_form':task_form})

def delete_task(request, task_id):
    task_id = int(task_id)
    try:
       task_sel = TaskList.objects.get(id = task_id)
    except TaskList.DoesNotExist:
        return redirect('index')
    task_sel.delete()
    return redirect('index')


def home_page(request):
    obj = TaskList.objects.all().order_by('priority_order')
    context = {
        'obj': obj
    }
    return render(request, 'display.html', context)
# authentication

def signup(request):
    userForm = CreateUser()
    if request.method == 'POST':
        userForm = CreateUser(request.POST, request.FILES)
        if userForm.is_valid():
            userForm.save()
            return redirect('login')
    return render(request, 'signup.html', {'details':userForm})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password = password)
        if user is not None:
            form = user_login(request, user)
            return redirect('index')   
    form = AuthenticationForm()   
    context = {'form':form, 'title':'login'}
    return render(request, 'login.html', context)

def logout(request):
    if request.method == 'POST':
        user_logout(request)
        return redirect('home')
    return render(request, 'temp.html', {})