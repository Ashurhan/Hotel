from django import forms
from .models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password','placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password','placeholder':'Repeat password'}))

    
    class Meta:
        model = User
        fields=(
            "username",
            "email",
            "password",
            "password2"
        )
        form_control = {"class":"login__input"}
        widgets = {
            "username": forms.TextInput(attrs={"placeholder":"Your username"}),
            "email":forms.EmailInput(attrs={"placeholder":"Your email"})
        }

    
    def clean(self):
        super().clean()
        password = self.cleaned_data["password"]
        password2 = self.cleaned_data["password2"]
        if password != password2:
            raise ValidationError({"password": "Пароли не совпали!"})
        

class LoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', "placeholder":"password"}))


    class Meta:
        model = User
        fields = ("username", "password")

        widgets = {
            "username": forms.TextInput(attrs={"placeholder":"Your username"}),
        }

    def clean_username(self):
        data = self.cleaned_data["username"]
        try:
            User.objects.get(username=data)
        except User.DoesNotExist:
            raise ValidationError({"username": "Такой пользователь не существует!"})
        
        return data


class UserBaseForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "avatar",
        )
