from django.contrib import admin

from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "published", "published_at", "created_at")
    list_editable = ("order", "published")
    list_filter = ("published",)
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "excerpt")
    ordering = ("order", "-published_at", "-created_at")
