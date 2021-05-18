<<<<<<< Updated upstream
=======
<<<<<<< Updated upstream
=======
<<<<<<< Updated upstream
=======
from django.contrib.auth.decorators import login_required
>>>>>>> Stashed changes
>>>>>>> Stashed changes
>>>>>>> Stashed changes
from django.contrib import auth, messages
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from authapp.forms import New_userLoginForm, UserRegisterForm, UserProfileForm
<<<<<<< Updated upstream

=======
<<<<<<< Updated upstream

=======
<<<<<<< Updated upstream

=======
from basketapp.models import Basket
>>>>>>> Stashed changes
>>>>>>> Stashed changes
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream

=======
<<<<<<< Updated upstream

=======
<<<<<<< Updated upstream

=======
@login_required
>>>>>>> Stashed changes
>>>>>>> Stashed changes
>>>>>>> Stashed changes
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
<<<<<<< Updated upstream
    context = {'title': 'Geekshop - Личный Кабинет', 'form': form}
=======
<<<<<<< Updated upstream
    context = {'title': 'Geekshop - Личный Кабинет', 'form': form}
=======
<<<<<<< Updated upstream
    context = {'title': 'Geekshop - Личный Кабинет', 'form': form}
=======
    context = {
        'title': 'Geekshop - Личный Кабинет',
        'form': form,
        'baskets': Basket.objects.all(),
    }
>>>>>>> Stashed changes
>>>>>>> Stashed changes
>>>>>>> Stashed changes
    return render(request, 'authapp/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
