from django.contrib.auth.forms import  AuthenticationForm

from authapp.models import New_user

class New_userLoginForm(AuthenticationForm):
    class Meta:
        model = New_user
        fields = ('username','password')