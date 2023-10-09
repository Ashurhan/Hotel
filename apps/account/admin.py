from django.contrib import admin
from .models import User , Comment , Employees

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    context= User.objects.all()

admin.site.register(Comment)
admin.site.register(Employees)

