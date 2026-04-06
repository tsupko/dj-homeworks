import django_filters as filters
from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    # Фильтр для даты (диапазон "от" и "до")
    created_at = filters.DateFromToRangeFilter(field_name='created_at')

    # Фильтр для статуса (точное совпадение)
    status = filters.CharFilter(field_name='status')

    # Фильтр для создателя (по ID пользователя)
    creator = filters.NumberFilter(field_name='creator')

    class Meta:
        model = Advertisement
        # Указываем все поля, по которым будет возможна фильтрация. Это активирует фильтры.
        fields = ['created_at', 'status', 'creator']
