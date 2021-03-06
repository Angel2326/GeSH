from authapp.forms import UserRegisterForm, UserProfileForm
from authapp.models import New_user
from django import forms

class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input'}), required=False)
class Meta:
    model = New_user
    fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4'}))

