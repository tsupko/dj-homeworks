from advertisements.models import Advertisement
from django.contrib import admin


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    """
    Настройка внешнего вида и поведения модели Объявление в админ-панели.
    """
    # 1. Какие поля показывать в общем списке объявлений
    list_display = ('id', 'title', 'status', 'creator', 'created_at')

    # 2. Какие поля будут ссылками на страницу редактирования
    list_display_links = ('id', 'title')

    # 3. Добавить боковую панель для быстрой фильтрации
    list_filter = ('status', 'creator', 'created_at')

    # 4. Добавить поиск по заголовку и описанию
    search_fields = ('title', 'description')

    # 5. Поля, доступные только для чтения (например, даты)
    readonly_fields = ('created_at', 'updated_at')

    # 6. Поля, по которым можно искать автора
    raw_id_fields = ('creator',)
