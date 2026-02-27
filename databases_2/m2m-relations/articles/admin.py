from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, ArticleTag


class ArticleTagInlineFormset(BaseInlineFormSet):
    """
    Переопределяем метод clean(), чтобы убедиться, что у каждой статьи есть ровно один основной раздел.
    """
    def clean(self):
        main_tags_count = sum(form.cleaned_data.get('is_main_tag', False)
                              for form in self.forms if not form.cleaned_data.get('DELETE'))
        if main_tags_count == 0:
            raise ValidationError("Укажите основной раздел")
        if main_tags_count != 1:
            raise ValidationError("Основным может быть только один раздел")
        return super().clean()


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    extra = 1
    formset = ArticleTagInlineFormset
    fields = ('tag', 'is_main_tag')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [ArticleTagInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
