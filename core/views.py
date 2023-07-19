from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login as LoginUser,logout
from core.forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TodoForm()
        todos = Todo.objects.filter(user = user).order_by('priority')
        context = {
            "form":form,
            "todos":todos,
        }
        return render(request,'index.html',context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            LoginUser(request,user)
            return redirect('home')
        else:
            messages.error(request,'Please Enter The Valid Username and Password')
            return redirect('login')
        
    context = {}
    return render(request,'login.html',context)
        
def signup(request):

    if request.method == 'GET':
        form = createUserForm()
        context = {
            "form" : form
        } 
        return render(request,'signup.html',context)
    
    else:
        print(request.POST)
        form = createUserForm(request.POST)
        context = {
            "form" : form
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                messages.success(request,'Account Was Created Successfully!')
                return redirect('login')
        else:
            return render(request,'signup.html',context)

@login_required(login_url='login')       
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TodoForm(request.POST)
        context = {
            "form" : form,
        }
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            print(todo)
            return redirect("home")
        else:
            return render(request,'index.html',context)
        
def signout(request):
    logout(request)
    return redirect("login")

def delete_todo(request,id):
    Todo.objects.get(pk=id).delete()
    return redirect('home')

def change_status_todo(request,id,status):
    todo = Todo.objects.get(pk=id)
    todo.status = status
    todo.save()
    return redirect('home')

