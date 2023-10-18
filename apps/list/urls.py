from django.urls import path

from .views import (
    index,
    room_details,
    all_rooms,
    about_us,
    contact,
    blog,
    blog_details
)


urlpatterns=[
    path("", index,name="page"),
    path("room_details/<int:room_pk>",room_details,name="room_details" ),
    path("all_rooms/",all_rooms, name="all_rooms"),
    path("about_us", about_us, name="about_us"),
    path("contact/", contact, name="contact"),
    path("blog/", blog, name="blog"),
    path("blog_details", blog_details, name="blog_details")
]


