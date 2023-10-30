from django.shortcuts import render , get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Post , CommentPost
from .forms import CommentForm , AnswerCommentForm
def blog(request):
    posts=Post.objects.all()
    context={
        "posts":posts
    }

    return render(request, "blog.html", context)

@login_required
def blog_details(request,post_pk):
    post=get_object_or_404(Post,pk=post_pk)
    comments = post.comments.filter(parent=None)

    return render(request, "blog-details.html",{"post": post, "comments": comments})


@login_required
def write_comments(request,post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post  # Set the post for the comment
            comment.save()
            return redirect("blog-details", post_pk=post.pk)
        



@login_required
def answer_comment(request, comment_id):
    parent_comment = get_object_or_404(CommentPost, pk=comment_id)
    
    if request.method == "POST":
        form =AnswerCommentForm (request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.parent = parent_comment
            comment.post_id = parent_comment.post_id
            comment.save()
            return redirect(request.META.get('HTTP_REFERER'))
    
    form = AnswerCommentForm()
    return render(request, "blog-details.html", {"form": form, "parent_comment": parent_comment})


@login_required
def delete_comment(request, comment_pk):
    comment= CommentPost.objects.get(pk=comment_pk)
    
    if comment not in request.user.post_commnets.all():
        return redirect("blog-details", post_pk=comment.post.pk)
    
    comment.delete()
    return redirect(request.META.get('HTTP_REFERER'))


