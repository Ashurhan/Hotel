from typing import Any
from django import forms

from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from .models import Contact, Booking , CommentRoom, RestaurantBook
import datetime



class ContactForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = (
            "name",
            "email",
            "message",
            "phone",
            "captcha",
        )
        widgets = {
            "name": forms.TextInput(attrs={"placeholder":"Your username"}),
            "email":forms.EmailInput(attrs={"placeholder":"Your email"}),
            "message":forms.TextInput(attrs={"placeholder":"Message"}),
            "phone":forms.TextInput(attrs={"placeholder":"Your phone"})
        }


    
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if not name.isalpha() and " " not in name:
            raise ValidationError("Имя должно содержать буквы и может включать пробелы.")
        return name

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if not phone.isdigit():
            raise ValidationError("Номер телефона должен содержать только цифры.")
        return phone

class BookingRoomForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = (
            "check_in",
            "check_out",
            "adult",
            "children"
        )

    def clean(self) -> dict[str, Any]:
        check_in = self.cleaned_data["check_in"]
        check_out = self.cleaned_data["check_out"]

        if check_in > check_out:
            raise ValidationError({"check_in":"Неправильно указана дата!"})
        elif check_in < datetime.date.today():
            raise ValidationError({"check_in": "Выберите дату в будущем времени!"})
        return super().clean()

    
class RoomCommentForm(forms.ModelForm):
    class Meta:
        model=CommentRoom
        fields=(
            "text",
            "rating",
        )

class AnswerCommentForm(forms.ModelForm):
    class Meta:
        model=CommentRoom
        fields=(
            "text",
        )


class BookTable(forms.ModelForm):
    class Meta:
        model = RestaurantBook
        fields = [
            "name",
            "phone",
            "email",
            "time",
            "persons"
           
        ]
        form_control = {"class":"login__input"}
        widgets = {
            "name":forms.TextInput(attrs={"class":"login__input",'type':'text',"placeholder":"Full name"}),
            "phone":forms.TextInput(attrs={"class":"login__input",'type':'tel',"placeholder":"Phone"}),
            "email":forms.EmailInput(attrs={"class":"login__input",'type':'email',"placeholder":"Email"}),
            "time":forms.DateTimeInput(attrs={"class":"login__input","type":"datetime-local"}),
            "persons":forms.TextInput(attrs={"class":"login__input",'type':'text',"placeholder":"Persons"})
        }



