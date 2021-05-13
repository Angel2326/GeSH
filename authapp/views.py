from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import New_userLoginForm, UserRegisterForm


def login(request):
    if request.method == 'POST':
        user_form = New_userLoginForm(data=request.POST)
        if user_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))

    else:
        user_form = New_userLoginForm()
    context = {'title': 'GeekShop - Авторизация', 'form': user_form}
    return render(request, 'authapp/login.html', context)


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    form = UserRegisterForm()
    context = {'title': 'GeekShop - Регистрация', 'form': form}
    return render(request, 'authapp/register.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))