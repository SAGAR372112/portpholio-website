from django.contrib import admin
from .models import Category, Tag, Blog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "description")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "published_date", "category", "view_count")
    list_filter = ("status", "category", "tags")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "content")
    filter_horizontal = ("tags",)

    fieldsets = (
        ("Content", {
            "fields": ("title", "slug", "content", "category", "tags")
        }),
        ("Publishing", {
            "fields": ("status", "published_date"),
        }),
    )
