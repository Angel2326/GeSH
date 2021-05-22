from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from adminapp.forms import UserAdminRegisterForm, UserRegisterForm, UserAdminProfileForm
from authapp.models import New_user


# Create your views here.

def index(request):
    return render(request, 'adminapp/admin.html')


def admin_users_read(request):
    context = {'users': New_user.objects.all()}
    return render(request, 'adminapp/admin-users-read.html', context)


def admin_users_create(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь успешно создан')
            return HttpResponseRedirect(reverse('admin_staff:admin_users_read'))
        else:
            print(form.errors)
    form = UserAdminRegisterForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-users-create.html', context)


def admin_users_update(request, user_id):
    selected_user = New_user.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=selected_user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно изменены')
            return HttpResponseRedirect(reverse('admin_staff:admin_users_read'))
        else:
            print(form.errors)
    form = UserAdminProfileForm(instance=selected_user)
    context = {'form': form, 'selected_user': selected_user}
    return render(request, 'adminapp/admin-users-update-delete.html', context)
