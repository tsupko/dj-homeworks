from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Advertisement, AdvertisementStatusChoices


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""
    creator = UserSerializer(read_only=True)

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator', 'status', 'created_at')

    def create(self, validated_data):
        """Метод для создания."""
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        user = self.context["request"].user
        is_creating = self.instance is None
        is_opening = self.instance and data.get('status') == AdvertisementStatusChoices.OPEN

        if is_creating or is_opening:
            open_count = Advertisement.objects.filter(
                creator=user,
                status=AdvertisementStatusChoices.OPEN
            ).count()

            # Если это обновление, не считаем текущее объявление в лимит
            if not is_creating:
                open_count -= 1

            if open_count >= 10:
                raise serializers.ValidationError(
                    {'status': 'У пользователя не может быть более 10 открытых объявлений.'}
                )
        return data
