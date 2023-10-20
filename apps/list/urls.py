from django.urls import path

from .views import (
    index,
    room_details,
    all_rooms,
    about_us,
    contact,
    booking_index,
    write_comments
)


urlpatterns=[
    path("", index,name="page"),
    path("room_details/<int:room_pk>",room_details,name="room_details" ),
    path("all_rooms/",all_rooms, name="all_rooms"),
    path("about_us", about_us, name="about_us"),
    path("contact/", contact, name="contact"),
    path("booking",booking_index,name="booking"),
    path("comment/write/", write_comments, name="comment_create")
]


