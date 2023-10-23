from django.db import models

class SiteContacts(models.Model):
    email = models.EmailField("Email")
    phone = models.CharField("Phone", max_length=20)
    address=models.CharField("Address",max_length=100)
    facebook_link = models.URLField("Facebook")
    twiter_link = models.URLField("Twiter")
    youtube_link = models.URLField("YouTube")
    instagram_link = models.URLField("Instagram")

    class Meta:
        verbose_name = "Site Contacts"
        verbose_name_plural = "Site Contacts"

    def __str__(self):
        return "Contacts"


class PostCategory(models.Model):
    name = models.CharField("Category", max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name
    


class Post(models.Model):
    title = models.CharField("Title", max_length=100)
    content = models.TextField("Content")
    category = models.ManyToManyField(PostCategory, related_name="posts", )
    image = models.ImageField("Image", upload_to="publications/")
    created_at = models.DateField("Date fo publication", auto_now_add=True)

    class Meta:
        verbose_name = "Publication"
        verbose_name_plural = "Publications"

    def __str__(self):
        return self.title


class PostImages(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="extra_images")
    image = models.ImageField("Image", upload_to="publications/")

    class Meta:
        verbose_name = "Post image"
        verbose_name_plural = "Post images"

    def __str__(self):
        return self.post.title
    

class CommentPost(models.Model):
    author=models.ForeignKey("account.User", related_name="post_commnets", on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    parent=models.ForeignKey("self", on_delete=models.CASCADE, related_name="sybcommnets", null=True, blank=True)


    