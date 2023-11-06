from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60,help_text="Required",widget=forms.TextInput(attrs={'class': 'form-control'}))
    # username = forms.EmailField(max_length=60,help_text="Required",widget=forms.TextInput(attrs={'class': 'form-control'}))
    # password1 = forms.EmailField(max_length=60,help_text="Required",widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # password2 = forms.EmailField(max_length=60,help_text="Required",widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Account
        fields = ("email","username","password1","password2")


class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=60,help_text="Required",widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email = email, password = password):
            raise forms.ValidationError("Invalid Login")