from django.urls import path

from .views import (
    blog
)

urlpatterns=[
    path("post/",blog , name="post"),
]

