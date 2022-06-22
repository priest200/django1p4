from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *


@login_required(login_url='login-user/')
def index(request):

    posts = Post.objects.all()
    businesses = Business.objects.all()
    contacts = Contacts.objects.all()
    find_business(request)
    return render(request, 'html/index.html', {"posts": posts, "businesses":businesses, "contacts":contacts})


@login_required(login_url='login-user/')
def add_post(request):
    name = request.POST.get('title')
    description = request.POST.get("description")
    post = Post(title=name, description=description, user=request.user)
    post.save()
    return redirect('index-page')


@login_required(login_url='login-user/')
def create_business(request):
    name = request.POST.get('b-name')
    email = request.POST.get('b-email')
    business = Business(name=name, user=request.user, neighborhood=request.user.profile.neighborhood, email=email)
    business.save()
    return redirect('index-page')


@login_required(login_url='login-user/')
def create_neigborhood(request):
    name = request.POST.get('name')
    location = request.POST.get('location')
    hood = Neighborhood(name=name, location=location, admin=request.user)
    hood.save()
    return redirect('index-page')


@login_required(login_url='login-user/')
def delete_business(request, id):
    Business.objects.get(id=id).delete()
    return redirect('profile')


@login_required(login_url='login-user/')
def delete_neighborhood(request, id):
    Neighborhood.objects.get(id=id).delete()
    return redirect('profile')


@login_required(login_url='login-user/')
def find_business(request):
    if request.method == "POST":
        search = request.POST["search"]
        businesses = Business.objects.filter(name__contains=search)
        print(search)
        return render(request, "html/index.html", {"search": search, "businesses": businesses})
    return render(request, "html/index.html", {})


@login_required(login_url='/login-user')
def find_neigborhood(request, id):
    if request.method == "POST":
        search = request.POST["search"]
        hoods = Neighborhood.objects.filter(name__contains=id)
        return render(request, "html/index.html", {"search": search, "hoods": hoods})
    return render(request, "html/index.html", {})


@login_required(login_url='login-user/')
def update_business(request):
    return redirect('index-page')


@login_required(login_url='/login-user')
def update_neighborhood(request, id):
    return render(request, "html/index.html", {})


@login_required(login_url='login-user/')
def my_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    businesses = Business.objects.filter(user=user)
    hoods = Neighborhood.objects.filter(admin=user)

    if request.method == "POST":
        username = request.POST.get('username')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        profile.profile_pic = request.FILES['profile_pic']
        profile.caption = request.POST.get("bio")
        profile.neighborhood = request.POST.get('n-hood')

        user = User.objects.filter(username=user.username).update(username=username, first_name=fullname, email=email)
        profile.save()
    return render(request, 'html/profile.html', {"profile": profile, 'businesses': businesses, "hoods": hoods})


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile()
            profile.user = user
            profile.save()
            login(request, user)
            messages.success(request, "Account created successfully")
            return redirect('index-page')
        else:
            for error in form.error_messages:
                messages.error(request, form.error_messages[error])
                print(error)
                return render(request, 'html/register.html', {"form": form})
    else:
        form = RegisterForm()
    return render(request, 'html/register.html', {"form": form})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index-page')
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'html/login.html', {})

    return render(request, 'html/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('login-user')
