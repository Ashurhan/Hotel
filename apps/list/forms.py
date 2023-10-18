from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from ..account.models import Comment
from .models import Contact, Booking 
import datetime



class ContactForm(forms.ModelForm):
    class Meta:
        model= Contact
        fields=(
            "name",
            "email",
            "message",
            "phone",
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

    
class CommentForm(forms.ModelFrom):
    class Meta:
        model = Comment
        fields=(
            "text"
        )
        