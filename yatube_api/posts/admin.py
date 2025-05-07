from django.contrib import admin

from .models import Group, Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "text",
        "pub_date",
        "author",
        "group",
        "image",
    )
    search_fields = ("text",)
    list_filter = ("pub_date",)
    list_editable = ("group",)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "description",
    )
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("slug",)
    list_filter = ("title",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "text", "created")
