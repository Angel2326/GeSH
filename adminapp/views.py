from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from authapp.models import New_user
from adminapp.forms import UserAdminRegisterForm, UserRegisterForm
from django.contrib import messages

# Create your views here.

def index(request):

    return render(request, 'adminapp/admin.html')


def admin_users_read(request):
    context = {'users':New_user.objects.all()}
    return render(request, 'adminapp/admin-users-read.html', context)

def admin_users_create(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь успешно создан')
            return HttpResponseRedirect(reverse('admin_staff:admin_users_read'))
        else:
            print(form.errors)
    form = UserAdminRegisterForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-users-create.html', context)
