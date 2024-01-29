from rest_framework import permissions


class IsOwnerOrManagerOrAdmin(permissions.BasePermission):
    """
    Проверяем, является ли текущий пользователь владельцем объявления или менеджером или админом.
    """

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.user.role == 'MANAGER' or obj.user == request.user
