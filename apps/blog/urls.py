from django.urls import path

from .views import (
    blog,
    blog_details,
    write_comments,
    answer_comment,
    delete_comment
)

urlpatterns=[
    path("post/",blog , name="post"),
    path("blog-details/<int:post_pk>", blog_details, name="blog-details"),
    path("comment/write/<int:post_pk>", write_comments, name="comment_create"),
    path("answer_comment/<int:comment_id>", answer_comment,name="answer_comment"),
    path("post/comments/delete/<int:comment_pk>", delete_comment, name="delete_comment"),


]


