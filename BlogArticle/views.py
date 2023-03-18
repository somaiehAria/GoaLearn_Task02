from django.shortcuts import render, redirect
from django.http import request
from .models import Article, Category, MyUser
from .forms import UserRegisterForm, LoginForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

################## indexPage View ##################
def index(request):
    context = {
        "articles": Article.objects.all(),
        # "category": Category.objects.all()
    }
    return render(request, 'Blog/index.html', context)

################## detailArticle View ##################
def detail_article(request, slug):
    context = {
        "article": Article.objects.get(slug=slug)
       }
    return render(request, 'Blog/detail.html', context)

################## articleCategory View ##################
def article_category(request, slug):
    context = {
        "category": Category.objects.get(slug=slug)
       }   
    return render(request, 'Blog/category.html', context)

################## userRegistration View ##################   
def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = MyUser.objects.create_user(
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                age = form.cleaned_data['age'],
                gender = form.cleaned_data['gender'],
                mobile_number = form.cleaned_data['mobile_number'],
                user_name = form.cleaned_data['user_name'],
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password'],
            )
            user.save()
            return redirect('BlogArticle:login')
    else:
        form = UserRegisterForm()
    return render(request, 'Blog/register.html', {'form': form})

################## userLogin View ##################
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Logged in as {username}!')
                return redirect('BlogArticle:home')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'Blog/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('BlogArticle:home')





