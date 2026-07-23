from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "featured", "published", "created_at")
    list_editable = ("order", "featured", "published")
    list_filter = ("published", "featured")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "description")
    ordering = ("order", "-created_at")
