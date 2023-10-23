from django.urls import path

from .views import (
    blog,
    blog_details,
    write_comments
)

urlpatterns=[
    path("post/",blog , name="post"),
    path("blog-details/<int:post_pk>", blog_details, name="blog-details"),
    path("comment/write/<int:post_pk>", write_comments, name="comment_create")

]

