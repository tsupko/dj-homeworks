from django.contrib import admin

from .models import Article, Tag, Relationship


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']


class RelationshipInline(admin.TabularInline):
    model = Relationship


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [RelationshipInline]
