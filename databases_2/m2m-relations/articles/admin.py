from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, ArticleTag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']


class ArticleTagInlineFormset(BaseInlineFormSet):
    """
    Переопределяем метод clean(), чтобы убедиться, что у каждой статьи есть ровно один основной раздел.
    """

    def clean(self):
        main_tags_count = sum(form.cleaned_data.get('is_main_tag', False)
                              for form in self.forms if not form.cleaned_data.get('DELETE'))
        if main_tags_count != 1:
            raise ValidationError("У каждой статьи должен быть ровно один основной раздел.")
        return super().clean()


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    extra = 1
    formset = ArticleTagInlineFormset


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [ArticleTagInline]
