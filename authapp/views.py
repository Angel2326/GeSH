from django.shortcuts import render
from authapp.forms import New_userLoginForm
from django.contrib import auth
from django.urls import reverse
from django.http import HttpResponseRedirect

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
    context = {'title' :'GeekShop - Авторизация','form':user_form}
    return render(request,'authapp/login.html', context)
# Create your views here.
