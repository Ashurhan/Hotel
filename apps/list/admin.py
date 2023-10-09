from django.contrib import admin
from . models import Category, RoomIMage, Rooms, Contact, Booking


admin.site.register(Category)
admin.site.register(Rooms)
admin.site.register(Contact)
admin.site.register(RoomIMage)
admin.site.register(Booking)
