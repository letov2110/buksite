from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import UserReg, LoginUser,EditUser
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from tutor.models import Tutor
from .models import MyUser
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page

# @cache_page(60*10)
def register(request):
    error_msg = ""
    if request.method == 'POST':
        user_form = UserReg(request.POST)
        if user_form.is_valid():
            if len(user_form.cleaned_data['password']) < 8 or sum(c.isalpha() for c in user_form.cleaned_data['password']) < 2:
                error_msg = "Пароль должен быть не менее 8 символов, из которых 2 буквы"
                return render(request, 'reglog/register.html', {'user_form': user_form, 'error': error_msg})
            
            username = user_form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                error_msg = "Пользователь с таким именем уже существует"
                return render(request, 'reglog/register.html', {'user_form': user_form, 'error': error_msg})
            
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('login')
        else:
            error_msg = user_form.errors
    else:
        user_form = UserReg()
    return render(request, 'reglog/register.html', {'user_form': user_form, 'error': error_msg})



def user_login(request):
    log=LoginUser()
    if request.method == "POST":
        log=LoginUser(request,data=request.POST)
        if log.is_valid():
            user = authenticate(
                request,
                username=request.POST.get("username"),
                password=request.POST.get("password"),
            )
            if user is not None:
                login(request, user)
                return redirect('myprofile')
    return render(request, "reglog/login_page.html", {"login": log})

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def myprofile(request):   
    user = request.user
    posts= Tutor.objects.filter(author=request.user)
    return render(request, 'reglog/myprofile.html', {'posts':posts,'user': user})

@login_required(login_url='login')
def profile(request, user_id):
    user = MyUser.objects.get(id=user_id)
    posts = Tutor.objects.filter(author=user)
    return render(request, 'reglog/profile.html', {'posts': posts, 'user': user})

@login_required(login_url='login')
def editprofile(request):
    user = request.user
    if request.method == 'POST':
        profform = EditUser(request.POST, request.FILES, instance=user.myuser)
        if profform.is_valid():
            profform.save()
            return redirect('myprofile')
    else:
        profform=EditUser(instance=user.myuser)
    return render(request, 'reglog/editprofile.html', {'profform': profform})

def user_list(request):
    users = MyUser.objects.exclude(ava__isnull=True)
    user = request.user
    return render(request, 'reglog/user_list.html', {'users': users,'user':user})
