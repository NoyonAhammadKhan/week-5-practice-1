from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'id': 'required'}))

    class Meta:
        model = User
        fields = ['username', 'email']


# don't have in requirements

# class UpdateUserData(UserChangeForm):
#     password = None

#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email']
