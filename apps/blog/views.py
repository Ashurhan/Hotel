from django.shortcuts import render , get_object_or_404, redirect
from .models import Post
from .forms import CommentForm
def blog(request):
    posts=Post.objects.all()
    context={
        "posts":posts
    }

    return render(request, "blog.html", context)


def blog_details(request,post_pk):
    post=get_object_or_404(Post,pk=post_pk)

    return render(request, "blog-details.html",{"post": post})

def write_comments(request,post_pk):
    post=Post.objects.all(pk=post_pk)
    if request.method =="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author=request.user
            comment.save()
            return redirect("blog-details", post_pk=post.pk)