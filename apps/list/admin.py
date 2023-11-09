from django.contrib import admin
from . models import Category, RoomIMage, Rooms, Contact, Booking,CommentRoom,RestaurantMenu, RestaurantImage, RestaurantBook,RestaurantCategory


admin.site.register(Category)
admin.site.register(Rooms)
admin.site.register(Contact)
admin.site.register(RoomIMage)
admin.site.register(Booking)
admin.site.register(CommentRoom)
admin.site.register(RestaurantMenu)
admin.site.register(RestaurantCategory)
admin.site.register(RestaurantImage)
admin.site.register(RestaurantBook)