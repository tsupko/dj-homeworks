from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsAuthorOrAdmin
from advertisements.serializers import AdvertisementSerializer
from rest_framework import viewsets, permissions


class AdvertisementViewSet(viewsets.ModelViewSet):
    """ViewSet для объявлений."""

    # Используем get_queryset вместо статичного queryset для корректной фильтрации.

    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        elif self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        else:  # update, partial_update, destroy
            permission_classes = [permissions.IsAuthenticated, IsAuthorOrAdmin]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        """
        Возвращает базовый QuerySet.
        Фильтры из URL будут применены к нему автоматически.
        """
        return Advertisement.objects.all()
