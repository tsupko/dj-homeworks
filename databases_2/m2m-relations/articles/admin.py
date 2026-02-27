from django.contrib import admin

from .models import Article, Tag, ArticleTag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    extra = 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [ArticleTagInline]
