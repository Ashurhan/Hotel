from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    avatar = models.ImageField("Аватарка" , upload_to="account/", default="default_avatar.png" )
    phone = models.CharField("Номер телефона", max_length=14,null=True)
    email= models.EmailField("Почта", unique=True)


    class Meta:
        verbose_name="Пользователь"
        verbose_name_plural="Пользоветели"

    def __str__(self):
        return self.username
    
    @property
    def full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()


class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField("Отзыв")


    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["-created"]

    def str(self):
        return f"{self.content}"[:100]

class Employees(models.Model):
    avatar = models.ImageField(
        upload_to="users/avatars/",
        null=True, # для базы
        blank=True, # для формы 
        verbose_name="Фото профиля"
    )
    full_name=models.CharField(max_length=100,null=False,default=None)
    email=models.CharField(max_length=100,null=False)
    post = models.CharField(max_length=50,null=False,default=None)
