from django.contrib import admin

# Register your models here.
from .models import Post, PostCategory, PostImages, SiteContacts

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

class PostImagesInline(admin.StackedInline):
    model = PostImages


class PostAdmin(admin.ModelAdmin):
    list_display = ("title",)
    list_display_links = ("title", )
    list_filter = ("category", )
    search_fields = ("title", )
    inlines = (PostImagesInline,)


admin.site.register(SiteContacts)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, CategoryAdmin)