from rest_framework import permissions


class IsAuthorOrAdmin(permissions.BasePermission):
    """
    Разрешает доступ только автору объекта или администратору.
    """

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.creator == request.user
