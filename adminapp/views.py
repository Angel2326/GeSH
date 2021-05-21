from django.shortcuts import render
from authapp.models import New_user


# Create your views here.

def index(request):
    return render(request, 'adminapp/admin.html')


def admin_users_read(request):
    context = {'users':New_user.objects.all()}
    return render(request, 'adminapp/admin-users-read.html', context)
