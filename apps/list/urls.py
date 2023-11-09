from django.urls import path

from .views import (
    index,
    room_details,
    all_rooms,
    about_us,
    contact,
    room_comment,
    delete_comment,
    employees,
)


urlpatterns=[
    path("", index,name="page"),
    path("room_details/<int:room_pk>",room_details,name="room_details" ),
    path("all_rooms/",all_rooms, name="all_rooms"),
    path("about_us", about_us, name="about_us"),
    path("contact/", contact, name="contact"),
    path("room/comment/<int:room_pk>", room_comment, name="room_comment"),
    path("room/comments/delete/<int:comment_pk>", delete_comment, name="delete_comment"),
    path("employees",employees,name="employees"),
]


